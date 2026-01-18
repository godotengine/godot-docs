.. _doc_hdr_output:

HDR output
======================

First steps
-----------

Try out the `HDR output demo project <https://github.com/godotengine/godot-demo-projects/pull/1287>`_ to ensure HDR output is working with your setup. Follow the troubleshooting steps below to resolve any issues you might have.

Enabling HDR output in your project
-----------------------------------

You can enable HDR output in any new or existing project using these steps:

1. Ensure all Environment resources do *not* use SDR-only features:

    - Tonemap Mode: Filmic or ACES
    - Glow Blend Mode: Soft Light
    - Adjustments: Color Correction

2. Configure the :ref:`Rendering Device Driver<class_ProjectSettings_property_rendering/rendering_device/driver>` project setting to the following:

    - macos: metal
    - ios: metal
    - windows: d3d12

3. Turn on the :ref:`HDR 2D<class_ProjectSettings_property_rendering/viewport/hdr_2d>` project setting and also turn on :ref:`use_hdr_2d<class_Viewport_property_use_hdr_2d>` of all :ref:`SubViewports <class_SubViewport>` and :ref:`Windows <class_Window>` that should support HDR output.
4. Turn on the [code]display/window/hdr/request_hdr_output[/code] project setting and also turn on :!ref:`hdr_output_requested<class_Window_property_hdr_output_requested>` of all other :ref:`Windows <class_Window>` that should support HDR output.
5. [Optional] Provide in-game settings for the player to adjust HDR brightness and maximum luminance by copying [code]in_game_hdr_settings[/code] from this demo into your project.

HDR output fundamentals
-----------------------

Godot uses the Extended Dynamic Range (EDR) paradigm for HDR output. (Link to Apple talk that describes it further.) While Standard Dynamic Range (SDR) output allows color component values between 0.0 and 1.0 to be displayed, HDR output allows values higher than 1.0. The maximum value that can be displayed is provided by Window.output_max_linear_value and is valid when using SDR or HDR.

(Image showing [0, infinity] with [0, 1 aka output_max_linear_value for SDR] and [0, ~3 aka output_max_linear_value for HDR]. Maybe four bars, greyscale, red, green, blue in the centre with SDR on the left and HDR on the right.)

Designing for HDR output
------------------------

There are two primary approaches to make the most of HDR output: using Window.output_max_linear_value and using the WorldEnvironment. While both approaches can be used in the same project, the output_max_linear_value should not be used in scenes that are affected by a WorldEnvironment.

Using output_max_linear_value
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In a traditional SDR-only game, the brightest presentation of a color is limited by either the red, green, or blue component of the color reaching a maximum of 1.0. Using modern HDR displays, this limitation no longer applies. Even if you are developing an SDR game, it may be best to use Window.output_max_linear_value to determine the brightest colour component value that a display can present instead of hardcoding a value of 1.0 because this can make it easier to adapt your SDR game to HDR in the future.

The output_max_linear_value may change often as the player adjusts their device brightness, enables or disables HDR output on their device, or moves the game window between SDR or HDR displays, so it’s important to retrieve this value every frame.

It is best to use this output_max_linear_value with “highlights” and special effects that are either brief or involve a small portion of the screen; if the majority of the screen is presented at this maximum brightness for more than a short time, it will cause the game to appear uncomfortably bright, as if the game is ignoring the device brightness setting.

Transforming a colour to be the brightest the display can present can be done with a script such as the following:

(Documentation)

When working with CanvasItems, it may be convenient to apply the result to the self_modulate or modulate property.

Using the Environment resource
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Window.output_max_linear_value should generally not be used with a WorldEnvironment. This is because a number of effects of Environment expect stable scene values that do not change based on the display capabilities. For example, the strength of the glow effect is directly influenced by the brightness of the scene. If the scene brightness changes based on Window.output_max_linear_value, then the glow strength will change in turn: a larger output_max_linear_value will produce a stronger glow effect, which is generally an undesirable behaviour. The Viewport.own_world_3d property can be used to separate which Viewports are affected by which WorldEnvironments.

When using HDR output without the output_max_linear_value, your scenes will need Color values that exceed what an SDR display can produce, so it is important to use a tone mapper like Reinhard or AgX to handle display of bright scene values on both SDR and HDR displays.

**Tonemapping and HDR**

The primary role of a tone mapper is to reduce the dynamic range of a natural scene with a very high dynamic range of brightness into a smaller dynamic range that can be reproduced on a display. For example, with the Reinhard tone mapper in Godot, scene values in the range of 0.0 to the linear value of tonemap_white are mapped to an output range of 0.0 to output_max_linear_value.

