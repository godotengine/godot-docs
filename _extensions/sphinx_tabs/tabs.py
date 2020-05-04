""" Tabbed views for Sphinx, with HTML builder """

import base64
import json
import posixpath
import os
from docutils.parsers.rst import Directive
from docutils import nodes
from pygments.lexers import get_all_lexers
from sphinx.util.osutil import copyfile

DIR = os.path.dirname(os.path.abspath(__file__))


FILES = [
    'tabs.js',
    'tabs.css',
    'semantic-ui-2.2.10/segment.min.css',
    'semantic-ui-2.2.10/menu.min.css',
    'semantic-ui-2.2.10/tab.min.css',
    'semantic-ui-2.2.10/tab.min.js',
]


LEXER_MAP = {}
for lexer in get_all_lexers():
    for short_name in lexer[1]:
        LEXER_MAP[short_name] = lexer[0]


class TabsDirective(Directive):
    """ Top-level tabs directive """

    has_content = True

    def run(self):
        """ Parse a tabs directive """
        self.assert_has_content()
        env = self.state.document.settings.env

        node = nodes.container()
        node['classes'] = ['sphinx-tabs']

        tabs_node = nodes.container()
        tabs_node.tagname = 'div'

        classes = 'ui top attached tabular menu sphinx-menu'
        tabs_node['classes'] = classes.split(' ')

        env.temp_data['tab_titles'] = []
        env.temp_data['is_first_tab'] = True
        self.state.nested_parse(self.content, self.content_offset, node)

        tab_titles = env.temp_data['tab_titles']
        for idx, [data_tab, tab_name] in enumerate(tab_titles):
            tab = nodes.container()
            tab.tagname = 'a'
            tab['classes'] = ['item'] if idx > 0 else ['active', 'item']
            tab['classes'].append(data_tab)
            tab += tab_name
            tabs_node += tab

        node.children.insert(0, tabs_node)

        return [node]


class TabDirective(Directive):
    """ Tab directive, for adding a tab to a collection of tabs """

    has_content = True

    def run(self):
        """ Parse a tab directive """
        self.assert_has_content()
        env = self.state.document.settings.env

        args = self.content[0].strip()
        try:
            args = json.loads(args)
            self.content.trim_start(1)
        except ValueError:
            args = {}

        tab_name = nodes.container()
        self.state.nested_parse(
            self.content[:1], self.content_offset, tab_name)
        args['tab_name'] = tab_name

        if 'tab_id' not in args:
            args['tab_id'] = env.new_serialno('tab_id')

        data_tab = "sphinx-data-tab-{}".format(args['tab_id'])

        env.temp_data['tab_titles'].append((data_tab, args['tab_name']))

        text = '\n'.join(self.content)
        node = nodes.container(text)

        classes = 'ui bottom attached sphinx-tab tab segment'
        node['classes'] = classes.split(' ')
        node['classes'].extend(args.get('classes', []))
        node['classes'].append(data_tab)

        if env.temp_data['is_first_tab']:
            node['classes'].append('active')
            env.temp_data['is_first_tab'] = False

        self.state.nested_parse(self.content[2:], self.content_offset, node)
        return [node]


class GroupTabDirective(Directive):
    """ Tab directive that toggles with same tab names across page"""

    has_content = True

    def run(self):
        """ Parse a tab directive """
        self.assert_has_content()

        group_name = self.content[0]
        self.content.trim_start(2)

        for idx, line in enumerate(self.content.data):
            self.content.data[idx] = '   ' + line

        tab_args = {
            'tab_id': base64.b64encode(
                group_name.encode('utf-8')).decode('utf-8')
        }

        new_content = [
            '.. tab:: {}'.format(json.dumps(tab_args)),
            '   {}'.format(group_name),
            '',
        ]

        for idx, line in enumerate(new_content):
            self.content.data.insert(idx, line)
            self.content.items.insert(idx, (None, idx))

        node = nodes.container()
        self.state.nested_parse(self.content, self.content_offset, node)
        return node.children


