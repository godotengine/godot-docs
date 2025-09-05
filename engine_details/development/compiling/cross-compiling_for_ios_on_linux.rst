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

- `XCode with the iOS SDK <https://developer.apple.com/download/all/?q=Xcode>`__
  (you must be logged into an Apple ID to download Xcode).
- `Clang >= 3.5 <https://clang.llvm.org>`__ for your development
  machine installed and in the ``PATH``. It has to be version >= 3.5
  to target ``arm64`` architecture.
- `xar <https://mackyle.github.io/xar/>`__ and `pbzx <https://github.com/NiklasRosenstein/pbzx>`__
  (required to extract the ``.xip`` archive Xcode comes in).

  - For building xar and pbzx, you may want to follow
    `this guide <https://gist.github.com/phracker/1944ce190e01963c550566b749bd2b54>`__.

- `cctools-port <https://github.com/tpoechtrager/cctools-port>`__
  for the needed build tools. The procedure for building is quite
  peculiar and is described below.

  - This also has some extra dependencies: automake, autogen, libtool.

Configuring the environment
---------------------------

Preparing the SDK
~~~~~~~~~~~~~~~~~

Extract the Xcode ``.xip`` file you downloaded from Apple's developer website:

::

    mkdir xcode
    xar -xf /path/to/Xcode_X.x.xip -C xcode
    pbzx -n Content | cpio -i

    [...]
    ######### Blocks

Note that for the commands below, you will need to replace the version (``x.x``)
with whatever iOS SDK version you're using. If you don't know your iPhone SDK
version, you can see the JSON file inside of
``Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs``.

Extract the iOS SDK:

::

    export IOS_SDK_VERSION="x.x"
    mkdir -p iPhoneSDK/iPhoneOS${IOS_SDK_VERSION}.sdk
    cp -r xcode/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS.sdk/* iPhoneSDK/iPhoneOS${IOS_SDK_VERSION}.sdk
    cp -r xcode/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include/c++/* iPhoneSDK/iPhoneOS${IOS_SDK_VERSION}.sdk/usr/include/c++
    fusermount -u xcode

Pack the SDK so that cctools can use it:

::

    cd iPhoneSDK
    tar -cf - * | xz -9 -c - > iPhoneOS${IOS_SDK_VERSION}.sdk.tar.xz

Toolchain
~~~~~~~~~

Build cctools:

::

    git clone https://github.com/tpoechtrager/cctools-port.git
    cd cctools-port/usage_examples/ios_toolchain
    ./build.sh /path/iPhoneOS${IOS_SDK_VERSION}.sdk.tar.xz arm64

Copy the tools to a nicer place. Note that the SCons scripts for
building will look under ``usr/bin`` inside the directory you provide
for the toolchain binaries, so you must copy to such subdirectory, akin
to the following commands:

::

    mkdir -p "$HOME/iostoolchain/usr"
    cp -r target/bin "$HOME/iostoolchain/usr/"

Now you should have the iOS toolchain binaries in
``$HOME/iostoolchain/usr/bin``.

Compiling Godot for iPhone
--------------------------

Once you've done the above steps, you should keep two things in your
environment: the built toolchain and the iPhoneOS SDK directory. Those
can stay anywhere you want since you have to provide their paths to the
SCons build command.

For the iPhone platform to be detected, you need the ``OSXCROSS_IOS``
environment variable defined to anything.

::

    export OSXCROSS_IOS="anything"

Now you can compile for iPhone using SCons like the standard Godot
way, with some additional arguments to provide the correct paths:

::

    scons platform=ios arch=arm64 target=template_release IOS_SDK_PATH="/path/to/iPhoneSDK" IOS_TOOLCHAIN_PATH="/path/to/iostoolchain" ios_triple="arm-apple-darwin11-"
