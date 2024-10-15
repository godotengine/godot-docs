"""
## Migrate files from Godot to Redot

usage: Migrate [-h] [-e] [-t] [-v] input output

Simple file migrator. Uses str.replace to map from Godot to Redot. Also converts some filenames.

positional arguments:
  input           Input directory relative to current
  output          Output directory relative to current

options:
  -h, --help      show this help message and exit
  -e, --extended  Include unimplemented substitutions, don't use in production
  -t, --tiny      Exclude classes directory
  -v, --verbose

Will replace specific godot strings with redot. It tries to ignore external projects and other things that shouldn't
change.

A distinction is made between unimplemented instances of the godot keyword (for instance references to the main 
website), and implemented ones (like references to github repositories that are already compatible).

The idea is that, as the project is being migrated to the new name, the unimplemented mappings will gradually move
to the 'normal' mappings. This way the docs can grow along with the project, keeping broken links to a minimum. When
all is done, migrate.py has served its purpose and can be deleted.

It will recursively traverse all directories, targeting .rst and .md files. It will convert the text and filename
if necessary, and then save them to the output directory (default _migrated)

From there, the docs can be built in the normal way.
"""

import argparse
import fnmatch
import os
import re
from shutil import copyfile
import shutil
import sys
import codecs
from distutils.dir_util import copy_tree

defaultInputDirectory = '.'
defaultOutputDirectory = '_migrated'
defaultIncludeUnimplemented = False
defaultIgnoreClasses = True
defaultVerbose = False

encoding = 'utf-8'
filename_masks = ['.rst', '.md']

# Mappings that will currently lead to nowhere. Can be treated as a todo list.
mappings_unimplemented = [
    # Non existing urls
    ('https://hosted.weblate.org/projects/godot-engine/godot-docs', 'https://hosted.weblate.org/projects/redot-engine/redot-docs'),
    ('https://hosted.weblate.org/engage/godot-engine/', 'https://hosted.weblate.org/engage/redot-engine/'),
    ('https://store.steampowered.com/app/404790/Godot_Engine/', 'https://store.steampowered.com/app/TODO'),
    ('https://flathub.org/apps/details/org.godotengine.Godot', 'https://flathub.org/apps/details/org.redot-engine.Redot'),
    ('https://godot.foundation', 'https://redot.foundation'),
    ('https://hosted.weblate.org/projects/godot-engine/godot/', 'https://hosted.weblate.org/projects/redot-engine/redot/'),
    ('https://hosted.weblate.org/projects/godot-engine/', 'https://hosted.weblate.org/projects/redot-engine/'),
    ('https://hosted.weblate.org/browse/godot-engine', 'https://hosted.weblate.org/browse/redot-engine'),
    ('https://repo1.maven.org/maven2/org/godotengine/godot/', 'https://repo1.maven.org/maven2/org/redot-engine/redot/'),
    # The following mappings probably require changes to the core engine
    ('GodotEngine.epub', 'RedotEngine.epub'),
    ('godotengine.org/license', 'redotengine.org/license'),
    ('AsGodotDictionary', 'AsRedotDictionary'),
    ('GODOT_', 'REDOT_'),
    ('-godot-', '-redot-'),
    ('project.godot', 'project.redot'),
    ('Godot.Collections', 'Redot.Collections'),
    ('"Godot"', '"Redot"'),
    ('.godot/', '.redot/'),
    ('.godot.', '.redot.'),
    ('APPDATA%\\Godot\\', 'APPDATA%\\Redot\\'),
    ('AppData%\\Godot\\', 'AppData%\\Redot\\'),
    ('Caches/Godot/', 'Caches/Redot/'),
    ('cache/godot/', 'cache/redot/'),
    ('Support/Godot/', 'Support/Redot/'),
    ('config/godot/', 'config/redot/'),
    ('share/godot/', 'share/redot/'),
    ('org.godotengine.Godot', 'org.redotengine.Redot'),
    ('godot-ios-plugins', 'redot-ios-plugins'),
    ('godot-syntax-themes', 'redot-syntax-themes'),
    ('godot_skin', 'redot_skin'),
    ('godot_scene_node', 'redot_scene_node'),
    ('``godotengine/godot', '``redot-engine/redot'),
    ('>/Godot/', '>/Redot/'),
    ('``.godot``', '``.redot``'),
    ('``godot``', '``redot``'),
    ('/godot.', '/redot.'),
    ('GodotPhysics', 'RedotPhysics'),
    ('AsGodotObject', 'AsRedotObject'),
    ('non-Godot', 'non-Redot'),
    ('Godot-', 'Redot-'),
    ('libgodot', 'libredot'),
    ('godot.linuxbsd', 'redot.linuxbsd'),
    ('Godot.app', 'Redot.app'),
    ('MacOS/Godot', 'MacOS/Redot'),
    ('C:\\godot', 'C:\\redot'),
    ('GodotSharp', 'RedotSharp'),
    ('godot.gdkey', 'redot.gdkey'),
    ('godot-nir', 'redot-nir'),
    ('godot-angle', 'redot-angle'),
    ('godot-binary', 'redot-binary'),
    ('``Godot', '``Redot'),
    ('godot/modules', 'redot/modules'),
    ('godot_binary', 'redot_binary'),
    ('godotengine.org', 'redotengine.org'),
    ('godot-source', 'redot-source'),
    ('godot/bin', 'redot/bin'),
    ('gdb godot', 'gdb redot'),
    ('GODOT', 'REDOT'),
    ('USERNAME/godot', 'USERNAME/redot'),
    ('godot-xr', 'redot-xr'),
    ('godotisawesome', 'redotisawesome'),
    ('godot-cpp', 'redot-cpp'),
    ('GodotCPP', 'RedotCPP'),
    ('namespace godot', 'namespace redot'),
    ('godot_cpp', 'redot_cpp'),
    ('GodotObject', 'RedotObject'),
    ('GodotBot', 'RedotBot'),
    ('GodotPlugin', 'RedotPlugin'),
    ('org.godotengine', 'org.redotengine'),
    ('/godot>', '/redot>'),
    ('repos/godotengine/godot', 'repos/redot-engine/redot'),
    ('godot demo', 'redot demo'),
    ('godotsharp', 'redotsharp'),
]

