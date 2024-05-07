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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. When adjusting specifications, make sure to only mention hardware that can run the required OS version.
.. For example, the x86 CPU requirement for macOS is set after the MacBook Air 11" (late 2010 model),
.. which can run up to macOS 10.13.

+----------------------+-----------------------------------------------------------------------------------------+
| **CPU**              | - **Windows:** x86_32 CPU with SSE2 instructions, or any x86_64 CPU                     |
|                      |                                                                                         |
|                      |   - *Example: Intel Core 2 Duo E8200, AMD Athlon XE BE-2300*                            |
|                      |                                                                                         |
|                      | - **macOS:** x86_64 or ARM CPU (Apple Silicon)                                          |
|                      |                                                                                         |
|                      |   - *Example: Intel Core 2 Duo SU9400, Apple M1*                                        |
|                      |                                                                                         |
|                      | - **Linux:** x86_32 CPU with SSE2 instructions, x86_64 CPU, ARMv7 or ARMv8 CPU          |
|                      |                                                                                         |
|                      |   - *Example: Intel Core 2 Duo E8200, AMD Athlon XE BE-2300, Raspberry Pi 4*            |
+----------------------+-----------------------------------------------------------------------------------------+
| **GPU**              | - **Forward+ rendering method:** Integrated graphics with full Vulkan 1.0 support       |
|                      |                                                                                         |
|                      |   - *Example: Intel HD Graphics 5500 (Broadwell), AMD Radeon R5 Graphics (Kaveri)*      |
|                      |                                                                                         |
|                      | - **Mobile rendering method:** Integrated graphics with full Vulkan 1.0 support         |
|                      |                                                                                         |
|                      |   - *Example: Intel HD Graphics 5500 (Broadwell), AMD Radeon R5 Graphics (Kaveri)*      |
|                      |                                                                                         |
|                      | - **Compatibility rendering method:** Integrated graphics with full OpenGL 3.3 support  |
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
| **Operating system** | - **Native editor:** Windows 7, macOS 10.13 (Compatibility) or                          |
|                      |   macOS 10.15 (Forward+/Mobile), Linux distribution released after 2016                 |
|                      | - **Web editor:** Firefox 79, Chrome 68, Edge 79, Safari 15.2, Opera 64                 |
+----------------------+-----------------------------------------------------------------------------------------+

.. note::

    Windows 7/8/8.1 are supported on a best-effort basis. These versions are not
    regularly tested and some features may be missing (such as colored
    :ref:`print_rich <class_@GlobalScope_method_print_rich>` console output).
    Support for Windows 7/8/8.1 may be removed in a
    :ref:`future Godot 4.x release <doc_release_policy>`.

    Vulkan drivers for these Windows versions are known to have issues with
    memory leaks. As a result, it's recommended to stick to the Compatibility
    rendering method when running Godot on an Windows version older than 10.

Mobile device (smartphone/tablet) - Minimum
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------------------+-----------------------------------------------------------------------------------------+
| **CPU**              | - **Android:** SoC with any 32-bit or 64-bit ARM or x86 CPU                             |
|                      |                                                                                         |
|                      |    - *Example: Qualcomm Snapdragon 430, Samsung Exynos 5 Octa 5430*                     |
|                      |                                                                                         |
|                      | - **iOS:** *Cannot run the editor*                                                      |
+----------------------+-----------------------------------------------------------------------------------------+
| **GPU**              | - **Forward+ rendering method:** SoC featuring GPU with full Vulkan 1.0 support         |
|                      |                                                                                         |
|                      |   - *Example: Qualcomm Adreno 505, Mali-G71 MP2*                                        |
|                      |                                                                                         |
|                      | - **Mobile rendering method:** SoC featuring GPU with full Vulkan 1.0 support           |
|                      |                                                                                         |
|                      |   - *Example: Qualcomm Adreno 505, Mali-G71 MP2*                                        |
|                      |                                                                                         |
|                      | - **Compatibility rendering method:** SoC featuring GPU with full OpenGL ES 3.0 support |
|                      |                                                                                         |
|                      |   - *Example: Qualcomm Adreno 306, Mali-T628 MP6*                                       |
+----------------------+-----------------------------------------------------------------------------------------+
| **RAM**              | - **Native editor:** 3 GB                                                               |
|                      | - **Web editor:** 6 GB                                                                  |
+----------------------+-----------------------------------------------------------------------------------------+
| **Storage**          | 200 MB (used for the executable, project files and cache).                              |
|                      | Exporting projects requires downloading export templates separately                     |
|                      | (1.3 GB after installation).                                                            |
+----------------------+-----------------------------------------------------------------------------------------+
| **Operating system** | - **Native editor:** Android 6.0 (Compatibility) or Android 9.0 (Forward+/Mobile),      |
|                      |   iOS 11.0                                                                              |
|                      | - **Web editor:** Firefox 79, Chrome 88, Edge 79, Safari 15.2, Opera 64,                |
|                      |   Samsung Internet 15                                                                   |
+----------------------+-----------------------------------------------------------------------------------------+

