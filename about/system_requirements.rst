:allow_comments: False

.. _doc_system_requirements:

System requirements
===================

This page contains system requirements for the editor and exported projects.
These specifications are given for informative purposes only, but they can be
referred to if you're looking to build or upgrade a system to use Godot on.

Godot editor
------------

These are the **minimum** specifications required to run the Godot editor and work
on a simple 2D or 3D project:

Desktop or laptop PC - Minimum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. When adjusting specifications, make sure to only mention hardware that can run the required OS version.
.. For example, the x86 CPU requirement for macOS is set after the MacBook Air 11" (late 2010 model),
.. which can run up to macOS 10.13.

+----------------------+-----------------------------------------------------------------------------------------+
| **CPU**              | - **Windows:** x86_32 CPU with SSE2 support, x86_64 CPU with SSE4.2 support, ARMv8 CPU  |
|                      |                                                                                         |
|                      |   - *Example: Intel Core 2 Duo E8200, AMD FX-4100, Snapdragon X Elite*                  |
|                      |                                                                                         |
|                      | - **macOS:** x86_64 or ARM CPU (Apple Silicon)                                          |
|                      |                                                                                         |
|                      |   - *Example: Intel Core 2 Duo SU9400, Apple M1*                                        |
|                      |                                                                                         |
|                      | - **Linux:** x86_32 CPU with SSE2 support, x86_64 CPU with SSE4.2 support, ARMv7 or     |
|                      |   ARMv8 CPU                                                                             |
|                      |                                                                                         |
|                      |   - *Example: Intel Core 2 Duo E8200, AMD FX-4100, Raspberry Pi 4*                      |
+----------------------+-----------------------------------------------------------------------------------------+
| **GPU**              | - **Forward+ renderer:** Integrated graphics with full Vulkan 1.0 support               |
|                      |                                                                                         |
|                      |   - *Example: Intel HD Graphics 510 (Skylake), AMD Radeon R5 Graphics (Kaveri)*         |
|                      |                                                                                         |
|                      | - **Mobile renderer:** Integrated graphics with full Vulkan 1.0 support                 |
|                      |                                                                                         |
|                      |   - *Example: Intel HD Graphics 510 (Skylake), AMD Radeon R5 Graphics (Kaveri)*         |
|                      |                                                                                         |
|                      | - **Compatibility renderer:** Integrated graphics with full OpenGL 3.3 support          |
|                      |                                                                                         |
|                      |   - *Example: Intel HD Graphics 2500 (Ivy Bridge), AMD Radeon R5 Graphics (Kaveri)*     |
+----------------------+-----------------------------------------------------------------------------------------+
| **RAM**              | - **Native editor:** 4 GB                                                               |
|                      | - **Web editor:** 8 GB                                                                  |
+----------------------+-----------------------------------------------------------------------------------------+
| **Storage**          | 200 MB (used for the executable, project files and cache).                              |
|                      | Exporting projects requires downloading export templates separately                     |
|                      | (1.3 GB after installation).                                                            |
+----------------------+-----------------------------------------------------------------------------------------+
| **Operating system** | - **Native editor:** Windows 10, macOS 10.13 (Compatibility) or                         |
|                      |   macOS 10.15 (Forward+/Mobile), Linux distribution released after 2018                 |
|                      | - **Web editor:** Recent versions of mainstream browsers: Firefox and derivatives       |
|                      |   (including ESR), Chrome and Chromium derivatives, Safari and WebKit derivatives.      |
+----------------------+-----------------------------------------------------------------------------------------+

.. note::

    If your x86_64 CPU does not support SSE4.2, you can still run the 32-bit Godot
    executable which only has a SSE2 requirement (all x86_64 CPUs support SSE2).

    While supported on Linux, we have no official minimum requirements for running on
    rv64 (RISC-V), ppc64 & ppc32 (PowerPC), and loongarch64. In addition you must
    compile the editor for that platform (as well as export templates) yourself,
    no official downloads are currently provided. RISC-V compiling instructions can
    be found on the :ref:`doc_compiling_for_linuxbsd` page.

