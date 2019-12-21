.. _doc_cross-compiling_for_ios_on_linux:

Cross-compiling for iOS on Linux
================================

.. highlight:: shell

The procedure for this is somewhat complex and requires a lot of steps,
but once you have the environment properly configured it will be easy to
compile Godot for iOS anytime you want.

Disclaimer
----------

While it is possible to compile for iOS on a Linux environment, Apple is
very restrictive about the tools to be used (especially hardware-wise),
allowing pretty much only their products to be used for development. So
this is **not official**. However, a `statement from Apple in 2010
<http://www.apple.com/pr/library/2010/09/09Statement-by-Apple-on-App-Store-Review-Guidelines.html>`__
says they relaxed some of the `App Store review guidelines
<https://developer.apple.com/app-store/review/guidelines/>`__
to allow any tool to be used, as long as the resulting binary does not
download any code, which means it should be OK to use the procedure
described here and cross-compiling the binary.

Requirements
------------

-  `XCode with the iOS SDK <https://developer.apple.com/xcode/download>`__
   (a dmg image)
-  `Clang >= 3.5 <http://clang.llvm.org>`__ for your development
   machine installed and in the ``PATH``. It has to be version >= 3.5
   to target ``arm64`` architecture.
-  `Fuse <https://github.com/libfuse/libfuse>`__ for mounting and umounting
   the dmg image.
-  `darling-dmg <https://github.com/darlinghq/darling-dmg>`__, which
   needs to be built from source. The procedure for that is explained
   below.

   -  For building darling-dmg, you'll need the development packages of
      the following libraries: fuse, icu, openssl, zlib, bzip2.

-  `cctools-port <https://github.com/tpoechtrager/cctools-port>`__
   for the needed build tools. The procedure for building is quite
   peculiar and is described below.

   -  This also has some extra dependencies: automake, autogen, libtool.

Configuring the environment
---------------------------

darling-dmg
~~~~~~~~~~~

Clone the repository on your machine:

::

    $ git clone https://github.com/darlinghq/darling-dmg.git

Build it:

::

    $ cd darling-dmg
    $ mkdir build
    $ cd build
    $ cmake .. -DCMAKE_BUILD_TYPE=Release
    $ make -j 4  # The number is the amount of cores your processor has, for faster build
    $ cd ../..

Preparing the SDK
~~~~~~~~~~~~~~~~~

Mount the XCode image:

::

    $ mkdir xcode
    $ ./darling-dmg/build/darling-dmg /path/to/Xcode_7.1.1.dmg xcode
    [...]
    Everything looks OK, disk mounted

Extract the iOS SDK:

::

    $ mkdir -p iPhoneSDK/iPhoneOS9.1.sdk
    $ cp -r xcode/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS.sdk/* iPhoneSDK/iPhoneOS9.1.sdk
    $ cp -r xcode/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include/c++/* iPhoneSDK/iPhoneOS9.1.sdk/usr/include/c++
    $ fusermount -u xcode  # unmount the image

Pack the SDK:

::

    $ cd iPhoneSDK
    $ tar -cf - * | xz -9 -c - > iPhoneOS9.1.sdk.tar.xz

Toolchain
~~~~~~~~~

Build cctools:

::

    $ git clone https://github.com/tpoechtrager/cctools-port.git
    $ cd cctools-port/usage_examples/ios_toolchain
    $ ./build.sh /path/iPhoneOS9.1.sdk.tar.xz arm64

Copy the tools to a nicer place. Note that the SCons scripts for
building will look under ``usr/bin`` inside the directory you provide
for the toolchain binaries, so you must copy to such subdirectory, akin
to the following commands:

::

    $ mkdir -p /home/user/iostoolchain/usr
    $ cp -r target/bin /home/user/iostoolchain/usr/

Now you should have the iOS toolchain binaries in
``/home/user/iostoolchain/usr/bin``.

Compiling Godot for iPhone
--------------------------

Once you've done the above steps, you should keep two things in your
environment: the built toolchain and the iPhoneOS SDK directory. Those
can stay anywhere you want since you have to provide their paths to the
SCons build command.

For the iPhone platform to be detected, you need the ``OSXCROSS_IOS``
environment variable defined to anything.

::

    $ export OSXCROSS_IOS=anything

Now you can compile for iPhone using SCons like the standard Godot
way, with some additional arguments to provide the correct paths:

::

    $ scons -j 4 platform=iphone arch=arm target=release_debug IPHONESDK="/path/to/iPhoneSDK" IPHONEPATH="/path/to/iostoolchain" ios_triple="arm-apple-darwin11-"
    $ scons -j 4 platform=iphone arch=arm64 target=release_debug IPHONESDK="/path/to/iPhoneSDK" IPHONEPATH="/path/to/iostoolchain" ios_triple="arm-apple-darwin11-"

Producing fat binaries
~~~~~~~~~~~~~~~~~~~~~~

Apple requires a fat binary with both architectures (``armv7`` and
``arm64``) in a single file. To do this, use the
``arm-apple-darwin11-lipo`` executable. The following example assumes
you are in the root Godot source directory:

::

    $ /path/to/iostoolchain/usr/bin/arm-apple-darwin11-lipo -create bin/libgodot.iphone.opt.debug.arm.a bin/libgodot.iphone.opt.debug.arm64.a -output bin/libgodot.iphone.debug.fat.a
    $ /path/to/iostoolchain/usr/bin/arm-apple-darwin11-lipo -create bin/libgodot_camera_module.iphone.opt.debug.arm.a bin/libgodot_camera_module.iphone.opt.debug.arm64.a -output bin/libgodot_camera_module.iphone.debug.fat.a
    $ /path/to/iostoolchain/usr/bin/arm-apple-darwin11-lipo -create bin/libgodot_arkit_module.iphone.opt.debug.arm.a bin/libgodot_arkit_module.iphone.opt.debug.arm64.a -output bin/libgodot_arkit_module.iphone.debug.fat.a


Then you will have iOS fat binaries in ``bin`` directory.