These are the **recommended** specifications to get a smooth experience with the
Godot editor on a simple 2D or 3D project:

Desktop or laptop PC - Recommended
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------------------+-----------------------------------------------------------------------------------------+
| **CPU**              | - **Windows:** x86_64 CPU with SSE4.2 instructions, with 4 physical cores or more       |
|                      |                                                                                         |
|                      |   - *Example: Intel Core i5-6600K, AMD Ryzen 5 1600*                                    |
|                      |                                                                                         |
|                      | - **macOS:** x86_64 or ARM CPU (Apple Silicon)                                          |
|                      |                                                                                         |
|                      |   - *Example: Intel Core i5-8500, Apple M1*                                             |
|                      |                                                                                         |
|                      | - **Linux:** x86_32 CPU with SSE2 instructions, x86_64 CPU, ARMv7 or ARMv8 CPU          |
|                      |                                                                                         |
|                      |   - *Example: Intel Core i5-6600K, AMD Ryzen 5 1600, Raspberry Pi 5 with overclocking*  |
+----------------------+-----------------------------------------------------------------------------------------+
| **GPU**              | - **Forward+ rendering method:** Dedicated graphics with full Vulkan 1.2 support        |
|                      |                                                                                         |
|                      |   - *Example: NVIDIA GeForce GTX 1050 (Pascal), AMD Radeon RX 460 (GCN 4.0)*            |
|                      |                                                                                         |
|                      | - **Mobile rendering method:** Dedicated graphics with full Vulkan 1.2 support          |
|                      |                                                                                         |
|                      |   - *Example: NVIDIA GeForce GTX 1050 (Pascal), AMD Radeon RX 460 (GCN 4.0)*            |
|                      |                                                                                         |
|                      | - **Compatibility rendering method:** Dedicated graphics with full OpenGL 4.6 support   |
|                      |                                                                                         |
|                      |   - *Example: NVIDIA GeForce GTX 650 (Kepler), AMD Radeon HD 7750 (GCN 1.0)*            |
+----------------------+-----------------------------------------------------------------------------------------+
| **RAM**              | - **Native editor:** 8 GB                                                               |
|                      | - **Web editor:** 12 GB                                                                 |
+----------------------+-----------------------------------------------------------------------------------------+
| **Storage**          | 1.5 GB (used for the executable, project files, all export templates and cache)         |
+----------------------+-----------------------------------------------------------------------------------------+
| **Operating system** | - **Native editor:** Windows 10, macOS 10.15,                                           |
|                      |   Linux distribution released after 2020                                                |
|                      | - **Web editor:** Latest version of Firefox, Chrome, Edge, Safari, Opera                |
+----------------------+-----------------------------------------------------------------------------------------+