Mobile device (smartphone/tablet) - Minimum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------+-----------------------------------------------------------------------------------------+
| **CPU**              | - **Android:** SoC with any 32-bit or 64-bit ARM or x86 CPU                             |
|                      |                                                                                         |
|                      |   - *Example: Qualcomm Snapdragon 430, Samsung Exynos 5 Octa 5430*                      |
|                      |                                                                                         |
|                      | - **iOS:** *Cannot run the editor*                                                      |
+----------------------+-----------------------------------------------------------------------------------------+
| **GPU**              | - **Forward+ renderer:** SoC featuring GPU with full Vulkan 1.0 support                 |
|                      |                                                                                         |
|                      |   - *Example: Qualcomm Adreno 505, Mali-G71 MP2*                                        |
|                      |                                                                                         |
|                      | - **Mobile renderer:** SoC featuring GPU with full Vulkan 1.0 support                   |
|                      |                                                                                         |
|                      |   - *Example: Qualcomm Adreno 505, Mali-G71 MP2*                                        |
|                      |                                                                                         |
|                      | - **Compatibility renderer:** SoC featuring GPU with full OpenGL ES 3.0 support         |
|                      |                                                                                         |
|                      |   - *Example: Qualcomm Adreno 306, Mali-T628 MP6*                                       |
+----------------------+-----------------------------------------------------------------------------------------+
| **RAM**              | - **Native editor:** 3 GB                                                               |
|                      | - **Web editor:** 6 GB                                                                  |
+----------------------+-----------------------------------------------------------------------------------------+
| **Storage**          | 200 MB (used for the executable, project files and cache)                               |
|                      | Exporting projects requires downloading export templates separately                     |
|                      | (1.3 GB after installation)                                                             |
+----------------------+-----------------------------------------------------------------------------------------+
| **Operating system** | - **Native editor:** Android 6.0 (Compatibility) or Android 9.0 (Forward+/Mobile)       |
|                      | - **Web editor:** Recent versions of mainstream browsers: Firefox and derivatives       |
|                      |   (including ESR), Chrome and Chromium derivatives, Safari and WebKit derivatives.      |
+----------------------+-----------------------------------------------------------------------------------------+

These are the **recommended** specifications to get a smooth experience with the
Godot editor on a simple 2D or 3D project:

Desktop or laptop PC - Recommended
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------+---------------------------------------------------------------------------------------------+
| **CPU**              | - **Windows:** x86_64 CPU with SSE4.2 support, with 4 physical cores or more, ARMv8 CPU     |
|                      |                                                                                             |
|                      |   - *Example: Intel Core i5-6600K, AMD Ryzen 5 1600, Snapdragon X Elite*                    |
|                      |                                                                                             |
|                      | - **macOS:** x86_64 or ARM CPU (Apple Silicon)                                              |
|                      |                                                                                             |
|                      |   - *Example: Intel Core i5-8500, Apple M1*                                                 |
|                      |                                                                                             |
|                      | - **Linux:** x86_64 CPU with SSE4.2 support, ARMv7 or ARMv8 CPU                             |
|                      |                                                                                             |
|                      |   - *Example: Intel Core i5-6600K, AMD Ryzen 5 1600, Raspberry Pi 5 with overclocking*      |
+----------------------+---------------------------------------------------------------------------------------------+
| **GPU**              | - **Forward+ renderer:** Dedicated graphics with full Vulkan 1.2 support                    |
|                      |                                                                                             |
|                      |   - *Example: NVIDIA GeForce GTX 1050 (Pascal), AMD Radeon RX 460 (GCN 4.0)*                |
|                      |                                                                                             |
|                      | - **Mobile renderer:** Dedicated graphics with full Vulkan 1.2 support                      |
|                      |                                                                                             |
|                      |   - *Example: NVIDIA GeForce GTX 1050 (Pascal), AMD Radeon RX 460 (GCN 4.0)*                |
|                      |                                                                                             |
|                      | - **Compatibility renderer:** Dedicated graphics with full OpenGL 4.6 support               |
|                      |                                                                                             |
|                      |   - *Example: NVIDIA GeForce GTX 650 (Kepler), AMD Radeon HD 7750 (GCN 1.0)*                |
+----------------------+---------------------------------------------------------------------------------------------+
| **RAM**              | - **Native editor:** 8 GB                                                                   |
|                      | - **Web editor:** 12 GB                                                                     |
+----------------------+---------------------------------------------------------------------------------------------+
| **Storage**          | 1.5 GB (used for the executable, project files, all export templates and cache)             |
+----------------------+---------------------------------------------------------------------------------------------+
| **Operating system** | - **Native editor:** Windows 10, macOS 10.15,                                               |
|                      |   Linux distribution released after 2020                                                    |
|                      | - **Web editor:** Latest version of Firefox, Chrome, Edge, Safari, Opera                    |
+----------------------+---------------------------------------------------------------------------------------------+

