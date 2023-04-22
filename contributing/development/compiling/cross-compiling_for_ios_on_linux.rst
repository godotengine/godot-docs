.. _doc_cross-compiling_for_ios_on_linux:

Cross-compiling for iOS on Linux
================================

.. highlight:: shell

The procedure for this is somewhat complex and requires a lot of steps,
but once you have the environment properly configured you can
compile Godot for iOS anytime you want.

Disclaimer
----------

While it is possible to compile for iOS on a Linux environment, Apple is
very restrictive about the tools to be used (especially hardware-wise),
allowing pretty much only their products to be used for development. So
this is **not official**. However, in 2010 Apple said they relaxed some of the
`App Store review guidelines <https://developer.apple.com/app-store/review/guidelines/>`__
to allow any tool to be used, as long as the resulting binary does not
download any code, which means it should be OK to use the procedure
described here and cross-compiling the binary.

Requirements
------------

- `XCode with the iOS SDK <https://developer.apple.com/xcode/download>`__
  (a dmg image, for newer versions a **xip** file is going to be downloaded.)
- `Clang >= 3.5 <https://clang.llvm.org>`__ for your development
  machine installed and in the ``PATH``. It has to be version >= 3.5
  to target ``arm64`` architecture.
- `Fuse <https://github.com/libfuse/libfuse>`__ for mounting and unmounting
  the dmg image.
- `darling-dmg <https://github.com/darlinghq/darling-dmg>`__, which
  needs to be built from source. The procedure for that is explained
  below.

    - For newer versions you should download `xar <https://mackyle.github.io/xar/>`__
      and `pbzx <https://github.com/NiklasRosenstein/pbzx>`__.
    - For building darling-dmg, you'll need the development packages of
      the following libraries: fuse, icu, openssl, zlib, bzip2.
    - For building xar and pbzx you may want to follow
      `this guide <https://gist.github.com/phracker/1944ce190e01963c550566b749bd2b54>`__.

- `cctools-port <https://github.com/tpoechtrager/cctools-port>`__
  for the needed build tools. The procedure for building is quite
  peculiar and is described below.

    - This also has some extra dependencies: automake, autogen, libtool.

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


For newer versions you should extract the **xip** file:

::

    $ mkdir xcode
    $ xar -xf /path/to/Xcode_X.x.xip -C xcode
    $ pbzx -n Content | cpio -i
    [...]
    ######### Blocks

Note that for the commands below, you may need to replace the version (`X.x`) with whatever iOS SDK version you're using.

Extract the iOS SDK:

::

    $ # If you don't know your iPhone SDK version you can see the json file inside of Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs
    $ mkdir -p iPhoneSDK/iPhoneOSX.x.sdk
    $ cp -r xcode/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS.sdk/* iPhoneSDK/iPhoneOSX.x.sdk
    $ cp -r xcode/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include/c++/* iPhoneSDK/iPhoneOSX.x.sdk/usr/include/c++
    $ fusermount -u xcode  # unmount the image

Pack the SDK:

::

    $ cd iPhoneSDK
    $ tar -cf - * | xz -9 -c - > iPhoneOSX.x.sdk.tar.xz

Toolchain
~~~~~~~~~

Build cctools:

::

    $ git clone https://github.com/tpoechtrager/cctools-port.git
    $ cd cctools-port/usage_examples/ios_toolchain
    $ ./build.sh /path/iPhoneOSX.x.sdk.tar.xz arm64

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

    $ scons -j 4 platform=ios arch=arm64 target=template_release IOS_SDK_PATH="/path/to/iPhoneSDK" IOS_TOOLCHAIN_PATH="/path/to/iostoolchain" ios_triple="arm-apple-darwin11-"