(Image of Reinhard mapping range of [0, white] to [0, output_max_linear_value])

With this approach, you can be sure that any linear scene value below tonemap_white will be shown without clipping. This ensures that details are not lost when presenting the image on a display with a lower dynamic range than the original scene.

(Image of Reinhard with bright clouds and a white of 1.0 and a white of 3.0 in SDR)

While this behaviour is perfectly stable in SDR, where output_max_linear_value is fixed at 1.0, this behaviour is dynamic with HDR based on the capabilities of the display. Importantly, when output_max_linear_value has increased to a be higher than white, white will be adjusted to match this output_max_linear_value:

(Image of Reinhard curve with white of 3.0 and output_max_linear_value of 1.0 (SDR), 2.0 (HDR), and 4.0 (HDR))

In the above example, the Reinhard tone mapper will behave the same as the Linear tonemapper when output_max_linear_value is 4.0. This allows for accurate colour reproduction on HDR displays that are capable of reproducing the original brighter scene values.

The AgX tone mapper behaves similarly to Reinhard in this way, but its white is always multiplied by output_max_linear_value. The Linear tonemapper applies no tonemapping at all; its white equals output_max_linear_value in all scenarios. The Filmic and ACES tone mappers ignore output_max_linear_value entirely and always produce an image in the SDR range.

Absolute luminance values
-------------------------

When using HDR output, Window.output_max_linear_value is calculated based on the reference white luminance (the device brightness) and the maximum luminance of the display.

Reference white luminance
^^^^^^^^^^^^^^^^^^^^^^^^^

The reference white luminance, or reference luminance for short, is simply the device brightness. This value is typically around 100 to 300 nits and is always represented by an output_max_linear_value of exactly 1.0. This value may also be referred to as “paper white” and matches the brightest possible SDR white value.

When the user changes their device brightness, they are simply adjusting their reference luminance. On a phone, this adjustment may happen automatically. On desktop computers, there are different ways to adjust this reference luminance depending on the operating system.

**Changing reference white luminance**

HDR brightness is the reference white luminance. It can be changed depending on operating system:

(TODO: instructions for each platform)

Maximum luminance
^^^^^^^^^^^^^^^^^

The maximum luminance is a property of an HDR display. This value may be anywhere from 250 to 2,000 nits or beyond.

Although this value is a property of the display hardware and is expected to not change, some devices dynamically adapt this value to work within the constraints of the platform. For example, the maximum luminance of Windows laptops with built-in HDR displays will change as the user adjusts their laptop display brightness.

output_max_linear_value in practice
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When in HDR mode, the output_max_linear_value will increase as the user decreases their device brightness setting because more HDR headroom becomes available. Similarly, as the user turns up their device brightness, they will have less HDR headroom available and output_max_linear_value will decrease. In some cases when using HDR mode with the highest device brightness, output_max_linear_value will equal 1.0, matching SDR behaviour, because no HDR headroom is available.

(TODO: image)

Not all displays are equal
--------------------------

SDR standards were designed to match the capabilities of existing displays that were commonly used around the world. HDR standards have been intentionally written with the opposite approach: they are designed to utilize the capabilities of an ideal display that is not yet widely available.

In practice, this means that common HDR displays may perform their own internal tone mapping to support content that extends to a wider gamut and luminance range than what the physical hardware can achieve. This tone mapping may produce colours that are not representative of other displays, so it’s best to disable this feature, if possible, when developing your HDR game. You may be able to disable some or all internal tone mapping by enabling the HGiG mode on your display or setting the display’s mode to “clip” and/or “stable”.

Additionally, some HDR displays may render dark or saturated colours differently than others. This difference in appearance may be controlled by the user through a black level adjustment that is built into the display or simply be the result of the screen technology.

Calibrating maximum luminance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

External HDR displays often do not provide accurate maximum luminance values, but instead provide the maximum luminance that can be provided to the internal tone mapper of the display. For this reason, it is important to calibrate your maximum luminance on devices that use an external display and provide in-game settings to users who may not be able to perform this calibration through their operating system.

TODO: how to calibrate on different platforms

Troubleshooting
---------------

When running the HDR output demo project, the following debug information is displayed:

DisplayServer
TODO

RenderingDevice
TODO

Window supports HDR output
If this is false, it likely means that the display that the game window is on does not support HDR output. If this is the case, you may need to enable HDR output for this display through your system settings.

Windows
^^^^^^^

Prerequisites
An HDR-capable display
HDR enabled for this display in your system display settings
For more information, see https://support.microsoft.com/en-us/windows/hdr-settings-in-windows-2d767185-38ec-7fdc-6f97-bbc6c5ef24e6


(TODO: Mac OS, etc.)