Mobile device (smartphone/tablet) - Recommended
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------+-----------------------------------------------------------------------------------------+
| **CPU**              | - **Android:** SoC with 64-bit ARM or x86 CPU, with 3 "performance" cores or more       |
|                      |                                                                                         |
|                      |   - *Example: Qualcomm Snapdragon 845, Samsung Exynos 9810*                             |
|                      |                                                                                         |
|                      | - **iOS:** *Cannot run the editor*                                                      |
+----------------------+-----------------------------------------------------------------------------------------+
| **GPU**              | - **Forward+ renderer:** SoC featuring GPU with full Vulkan 1.2 support                 |
|                      |                                                                                         |
|                      |   - *Example: Qualcomm Adreno 630, Mali-G72 MP18*                                       |
|                      |                                                                                         |
|                      | - **Mobile renderer:** SoC featuring GPU with full Vulkan 1.2 support                   |
|                      |                                                                                         |
|                      |   - *Example: Qualcomm Adreno 630, Mali-G72 MP18*                                       |
|                      |                                                                                         |
|                      | - **Compatibility renderer:** SoC featuring GPU with full OpenGL ES 3.2 support         |
|                      |                                                                                         |
|                      |   - *Example: Qualcomm Adreno 630, Mali-G72 MP18*                                       |
+----------------------+-----------------------------------------------------------------------------------------+
| **RAM**              | - **Native editor:** 6 GB                                                               |
|                      | - **Web editor:** 8 GB                                                                  |
+----------------------+-----------------------------------------------------------------------------------------+
| **Storage**          | 1.5 GB (used for the executable, project files, all export templates and cache)         |
+----------------------+-----------------------------------------------------------------------------------------+
| **Operating system** | - **Native editor:** Android 9.0                                                        |
|                      | - **Web editor:** Latest version of Firefox, Chrome, Edge, Safari, Opera,               |
|                      |   Samsung Internet                                                                      |
+----------------------+-----------------------------------------------------------------------------------------+

Exported Godot project
----------------------

.. warning::

    The requirements below are a baseline for a **simple** 2D or 3D project,
    with basic scripting and few visual flourishes. CPU, GPU, RAM and
    storage requirements will heavily vary depending on your project's scope,
    its renderer, viewport resolution and graphics settings chosen.
    Other programs running on the system while the project is running
    will also compete for resources, including RAM and video RAM.

    It is strongly recommended to do your own testing on low-end hardware to
    make sure your project runs at the desired speed. To provide scalability for
    low-end hardware, you will also need to introduce a
    `graphics options menu <https://github.com/godotengine/godot-demo-projects/tree/master/3d/graphics_settings>`__
    to your project.

These are the **minimum** specifications required to run a simple 2D or 3D
project exported with Godot:

Desktop or laptop PC - Minimum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. When adjusting specifications, make sure to only mention hardware that can run the required OS version.
.. For example, the x86 CPU requirement for macOS is set after the MacBook Air 11" (late 2010 model),
.. which can run up to macOS 10.13.