Mobile device (smartphone/tablet) - Recommended
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------------------+-----------------------------------------------------------------------------------------+
| **CPU**              | - **Android:** SoC with 64-bit ARM or x86 CPU, with 3 "performance" cores or more       |
|                      |                                                                                         |
|                      |   - *Example: Qualcomm Snapdragon 845, Samsung Exynos 9810*                             |
|                      |                                                                                         |
|                      | - **iOS:** *Cannot run the editor*                                                      |
+----------------------+-----------------------------------------------------------------------------------------+
| **GPU**              | - **Forward+ rendering method:** SoC featuring GPU with full Vulkan 1.2 support         |
|                      |                                                                                         |
|                      |   - *Example: Qualcomm Adreno 630, Mali-G72 MP18*                                       |
|                      |                                                                                         |
|                      | - **Mobile rendering method:** SoC featuring GPU with full Vulkan 1.2 support           |
|                      |                                                                                         |
|                      |   - *Example: Qualcomm Adreno 630, Mali-G72 MP18*                                       |
|                      |                                                                                         |
|                      | - **Compatibility rendering method:** SoC featuring GPU with full OpenGL ES 3.2 support |
|                      |                                                                                         |
|                      |   - *Example: Qualcomm Adreno 630, Mali-G72 MP18*                                       |
+----------------------+-----------------------------------------------------------------------------------------+
| **RAM**              | - **Native editor:** 6 GB                                                               |
|                      | - **Web editor:** 8 GB                                                                  |
+----------------------+-----------------------------------------------------------------------------------------+
| **Storage**          | 1.5 GB (used for the executable, project files, all export templates and cache)         |
+----------------------+-----------------------------------------------------------------------------------------+
| **Operating system** | - **Native editor:** Android 9.0 or iOS 11.0                                            |
|                      | - **Web editor:** Latest version of Firefox, Chrome, Edge, Safari, Opera,               |
|                      |   Samsung Internet                                                                      |
+----------------------+-----------------------------------------------------------------------------------------+

Exported Godot project
----------------------

.. warning::

    The requirements below are a baseline for a **simple** 2D or 3D project,
    with basic scripting and few visual flourishes. CPU, GPU, RAM and
    storage requirements will heavily vary depending on your project's scope,
    its rendering method, viewport resolution and graphics settings chosen.
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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. When adjusting specifications, make sure to only mention hardware that can run the required OS version.
.. For example, the x86 CPU requirement for macOS is set after the MacBook Air 11" (late 2010 model),
.. which can run up to macOS 10.13.

+----------------------+-----------------------------------------------------------------------------------------+
| **CPU**              | - **Windows:** x86_32 CPU with SSE2 instructions, or any x86_64 CPU                     |
|                      |                                                                                         |
|                      |  - *Example: Intel Core 2 Duo E8200, AMD Athlon XE BE-2300*                             |
|                      |                                                                                         |
|                      | - **macOS:** x86_64 or ARM CPU (Apple Silicon)                                          |
|                      |                                                                                         |
|                      |  - *Example: Intel Core 2 Duo SU9400, Apple M1*                                         |
|                      |                                                                                         |
|                      | - **Linux:** x86_32 CPU with SSE2 instructions, x86_64 CPU, ARMv7 or ARMv8 CPU          |
|                      |                                                                                         |
|                      |  - *Example: Intel Core 2 Duo E8200, AMD Athlon XE BE-2300, Raspberry Pi 4*             |
+----------------------+-----------------------------------------------------------------------------------------+
| **GPU**              | - **Forward+ rendering method:** Integrated graphics with full Vulkan 1.0 support       |
|                      |                                                                                         |
|                      |   - *Example: Intel HD Graphics 5500 (Broadwell), AMD Radeon R5 Graphics (Kaveri)*      |
|                      |                                                                                         |
|                      | - **Mobile rendering method:** Integrated graphics with full Vulkan 1.0 support         |
|                      |                                                                                         |
|                      |   - *Example: Intel HD Graphics 5500 (Broadwell), AMD Radeon R5 Graphics (Kaveri)*      |
|                      |                                                                                         |
|                      | - **Compatibility rendering method:** Integrated graphics with full OpenGL 3.3 support  |
|                      |                                                                                         |
|                      |   - *Example: Intel HD Graphics 2500 (Ivy Bridge), AMD Radeon R5 Graphics (Kaveri)*     |
+----------------------+-----------------------------------------------------------------------------------------+
| **RAM**              | - **For native exports:** 2 GB                                                          |
|                      | - **For web exports:** 4 GB                                                             |
+----------------------+-----------------------------------------------------------------------------------------+
| **Storage**          | 150 MB (used for the executable, project files and cache)                               |
+----------------------+-----------------------------------------------------------------------------------------+
| **Operating system** | - **For native exports:** Windows 7, macOS 10.13 (Compatibility) or                     |
|                      |   macOS 10.15 (Forward+/Mobile), Linux distribution released after 2016                 |
|                      | - **For web exports:** Firefox 79, Chrome 68, Edge 79, Safari 15.2, Opera 64            |
+----------------------+-----------------------------------------------------------------------------------------+