class CodeTabDirective(Directive):
    """ Tab directive with a codeblock as its content"""

    has_content = True

    def run(self):
        """ Parse a tab directive """
        self.assert_has_content()

        args = self.content[0].strip().split()
        self.content.trim_start(2)

        lang = args[0]
        tab_name = ' '.join(args[1:]) if len(args) > 1 else LEXER_MAP[lang]

        for idx, line in enumerate(self.content.data):
            self.content.data[idx] = '      ' + line

        tab_args = {
            'tab_id': '-'.join(tab_name.lower().split()),
            'classes': ['code-tab'],
        }

        new_content = [
            '.. tab:: {}'.format(json.dumps(tab_args)),
            '   {}'.format(tab_name),
            '',
            '   .. code-block:: {}'.format(lang),
            '',
        ]

        for idx, line in enumerate(new_content):
            self.content.data.insert(idx, line)
            self.content.items.insert(idx, (None, idx))

        node = nodes.container()
        self.state.nested_parse(self.content, self.content_offset, node)
        return node.children


class _FindTabsDirectiveVisitor(nodes.NodeVisitor):
    """ Visitor pattern than looks for a sphinx tabs
        directive in a document """
    def __init__(self, document):
        nodes.NodeVisitor.__init__(self, document)
        self._found = False

    def unknown_visit(self, node):
        if not self._found and isinstance(node, nodes.container) and \
           'classes' in node and isinstance(node['classes'], list):
            self._found = 'sphinx-tabs' in node['classes']

    @property
    def found_tabs_directive(self):
        """ Return whether a sphinx tabs directive was found """
        return self._found


# pylint: disable=unused-argument
def add_assets(app, pagename, templatename, context, doctree):
    """ Add CSS and JS asset files """
    if doctree is None:
        return
    visitor = _FindTabsDirectiveVisitor(doctree)
    doctree.walk(visitor)
    assets = ['sphinx_tabs/' + f for f in FILES]
    css_files = [posixpath.join('_static', path)
                 for path in assets if path.endswith('css')]
    script_files = [posixpath.join('_static', path)
                    for path in assets if path.endswith('js')]
    if visitor.found_tabs_directive:
        if 'css_files' not in context:
            context['css_files'] = css_files
        else:
            context['css_files'].extend(css_files)
        if 'script_files' not in context:
            context['script_files'] = script_files
        else:
            context['script_files'].extend(script_files)
    else:
        for path in css_files:
            if 'css_files' in context and path in context['css_files']:
                context['css_files'].remove(path)
        for path in script_files:
            if 'script_files' in context and path in context['script_files']:
                context['script_files'].remove(path)
# pylint: enable=unused-argument


def copy_assets(app, exception):
    """ Copy asset files to the output """
    builders = ('html', 'readthedocs', 'readthedocssinglehtmllocalmedia',
                'singlehtml')
    if app.builder.name not in builders:
        app.warn('Not copying tabs assets! Not compatible with %s builder' %
                 app.builder.name)
        return
    if exception:
        app.warn('Not copying tabs assets! Error occurred previously')
        return
    app.info('Copying tabs assets... ', nonl=True)

    installdir = os.path.join(app.builder.outdir, '_static', 'sphinx_tabs')

    for path in FILES:
        source = os.path.join(DIR, path)
        dest = os.path.join(installdir, path)

        destdir = os.path.dirname(dest)
        if not os.path.exists(destdir):
            os.makedirs(destdir)

        copyfile(source, dest)
    app.info('done')


def setup(app):
    """ Set up the plugin """
    app.add_directive('tabs', TabsDirective)
    app.add_directive('tab', TabDirective)
    app.add_directive('group-tab', GroupTabDirective)
    app.add_directive('code-tab', CodeTabDirective)
    app.connect('html-page-context', add_assets)
    app.connect('build-finished', copy_assets)