+----------------------+-----------------------------------------------------------------------------------------+
| **CPU**              | - **Windows:** x86_32 CPU with SSE2 support, x86_64 CPU with SSE4.2 support,            |
|                      |   ARMv8 CPU                                                                             |
|                      |                                                                                         |
|                      |   - *Example: Intel Core 2 Duo E8200, AMD FX-4100, Snapdragon X Elite*                  |
|                      |                                                                                         |
|                      | - **macOS:** x86_64 or ARM CPU (Apple Silicon)                                          |
|                      |                                                                                         |
|                      |   - *Example: Intel Core 2 Duo SU9400, Apple M1*                                        |
|                      |                                                                                         |
|                      | - **Linux:** x86_32 CPU with SSE2 support, x86_64 CPU with SSE4.2 support,              |
|                      |   ARMv7 or ARMv8 CPU                                                                    |
|                      |                                                                                         |
|                      |   - *Example: Intel Core 2 Duo E8200, AMD FX-4100, Raspberry Pi 4*                      |
+----------------------+-----------------------------------------------------------------------------------------+
| **GPU**              | - **Forward+ renderer:** Integrated graphics with full Vulkan 1.0 support,              |
|                      |   Metal 3 support (macOS) or Direct3D 12 (12_0 feature level) support (Windows)         |
|                      |                                                                                         |
|                      |   - *Example: Intel HD Graphics 510 (Skylake), AMD Radeon R5 Graphics (Kaveri)*         |
|                      |                                                                                         |
|                      | - **Mobile renderer:** Integrated graphics with full Vulkan 1.0 support,                |
|                      |   Metal 3 support (macOS) or Direct3D 12 (12_0 feature level) support (Windows)         |
|                      |                                                                                         |
|                      |   - *Example: Intel HD Graphics 510 (Skylake), AMD Radeon R5 Graphics (Kaveri)*         |
|                      |                                                                                         |
|                      | - **Compatibility renderer:** Integrated graphics with full OpenGL 3.3 support          |
|                      |   or Direct3D 11 support (Windows).                                                     |
|                      |                                                                                         |
|                      |   - *Example: Intel HD Graphics 2500 (Ivy Bridge), AMD Radeon R5 Graphics (Kaveri)*     |
+----------------------+-----------------------------------------------------------------------------------------+
| **RAM**              | - **For native exports:** 2 GB                                                          |
|                      | - **For web exports:** 4 GB                                                             |
+----------------------+-----------------------------------------------------------------------------------------+
| **Storage**          | 150 MB (used for the executable, project files and cache)                               |
+----------------------+-----------------------------------------------------------------------------------------+
| **Operating system** | - **For native exports:** Windows 10, macOS 10.13 (Compatibility), macOS 10.15          |
|                      |   (Forward+/Mobile, Vulkan), macOS 13.0 (Forward+/Mobile, Metal), Linux distribution    |
|                      |   released after 2018                                                                   |
|                      | - **Web editor:** Recent versions of mainstream browsers: Firefox and derivatives       |
|                      |   (including ESR), Chrome and Chromium derivatives, Safari and WebKit derivatives.      |
+----------------------+-----------------------------------------------------------------------------------------+