.. note::

    Windows 7/8/8.1 are supported on a best-effort basis. These versions are not
    regularly tested and some features may be missing (such as colored
    :ref:`print_rich <class_@GlobalScope_method_print_rich>` console output).
    Support for Windows 7/8/8.1 may be removed in a
    :ref:`future Godot 4.x release <doc_release_policy>`.

    Vulkan drivers for these Windows versions are known to have issues with
    memory leaks. As a result, it's recommended to stick to the Compatibility
    rendering method when running Godot on an Windows version older than 10.

Mobile device (smartphone/tablet) - Minimum
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------------------+-----------------------------------------------------------------------------------------+
| **CPU**              | - **Android:** SoC with any 32-bit or 64-bit ARM or x86 CPU                             |
|                      |                                                                                         |
|                      |   - *Example: Qualcomm Snapdragon 430, Samsung Exynos 5 Octa 5430*                      |
|                      |                                                                                         |
|                      | - **iOS:** SoC with any 64-bit ARM CPU                                                  |
|                      |                                                                                         |
|                      |   - *Example: Apple A7 (iPhone 5S)*                                                     |
+----------------------+-----------------------------------------------------------------------------------------+
| **GPU**              | - **Forward+ rendering method:** SoC featuring GPU with full Vulkan 1.0 support         |
|                      |                                                                                         |
|                      |   - *Example: Qualcomm Adreno 505, Mali-G71 MP2, PowerVR G6430 (iPhone 6S/iPhone SE 1)* |
|                      |                                                                                         |
|                      | - **Mobile rendering method:** SoC featuring GPU with full Vulkan 1.0 support           |
|                      |                                                                                         |
|                      |   - *Example: Qualcomm Adreno 505, Mali-G71 MP2, PowerVR G6430 (iPhone 6S/iPhone SE 1)* |
|                      |                                                                                         |
|                      | - **Compatibility rendering method:** SoC featuring GPU with full OpenGL ES 3.0 support |
|                      |                                                                                         |
|                      |   - *Example: Qualcomm Adreno 306, Mali-T628 MP6, PowerVR G6430 (iPhone 5S)*            |
+----------------------+-----------------------------------------------------------------------------------------+
| **RAM**              | - **For native exports:** 1 GB                                                          |
|                      | - **For web exports:** 2 GB                                                             |
+----------------------+-----------------------------------------------------------------------------------------+
| **Storage**          | 150 MB (used for the executable, project files and cache)                               |
+----------------------+-----------------------------------------------------------------------------------------+
| **Operating system** | - **For native exports:** Android 6.0 (Compatibility) or Android 9.0 (Forward+/Mobile), |
|                      |   iOS 11.0                                                                              |
|                      | - **For web exports:** Firefox 79, Chrome 88, Edge 79, Safari 15.2, Opera 64,           |
|                      |   Samsung Internet 15                                                                   |
+----------------------+-----------------------------------------------------------------------------------------+

These are the **recommended** specifications to get a smooth experience with a
simple 2D or 3D project exported with Godot:

Desktop or laptop PC - Recommended
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------------------+-----------------------------------------------------------------------------------------+
| **CPU**              | - **Windows:** x86_64 CPU with SSE4.2 instructions, with 4 physical cores or more       |
|                      |                                                                                         |
|                      |  - *Example: Intel Core i5-6600K, AMD Ryzen 5 1600*                                     |
|                      |                                                                                         |
|                      | - **macOS:** x86_64 or ARM CPU (Apple Silicon)                                          |
|                      |                                                                                         |
|                      |  - *Example: Intel Core i5-8500, Apple M1*                                              |
|                      |                                                                                         |
|                      | - **Linux:** x86_32 CPU with SSE2 instructions, x86_64 CPU, ARMv7 or ARMv8 CPU          |
|                      |                                                                                         |
|                      |  - *Example: Intel Core i5-6600K, AMD Ryzen 5 1600, Raspberry Pi 5 with overclocking*   |
+----------------------+-----------------------------------------------------------------------------------------+
| **GPU**              | - **Forward+ rendering method:** Dedicated graphics with full Vulkan 1.2 support        |
|                      |                                                                                         |
|                      |   - *Example: NVIDIA GeForce GTX 1050 (Pascal), AMD Radeon RX 460 (GCN 4.0)*            |
|                      |                                                                                         |
|                      | - **Mobile rendering method:** Dedicated graphics with full Vulkan 1.2 support          |
|                      |                                                                                         |
|                      |   - *Example: NVIDIA GeForce GTX 1050 (Pascal), AMD Radeon RX 460 (GCN 4.0)*            |
|                      |                                                                                         |
|                      | - **Compatibility rendering method:** Dedicated graphics with full OpenGL 4.6 support   |
|                      |                                                                                         |
|                      |   - *Example: NVIDIA GeForce GTX 650 (Kepler), AMD Radeon HD 7750 (GCN 1.0)*            |
+----------------------+-----------------------------------------------------------------------------------------+
| **RAM**              | - **For native exports:** 4 GB                                                          |
|                      | - **For web exports:** 8 GB                                                             |
+----------------------+-----------------------------------------------------------------------------------------+
| **Storage**          | 150 MB (used for the executable, project files and cache)                               |
+----------------------+-----------------------------------------------------------------------------------------+
| **Operating system** | - **For native exports:** Windows 10, macOS 10.15,                                      |
|                      |   Linux distribution released after 2020                                                |
|                      | - **For web exports:** Latest version of Firefox, Chrome, Edge, Safari, Opera           |
+----------------------+-----------------------------------------------------------------------------------------+

Mobile device (smartphone/tablet) - Recommended
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------------------+-----------------------------------------------------------------------------------------+
| **CPU**              | - **Android:** SoC with 64-bit ARM or x86 CPU, with 3 "performance" cores or more       |
|                      |                                                                                         |
|                      |   - *Example: Qualcomm Snapdragon 845, Samsung Exynos 9810*                             |
|                      |                                                                                         |
|                      | - **iOS:** SoC with 64-bit ARM CPU                                                      |
|                      |                                                                                         |
|                      |   - *Example: Apple A11 (iPhone XS/XR)*                                                 |
+----------------------+-----------------------------------------------------------------------------------------+
| **GPU**              | - **Forward+ rendering method:** SoC featuring GPU with full Vulkan 1.2 support         |
|                      |                                                                                         |
|                      |   - *Example: Qualcomm Adreno 630, Mali-G72 MP18, Apple G11P (iPhone XR/XS)*            |
|                      |                                                                                         |
|                      | - **Mobile rendering method:** SoC featuring GPU with full Vulkan 1.2 support           |
|                      |                                                                                         |
|                      |   - *Example: Qualcomm Adreno 630, Mali-G72 MP18, Apple G11P (iPhone XR/XS)*            |
|                      |                                                                                         |
|                      | - **Compatibility rendering method:** SoC featuring GPU with full OpenGL ES 3.2 support |
|                      |                                                                                         |
|                      |   - *Example: Qualcomm Adreno 630, Mali-G72 MP18, Apple G11P (iPhone XR/XS)*            |
+----------------------+-----------------------------------------------------------------------------------------+
| **RAM**              | - **For native exports:** 2 GB                                                          |
|                      | - **For web exports:** 4 GB                                                             |
+----------------------+-----------------------------------------------------------------------------------------+
| **Storage**          | 150 MB (used for the executable, project files and cache)                               |
+----------------------+-----------------------------------------------------------------------------------------+
| **Operating system** | - **For native exports:** Android 9.0 or iOS 11.0                                       |
|                      | - **For web exports:** Latest version of Firefox, Chrome, Edge, Safari, Opera,          |
|                      |   Samsung Internet                                                                      |
+----------------------+-----------------------------------------------------------------------------------------+

.. note::

    Godot doesn't use OpenGL/OpenGL ES extensions introduced after OpenGL
    3.3/OpenGL ES 3.0, but GPUs supporting newer OpenGL/OpenGL ES versions
    generally have fewer driver issues.