# Mappings that should work on first migration
mappings = [
    # These will have to change eventually.
    ('https://nightly.link/godotengine/godot-docs/workflows/build_offline_docs/master/godot-docs-html-stable.zip', 'https://download.redotengine.org/docs/redot-docs-html-stable.zip'),
    ('https://nightly.link/godotengine/godot-docs/workflows/build_offline_docs/master/godot-docs-html-master.zip', 'https://download.redotengine.org/docs/redot-docs-html-master.zip'),
    ('https://nightly.link/godotengine/godot-docs/workflows/build_offline_docs/master/godot-docs-html-3.6.zip', 'https://download.redotengine.org/docs/redot-docs-html-3.6.zip'),
    ('https://nightly.link/godotengine/godot-docs/workflows/build_offline_docs/master/godot-docs-epub-stable.zip', 'https://download.redotengine.org/docs/redot-docs-epub-stable.zip'),
    ('https://nightly.link/godotengine/godot-docs/workflows/build_offline_docs/master/godot-docs-epub-master.zip', 'https://download.redotengine.org/docs/redot-docs-epub-master.zip'),
    ('https://nightly.link/godotengine/godot-docs/workflows/build_offline_docs/master/godot-docs-epub-3.6.zip', 'https://download.redotengine.org/docs/redot-docs-epub-3.6.zip'),
    # Table breakers
    ('| ``"Please include this when reporting the bug on: https://github.com/godotengine/godot/issues"`` |', '| ``"Please include this when reporting the bug on: https://github.com/redot-engine/godot/issues"``|'),
    ('https://github.com/godotengine/godot/pull/40364>`_ for more.     |', 'https://github.com/redot-engine/redot/pull/40364>`_ for more.    |'),
    # Non existing internal urls
    ('https://chat.godotengine.org/', 'https://www.redotengine.org/'),
    ('https://editor.godotengine.org', 'https://www.redotengine.org'),
    ('https://forum.godotengine.org/', 'https://www.redotengine.org/'),
    ('https://fund.godotengine.org', 'https://www.redotengine.org'),
    # Almost existing urls
    ('https://docs.godotengine.org/', '/'),
    ('https://docs.godotengine.org', 'https://docs.redotengine.org'),
    ('https://godotengine.org', 'https://redotengine.org'),
    # Existing urls
    ('https://godotengine.org/community', 'https://www.redot.org'),
    ('https://nightly.link/godotengine/godot-docs/workflows/build_offline_docs/master/godot', 'https://nightly.link/redot-engine/redot-docs/workflows/build_offline_docs/master/redot'),
    ('https://github.com/godotengine/godot-docs/issues', 'https://github.com/redot-engine/redot-docs/issues'),
    ('https://github.com/godotengine/godot/blob/master', 'https://github.com/redot-engine/redot/blob/master'),
    ('https://raw.githubusercontent.com/godotengine/godot/master', 'https://raw.githubusercontent.com/redot-engine/redot/master'),
    ('https://github.com/godotengine/godot-demo-projects', 'https://github.com/redot-engine/redot-demo-projects'),
    ('https://discord.gg/bdcfAYM4W9', 'https://discord.gg/redot'),
    ('https://github.com/godotengine/godot', 'https://github.com/redot-engine/redot'),
    ('https://github.com/godotengine/godot-proposals', 'https://github.com/redot-engine/redot-proposals'),
    ('https://raw.githubusercontent.com/godotengine/godot-docs', 'https://raw.githubusercontent.com/redot-engine/redot-docs'),
    ('https://github.com/godotengine/', 'https://github.com/redot-engine/'),
    ('https://chat.godotengine.org/', 'https://discord.gg/redot'),
    # Generic replacements
    ('GODOT_COPYRIGHT.txt', 'REDOT_COPYRIGHT.txt'),
    ('godotengine.org', 'redotengine.org'),
    ('godot-docs', 'redot-docs'),
    ('GODOT ENGINE', 'REDOT ENGINE'),
    ('/bin/godot', '/bin/redot'),
    ('/Applications/Godot.app', '/Applications/Redot.app'),
    ('highlight=Godot', 'highlight=Redot'),
    ('/godot_', '/redot_'),
    ('/godot-', '/redot-'),
    ('_godot_', '_redot_'),
    ('``godot``', '``redot``'),
    ('Godot ', 'Redot '),
    (' Godot', ' Redot'),
    (' Godot.', ' Redot.'),
    (' Godot?', ' Redot?'),
    ('Godot\'', 'Redot\''),
    ('Godot,', 'Redot,'),
    ('Godot:', 'Redot:'),
    (' godot ', ' redot '),
    ('\nGodot.', '\nRedot.'),
    ('_godot\n', '_redot\n'),
    ('godot.gif', 'redot.gif'),
    ('godot.jpg', 'redot.jpg'),
    ('godot.png', 'redot.png'),
    ('"godot_', '"redot_'),
    ('"godotengine"', '"redotengine"'),
    ('GodotEngine', 'RedotEngine'),
    ('godot-giscus', 'redot-giscus'),
    ('"godotengine/', '"redotengine/'),
    ('godot_is_latest', 'redot_is_latest'),
    ('godot-edit-guideline', 'redot-edit-guideline'),
    ('_godot_', '_redot_'),
    ('to_godot', 'to_redot'),
    ('godot.html', 'redot.html'),
    ('by-godot', 'by-redot'),
    ('RocketChat', 'Discord'),
    ('MadeWithGodot', 'MadeWithRedot'),
    (' if on_rtd else "(DEV) "', ''),
    ('<span class="fa fa-book"> Read the Docs</span>', '<span class="fa fa-book"> Versions</span>'),
    ("const homeUrl = baseUrl.split('/latest/')[0] + '/stable/';", "const homeUrl = 'https://docs-stable.redotengine.org/';"),
    ('{% set listed_languages = ({"en":"#", "de":"#", "es":"#", "fr":"#"}).items() -%}', '{% set listed_languages = ({"en":"#"}).items() -%}'),
    ('({"stable":"#", "latest":"#"})', '({"stable":"https://docs-stable.redotengine.org/", "latest":"https://docs-latest.redotengine.org/", "3.6":"https://docs-3-6.redotengine.org/"})'),
    ('Hosted by <a href="https://readthedocs.org">Read the Docs', 'Hosted by <a href="https://cloudflare.com">CloudFlare'),
    ('<a href="https://docs.readthedocs.io/page/privacy-policy.html">Privacy Policy</a>', ''),
    ('G-dot', 'Godot'),
    (' godot_', ' redot_'),
    ('class_godotsharp', 'class_redotsharp'),
]