Mobile device (smartphone/tablet) - Minimum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------+-----------------------------------------------------------------------------------------+
| **CPU**              | - **Android:** SoC with any 32-bit or 64-bit ARM or x86 CPU                             |
|                      |                                                                                         |
|                      |   - *Example: Qualcomm Snapdragon 430, Samsung Exynos 5 Octa 5430*                      |
|                      |                                                                                         |
|                      | - **iOS:** SoC with any 64-bit ARM CPU                                                  |
|                      |                                                                                         |
|                      |   - *Example: Apple A7 (iPhone 5S)*                                                     |
+----------------------+-----------------------------------------------------------------------------------------+
| **GPU**              | - **Forward+ renderer:** SoC featuring GPU with full Vulkan 1.0 support, or             |
|                      |   Metal 3 support (iOS/iPadOS)                                                          |
|                      |                                                                                         |
|                      |   - *Example (Vulkan): Qualcomm Adreno 505, Mali-G71 MP2, Apple A12 (iPhone XR/XS)*     |
|                      |   - *Example (Metal): Apple A11 (iPhone 8/X)*                                           |
|                      |                                                                                         |
|                      | - **Mobile renderer:** SoC featuring GPU with full Vulkan 1.0 support, or               |
|                      |   Metal 3 support (iOS/iPadOS)                                                          |
|                      |                                                                                         |
|                      |   - *Example (Vulkan): Qualcomm Adreno 505, Mali-G71 MP2, Apple A12 (iPhone XR/XS)*     |
|                      |   - *Example (Metal): Apple A11 (iPhone 8/X)*                                           |
|                      |                                                                                         |
|                      | - **Compatibility renderer:** SoC featuring GPU with full OpenGL ES 3.0 support         |
|                      |                                                                                         |
|                      |   - *Example: Qualcomm Adreno 306, Mali-T628 MP6, Apple A7 (iPhone 5S)*                 |
+----------------------+-----------------------------------------------------------------------------------------+
| **RAM**              | - **For native exports:** 1 GB                                                          |
|                      | - **For web exports:** 2 GB                                                             |
+----------------------+-----------------------------------------------------------------------------------------+
| **Storage**          | 150 MB (used for the executable, project files and cache)                               |
+----------------------+-----------------------------------------------------------------------------------------+
| **Operating system** | - **For native exports:** Android 6.0 (Compatibility), Android 9.0 (Forward+/Mobile),   |
|                      |   iOS 12.0 (Forward+/Mobile, Vulkan), iOS 16.0 (Forward+/Mobile, Metal)                 |
|                      | - **Web editor:** Recent versions of mainstream browsers: Firefox and derivatives       |
|                      |   (including ESR), Chrome and Chromium derivatives, Safari and WebKit derivatives.      |
+----------------------+-----------------------------------------------------------------------------------------+

These are the **recommended** specifications to get a smooth experience with a
simple 2D or 3D project exported with Godot:

Desktop or laptop PC - Recommended
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------+----------------------------------------------------------------------------------------------+
| **CPU**              | - **Windows:** x86_64 CPU with SSE4.2 support, with 4 physical cores or more, ARMv8 CPU      |
|                      |                                                                                              |
|                      |   - *Example: Intel Core i5-6600K, AMD Ryzen 5 1600, Snapdragon X Elite*                     |
|                      |                                                                                              |
|                      | - **macOS:** x86_64 or ARM CPU (Apple Silicon)                                               |
|                      |                                                                                              |
|                      |   - *Example: Intel Core i5-8500, Apple M1*                                                  |
|                      |                                                                                              |
|                      | - **Linux:** x86_64 CPU with SSE4.2 support, with 4 physical cores or more,                  |
|                      |   ARMv7 or ARMv8 CPU                                                                         |
|                      |                                                                                              |
|                      |   - *Example: Intel Core i5-6600K, AMD Ryzen 5 1600, Raspberry Pi 5 with overclocking*       |
+----------------------+----------------------------------------------------------------------------------------------+
| **GPU**              | - **Forward+ renderer:** Dedicated graphics with full Vulkan 1.2 support,                    |
|                      |   Metal 3 support (macOS), or Direct3D 12 (12_0 feature level) support (Windows)             |
|                      |                                                                                              |
|                      |   - *Example: NVIDIA GeForce GTX 1050 (Pascal), AMD Radeon RX 460 (GCN 4.0)*                 |
|                      |                                                                                              |
|                      | - **Mobile renderer:** Dedicated graphics with full Vulkan 1.2 support,                      |
|                      |   Metal 3 support (macOS), or Direct3D 12 (12_0 feature level) support (Windows)             |
|                      |                                                                                              |
|                      |   - *Example: NVIDIA GeForce GTX 1050 (Pascal), AMD Radeon RX 460 (GCN 4.0)*                 |
|                      |                                                                                              |
|                      | - **Compatibility renderer:** Dedicated graphics with full OpenGL 4.6 support                |
|                      |                                                                                              |
|                      |   - *Example: NVIDIA GeForce GTX 650 (Kepler), AMD Radeon HD 7750 (GCN 1.0)*                 |
+----------------------+----------------------------------------------------------------------------------------------+
| **RAM**              | - **For native exports:** 4 GB                                                               |
|                      | - **For web exports:** 8 GB                                                                  |
+----------------------+----------------------------------------------------------------------------------------------+
| **Storage**          | 150 MB (used for the executable, project files and cache)                                    |
+----------------------+----------------------------------------------------------------------------------------------+
| **Operating system** | - **For native exports:** Windows 10, macOS 10.15 (Forward+/Mobile, Vulkan), macOS 13.0      |
|                      |   (Forward+/Mobile, Metal), Linux distribution released after 2020                           |
|                      | - **For web exports:** Latest version of Firefox, Chrome, Edge, Safari, Opera                |
+----------------------+----------------------------------------------------------------------------------------------+

