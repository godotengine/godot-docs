.. _doc_batch_building_templates:

Batch building templates
========================

The following is almost the same script that we use to build all the
export templates that go to the website. If you want to build or roll them
yourself, this might be of use.

(note: Apple stuff is missing)

::

    #This script is intended to run on Linux or OSX. Cygwin might work.

    # if this flag is set, build is tagged as release in the version
    # echo $IS_RELEASE_BUILD

    #Need to set path to EMScripten
    export EMSCRIPTEN_ROOT=/home/to/emscripten

    #Build templates

    #remove this stuff, will be created anew
    rm -rf templates
    mkdir -p templates


    # Windows 32 Release and Debug

    scons -j 4 p=windows target=release tools=no bits=32
    cp bin/godot.windows.opt.32.exe templates/windows_32_release.exe
    upx templates/windows_32_release.exe 
    scons -j 4 p=windows target=release_debug tools=no bits=32
    cp bin/godot.windows.opt.debug.32.exe templates/windows_32_debug.exe
    upx templates/windows_32_debug.exe

    # Windows 64 Release and Debug (UPX does not support it yet)

    scons -j 4 p=windows target=release tools=no bits=64
    cp bin/godot.windows.opt.64.exe templates/windows_64_release.exe
    x86_64-w64-mingw32-strip templates/windows_64_release.exe 
    scons -j 4 p=windows target=release_debug tools=no bits=64
    cp bin/godot.windows.opt.debug.64.exe templates/windows_64_debug.exe
    x86_64-w64-mingw32-strip templates/windows_64_debug.exe

    # Linux 64 Release and Debug

    scons -j 4 p=x11 target=release tools=no bits=64
    cp bin/godot.x11.opt.64 templates/linux_x11_64_release
    upx templates/linux_x11_64_release
    scons -j 4 p=x11 target=release_debug tools=no bits=64
    cp bin/godot.x11.opt.debug.64 templates/linux_x11_64_debug
    upx templates/linux_x11_64_debug

    # Linux 32 Release and Debug

    scons -j 4 p=x11 target=release tools=no bits=32
    cp bin/godot.x11.opt.32 templates/linux_x11_32_release
    upx templates/linux_x11_32_release
    scons -j 4 p=x11 target=release_debug tools=no bits=32
    cp bin/godot.x11.opt.debug.32 templates/linux_x11_32_debug
    upx templates/linux_x11_32_debug

    # Server for 32 and 64 bits (always in debug)
    scons -j 4 p=server target=release_debug tools=no bits=64
    cp bin/godot_server.server.opt.debug.64 templates/linux_server_64
    upx templates/linux_server_64
    scons -j 4 p=server target=release_debug tools=no bits=32
    cp bin/godot_server.server.opt.debug.32 templates/linux_server_32
    upx templates/linux_server_32


    # Android
    **IMPORTANT REPLACE THIS BY ACTUAL VALUES**

    export ANDROID_HOME=/home/to/android-sdk
    export ANDROID_NDK_ROOT=/home/to/android-ndk

    # git does not allow empty dirs, so create those
    mkdir -p platform/android/java/libs/armeabi
    mkdir -p platform/android/java/libs/x86

    #Android Release 

    scons -j 4 p=android target=release
    cp bin/libgodot.android.opt.so platform/android/java/libs/armeabi/libgodot_android.so
    ./gradlew build
    cp platform/android/java/build/outputs/apk/java-release-unsigned.apk templates/android_release.apk

    #Android Debug

    scons -j 4 p=android target=release_debug
    cp bin/libgodot.android.opt.debug.so platform/android/java/libs/armeabi/libgodot_android.so
    ./gradlew build
    cp platform/android/java/build/outputs/apk/java-release-unsigned.apk templates/android_debug.apk

    # EMScripten

    scons -j 4 p=javascript target=release
    cp bin/godot.javascript.opt.html godot.html 
    cp bin/godot.javascript.opt.js godot.js 
    cp tools/html_fs/filesystem.js .
    zip javascript_release.zip godot.html godot.js filesystem.js
    mv javascript_release.zip templates/

    scons -j 4 p=javascript target=release_debug
    cp bin/godot.javascript.opt.debug.html godot.html
    cp bin/godot.javascript.opt.debug.js godot.js 
    cp tools/html_fs/filesystem.js .
    zip javascript_debug.zip godot.html godot.js filesystem.js
    mv javascript_debug.zip templates/

    # BlackBerry 10 (currently disabled)

    #./path/to/bbndk/bbndk-env.sh
    #scons -j 4 platform/bb10/godot_bb10_opt.qnx.armle target=release
    #cp platform/bb10/godot_bb10_opt.qnx.armle platform/bb10/bar

    #scons -j 4 platform/bb10/godot_bb10.qnx.armle target=release_debug
    #cp platform/bb10/godot_bb10.qnx.armle platform/bb10/bar
    #cd platform/bb10/bar
    #zip -r bb10.zip *
    #mv bb10.zip ../../../templates
    #cd ../../..


    # BUILD ON MAC

    [...]

    # Build release executables with editor

    mkdir -p release

    scons -j 4 p=server target=release_debug bits=64
    cp bin/godot_server.server.opt.tools.64 release/linux_server.64
    upx release/linux_server.64

    scons -j 4 p=x11 target=release_debug tools=yes bits=64
    cp bin/godot.x11.opt.tools.64 release/godot_x11.64
    # upx release/godot_x11.64 -- fails on some linux distros

    scons -j 4 p=x11 target=release_debug tools=yes bits=32
    cp bin/godot.x11.opt.tools.32 release/godot_x11.32

    scons -j 4 p=windows target=release_debug tools=yes bits=64
    cp bin/godot.windows.opt.tools.64.exe release/godot_win64.exe
    x86_64-w64-mingw32-strip release/godot_win64.exe
    #upx release/godot_win64.exe

    scons -j 4 p=windows target=release_debug tools=yes bits=32
    cp bin/godot.windows.opt.tools.32.exe release/godot_win32.exe
    x86_64-w64-mingw32-strip release/godot_win32.exe
    #upx release/godot_win64.exe

    [..] # mac stuff

    # Update classes.xml (used to generate doc)

    cp doc/base/classes.xml .
    release/linux_server.64 -doctool classes.xml


    cd demos
    rm -f godot_demos.zip
    zip -r godot_demos *
    cd ..

    cd tools/export/blender25
    zip -r bettercollada *
    mv bettercollada.zip ../../..
    cd ../../..