filename_mappings = [
    ('godot', 'redot'),
]

static_dirs = [
    '**/img',
    '**/files',
    '_extensions',
    '_static',
    '_styleguides',
    '_templates',
    '_tools',
]

alphanumeric = [
    'py',
    'md',
    'css',
    'txt',
    'css',
    'js',
    'html',
    'csv',
    'rst',
]

# force stdout encoding so it won't fail on print statements
if (sys.stdout.encoding != encoding):
    sys.stdout = codecs.getwriter(encoding)(sys.stdout.buffer, 'strict')
    sys.stdout.encoding = encoding

def is_target(filename):
    return any(filename.lower().endswith(m) for m in filename_masks)

def ensureDirExists(outputName):
    dirname = os.path.dirname(outputName)
    try:
        os.makedirs(dirname)
    except FileExistsError:
        pass

def generateOutputName(root, fileName, outputDirectory):
    on = os.path.join('.', outputDirectory, root, fileName)
    on = convertContent(on, filename_mappings)
    ensureDirExists(on)
    return on

def convertContent(content, mappings):
    for mapping in mappings:
        search, replace = mapping
        if (search != ''):
            content = content.replace(search, replace)
    return content

def copyFile(root, filename, outputDirectory, verbose):
    inputName = os.path.join(root, filename)
    outputName = generateOutputName(root, inputName.replace('.\\', '').replace('./', ''), outputDirectory)

    if verbose: print(f'Copying "{inputName}" to "{outputName}"')
    shutil.copyfile(inputName, outputName)