Mobile device (smartphone/tablet) - Recommended
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------+-----------------------------------------------------------------------------------------+
| **CPU**              | - **Android:** SoC with 64-bit ARM or x86 CPU, with 3 "performance" cores or more       |
|                      |                                                                                         |
|                      |   - *Example: Qualcomm Snapdragon 845, Samsung Exynos 9810*                             |
|                      |                                                                                         |
|                      | - **iOS:** SoC with 64-bit ARM CPU                                                      |
|                      |                                                                                         |
|                      |   - *Example: Apple A14 (iPhone 12)*                                                    |
+----------------------+-----------------------------------------------------------------------------------------+
| **GPU**              | - **Forward+ renderer:** SoC featuring GPU with full Vulkan 1.2 support, or             |
|                      |   Metal 3 support (iOS/iPadOS)                                                          |
|                      |                                                                                         |
|                      |   - *Example: Qualcomm Adreno 630, Mali-G72 MP18, Apple A14 (iPhone 12)*                |
|                      |                                                                                         |
|                      | - **Mobile renderer:** SoC featuring GPU with full Vulkan 1.2 support, or               |
|                      |   Metal 3 support (iOS/iPadOS)                                                          |
|                      |                                                                                         |
|                      |   - *Example: Qualcomm Adreno 630, Mali-G72 MP18, Apple A14 (iPhone 12)*                |
|                      |                                                                                         |
|                      | - **Compatibility renderer:** SoC featuring GPU with full OpenGL ES 3.2 support         |
|                      |                                                                                         |
|                      |   - *Example: Qualcomm Adreno 630, Mali-G72 MP18, Apple A14 (iPhone 12)*                |
+----------------------+-----------------------------------------------------------------------------------------+
| **RAM**              | - **For native exports:** 2 GB                                                          |
|                      | - **For web exports:** 4 GB                                                             |
+----------------------+-----------------------------------------------------------------------------------------+
| **Storage**          | 150 MB (used for the executable, project files and cache)                               |
+----------------------+-----------------------------------------------------------------------------------------+
| **Operating system** | - **For native exports:** Android 9.0, iOS 14.1 (Forward+/Mobile, Vulkan), iOS 16.0     |
|                      |   (Forward+/Mobile, Metal)                                                              |
|                      | - **For web exports:** Latest version of Firefox, Chrome, Edge, Safari, Opera,          |
|                      |   Samsung Internet                                                                      |
+----------------------+-----------------------------------------------------------------------------------------+

.. note::

    Godot doesn't use OpenGL/OpenGL ES extensions introduced after OpenGL
    3.3/OpenGL ES 3.0, but GPUs supporting newer OpenGL/OpenGL ES versions
    generally have fewer driver issues.