def convertFile(root, filename, outputDirectory, includeUnimplemented, verbose):
    inputName = os.path.join(root, filename)
    outputName = generateOutputName(root, filename, outputDirectory)

    if verbose: print(f'Converting "{inputName}" to "{outputName}"')
    with open(inputName, mode = 'r', encoding = encoding) as input: 
        data = input.read()

        if (includeUnimplemented):
            data = convertContent(data, mappings_unimplemented)
        data = convertContent(data, mappings)
        ensureDirExists(outputName)
        with open(outputName, mode = 'w', encoding = encoding) as output:
            output.write(data)

def copyGlobalDir(inputDirectory, inputMask, outputDirectory, verbose):
    for root, dirs, files in os.walk(inputDirectory):
        if (inputMask in root and outputDirectory not in root):
            for f in files:
                inputName = os.path.join(root, f)
                outputName = generateOutputName(root, f, outputDirectory)
                ensureDirExists(outputName)
                if verbose: print(f"Copying {inputName} to {outputName}")
                copyfile(inputName, outputName)

def convertStaticDir(inputDirectory, outputDirectory, verbose):
    for root, dirs, files in os.walk(inputDirectory):
        if (outputDirectory not in root and '__' not in root):
            for f in files:
                if (f.split('.')[1] in alphanumeric):
                    convertFile(root, f, outputDirectory, True, verbose)
                else:
                    copyFile(root, f, outputDirectory, verbose)

def migrate(inputDirectory, outputDirectory, includeUnimplemented, ignoreClasses, verbose):
    outputsig = os.path.join('.', outputDirectory)
    for root, dirs, files in os.walk(inputDirectory):
        # ignore output path
        if (root.startswith(outputsig)):
            continue

        if (ignoreClasses and 'classes' in root):
            continue

        items = filter(is_target, files)
        for item in items:
            convertFile(root, item, outputDirectory, includeUnimplemented, verbose)

def main():
    inputDir = defaultInputDirectory
    outputDir = defaultOutputDirectory
    includeUnimplemented = defaultIncludeUnimplemented
    ignoreClasses = defaultIgnoreClasses
    verbose = defaultVerbose

    parser = argparse.ArgumentParser(
                    prog='Migrate',
                    description='Simple file migrator. Uses str.replace to map from Godot to Redot. Also converts some filenames.',
                    epilog='Done. Made by @Craptain')
    
    parser.add_argument('input', help='Input directory relative to current')
    parser.add_argument('output', help='Output directory relative to current')
    parser.add_argument('-e', '--extended', action='store_true', help='Include unimplemented substitutions, don\'t use in production')
    parser.add_argument('-t', '--tiny', action='store_true', help='Exclude classes directory')
    parser.add_argument('-v', '--verbose', action='store_true') 

    args = parser.parse_args()
    verbose = args.verbose
    if (verbose):
        print("arguments:")
        print(args)

    inputDir = args.input
    if (args.output != '.' and not args.output.startswith('/')):
        outputDir = args.output
    else:
        print("output can't be . or start with /")
        exit(1)
    includeUnimplemented = args.extended
    ignoreClasses = args.tiny

    if (os.path.exists(outputDir)):
        print(f"Deleting {outputDir}")
        shutil.rmtree(outputDir)
    
    print("Migrating...")
    migrate(inputDir, outputDir, includeUnimplemented, ignoreClasses, verbose)

    print("Copying config files...")
    convertFile(inputDir, 'conf.py', outputDir, includeUnimplemented, verbose)
    convertFile(inputDir, 'robots.txt', outputDir, includeUnimplemented, verbose)
    copyFile(inputDir, 'favicon.ico', outputDir, verbose)

    print("Copying static directories...")
    for dir in static_dirs:
        if ('**' in dir):
            if verbose: print(f"Copying dirs with mask {dir}")
            copyGlobalDir(inputDir, dir.split('/')[1], outputDir, verbose)
        else:
            if verbose: print(f"Converting dir {dir}")
            convertStaticDir(dir, outputDir, verbose)

    print(parser.epilog)

if __name__ == "__main__":
    main()
