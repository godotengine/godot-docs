.. _doc_environment_and_post_processing:

Environment and Post-Processing
===============================

Godot 3 provides a redesigned Environment node, as well as a brand new post-processing system with many available effects, right out of the box.

Environment
-----------

The Environment resource stores all the information required for controlling rendering environment. This includes sky, ambient lighting, tone mapping, effects and adjustments.
By itself it does nothing, but it becomes enabled once used in one of the following locations, in order of priority:

Camera Node
^^^^^^^^^^^^

An Environment can be set to a camera. It will have priority over any other setting.

.. image:: img/environment_camera.png

This is mostly useful when wanting to override an existing environment, but in general it's a better idea to use the option below.


WorldEnvironment Node
^^^^^^^^^^^^^^^^^^^^^

The WorldEnvironment node can be added to any scene, but only one per active scene tree can exist. Adding more than one will result in a warning.

.. image:: img/environment_world.png

Any Environment set to it more priority than the default Environment (explained below). The fact it's per-scene usually makes it the most pratical.


Default Environment
^^^^^^^^^^^^^^^^^^^^^

A default environment can be set, which acts as a fallback when no Environment was set to a Camera or WorldEnvironment.
Just head to Project Settings -> Rendering -> Environment:

.. image:: img/environment_default.png

Make sure to have an environment saved to disk for this.

Environment Options
-------------------

Following is a detailed description of all environment options and how they are intended to be used.


Background
^^^^^^^^^^

The Background section contains settings on how to fill the view background (anywhere no-rendered in the screen). In Godot 3.0, the background does not only serve the purpose
of showing an image or color, but it can also affect how objects are affected by ambient and reflected light.

.. image:: img/environment_background.png

There are many ways to set the background: 

- **Clear Color** uses the default clear color defined by the project. The background will be a constant color.
- **Custom Color** is like Clear Color, but with a custom color value.
- **Sky** lets you define a panorama sky (a 360 degree sphere texture) or a procedural sky (a simple sky featuring a gradient and an optional sun). Objects will reflect it and absorb ambient light from it.
- **Color+Sky** lets you define a sky (as above), but uses a constant color value for drawing the background. The sky will only be used for reflection and ambient light.


Ambient Light
^^^^^^^^^^^^^

Ambient is a type of light that affects every piece of geometry the same. It is global and independent of lights that might be added to the scene. The only exception is when using GIProbes or Reflection Probes in **Interior** mode, which make objects inside ignore ambient lighting.


There are two types of ambient light, the *Ambient Color* (which is just a constant color multiplied by the material albedo), and then one obtained from the *Sky* (as described before, but a sky needs to be set as background for this to be enabled). 

.. image:: img/environment_ambient.png


Why a *Sky* is set as background, it's possible to blend between color and sky using the **Sky Contribution** setting (this value is 1.0 by default for convenience, so only light ambient affects objects).

Here is a comparison of how different ambient affect a scene:

.. image:: img/environment_ambient2.png

Finally there is a **Energy** setting, which is just a multiplier, useful when working with HDR.

In general, unless doing simple scenes, large exteriors or for performance reasons (ambient light is cheap), using ambient does not provide the best lighting quality. It's better to generate
ambient light from ReflectionProbe or GIProbe, which will more faithfully simulate how indirect light propagates. Below is a comparision in quality between using a flat ambient color and a GIProbe:

.. image:: img/environment_ambient_comparison.png

Fog
^^^

Fog, just as in real life, makes distant objects fade away into an uniform color. The physical effect is actually pretty complex, but Godot provides a good approximation. There are two kinds of fog in Godot:

- **Depth Fog:** This one applies based on the distance from the camera.
- **Height Fog:** This one applies to any objects below (or above) a certain height, regardless of the distance from the camera.

.. image:: img/environment_fog_depth_height.png

Both of these fog types can have their curve tweaked, making their transition more or less sharp.

Two properties can be tweaked to make the fog effect more interesting:

- **Sun Amount** makes use of the Sun Color property of the fog. When looking towards a directional light (usually a sun), the color of the fog will be changed, simulating the sunlight passing through the fog.

An extra option is provided, **Transmit Enabled** wich simulates more realistic light transmittance. In practice, it makes light stand out more across the fog.

.. image:: img/environment_fog_transmission.png

Tonemap
^^^^^^^

Selects the tone-mapping curve that will be applied to the scene, from a short list of standard curves used in the film and game industry. Tone mapping can make light and dark areas more homogeneous, even though the result is slight. Tone mapping options are:

- **Mode:** Tone mapping mode, which can be Linear, Reindhart, Filmic or Aces.
- **Exposure:** Tone mapping exposure, which simulates amount of light received over time.
- **White:** Tone mapping white, which simulates where in the scale is white located (by default 1.0).

Auto Exposure (HDR)
^^^^^^^^^^^^^^^^^^^

Even though, in most cases, lighting and texturing are heavily artist controlled, Godot suports a simple high dynamic range with auto exposure mechanism. This is generally used for the
sake of realism, when combining interior areas with low light and outdoors. Auto expure simulates the camera (or eye) correction of exposure when changing from a scene with considerably
different amount of light.

.. image:: img/environment_hdr_autoexp.gif

The simplest way to use auto exposure is to make sure outdoor lights (or other strong lights) have energy beyond 1.0. This is done by tweaking their **Energy** multiplier (on the Light itself). To
make it consistent, the **Sky** usually needs to use the energy multiplier too, to match the with the directional light. Normally, values between 3.0 and 6.0 are enough to simulate indoor-oudoor conditions.

By combining Auto Exposure with *Glow* post processing (more on that below), pixels that go over the tonemap **White** will bleed to the glow buffer, creating the typical bloom effect in photography.

.. image:: img/environment_hdr_bloom.png

The user-controllable values in the Auto Exposure section come with sensible defaults, but you can still tweak then:

.. image:: img/environment_hdr.png

- **Scale** Value to scale the lighting. Brighter values produce brighter images, smaller ones produce darker ones.
- **Min Luma** Minimum luminance that auto exposure will aim to adjust for. Luminance is the average of the light in all the pixels of the screen.
- **Max Luma** Maximum luminance that auto exposure will aim to adjust for.
- **Speed** Speed at which luminance corrects itself. The higher the value, the faster correction happens.

Mid and Post-Processing Effects
-------------------------------

A large amount of common mid and post-processing effects are supported in Environment.

Screen-Space Reflections (SSR)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

While Godot supports three sources of reflection data (Sky, ReflectionProbe and GIProbe), it sometimes is needed to have even more accurate reflections. Scenarios
where Screen Space Refletions mak the most sense is when objects are in contact (object over floor, over a table, floating on water, etc). 

.. image:: img/environment_ssr.png

The other advantage to using it, even if slightly in a scene, is that it works in real-time (while the other types of reflections are pre-computed). This is great to
make characters, cars, etc. reflect when moving around.

A few user-controlled parameters are available to better tweak the technique:

- **Max Steps** determines the length of the reflection. The bigger this number, the more costly it is to compute.
- **Fade In** allows adjusting the fade-in curve, which is useful to make the contact area softer.
- **Fade Out** allows adjusting the fade-out curve, which is useful to make the place where no more steps exist disappear softly.
- **Depth Tolerance** can be used for scren-space-ray hit tolerance to gaps. The bigger the value, the more gaps will be ignored.
- **Roughness** will apply a screen-space blur to approximate roughness in objects with this material characteristic.

Keep in mind that screen-space-reflections only work for reflecting opaque geometry. Transparent objects can't be reflected.

Screen-Space Ambient Occlusion (SSAO)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In areas where light does not reach directly, illumination happens by indirect (or ambient) light. As mentioned above in the *Ambient Light** section, Godot can simulate this using GIProbe, ReflectionProbe, the Sky or a constant ambient color. The problem, however, is that all the methods proposed before act more on larger scale (large regions) than at the smaller geometry level.

Constant ambient color and Sky are uniform, while GI and Reflection probe have more local detail, but not enough to simulate situations like light not being able to fill inside hollow or concave
geometries.

This can be simulated with Screen Space Ambient Occlusion. As you can see in the image below, the goal of it is to make sure concave areas are darker, simulating less space for the light to enter:

.. image:: img/environment_ssao.png

While still there, the effect is less noticeable under the direct light on the left of the image, just like in reality.

Of course, the effect looks best when combined with a real source of indirect light, like GIProbe:

.. image:: img/environment_ssao2.png

Tweaking SSAO is made possible with several available parameters:

.. image:: img/environment_ssao_parameters.png

- **Radius/Intensity:** To control the radius or intensity of the occlusion, these two parameters are available. Radius is in world (Metric) units.
- **Radius2/Intensity2:** A Secondary radius/intensity can be used. Combining a large and a small radius AO generally works well.
- **Bias:** This can be tweaked to solve self occlusion, though the default generally works well enough.
- **Light Affect:** SSAO only affects ambient light, but increasing this slider can make it also affect direct light. Some artists prefer this effect.
- **Quality:** Depending on quality, SSAO will do more samplings over a sphere for every pixel. High quality only works well on modern GPUs.
- **Blur:** Type of blur kernel used. The 1x1 kernel is a simple blur that preserves local detail better, but is not as efficient (generally works better with high quality setting above), while 3x3 will soften the image better (with a bit of dithering-like effect), but does not preserve local detail as well.
- **Edge Sharpness**: This can be used to preserve the sharpness of edges (avoids areas without AO on creases).

Depth of Field / Far Blur
^^^^^^^^^^^^^^^^^^^^^^^^^

This effect simulates focal distance on high end cameras. It blurs objects behind a given range. 
It has an initial **Distance** with a **Transition** region (in world units):

.. image:: img/environment_dof_far.png

The **Amount** parameter controls the amount of blur. For larger blurs, tweaking the **Quality** may be needed in order to avoid arctifacts.


Depth of Field / Near Blur
^^^^^^^^^^^^^^^^^^^^^^^^^^

This effect simulates focal distance on high end cameras. It blurs objects close to the camera (acts in the opposite direction as far blur).
It has an initial **Distance** with a **Transition** region (in world units):

.. image:: img/environment_dof_near.png

The **Amount** parameter controls the amount of blur. For larger blurs, tweaking the **Quality** may be needed in order to avoid arctifacts.

Combining both blurs to focus the viewer attention on a given object is a very common use case for this feature:

.. image:: img/environment_mixed_blur.png


Glow
^^^^

In photography and film, when light exceeds the medium supported, it generally bleeds outwards to darker regions of the image. This is simulated in Godot with
the glow effect. 

.. image:: img/environment_glow1.png

By default, even if the effect is enabled, it will be very weak or not visible. One of two conditions need to happen for it to actually become visible:

- 1) The light in a pixel surpasses the **HDR Treshold** (where 0 is all light surpasses it, and 1.0 is light over the tonemapper **White** value). Normally this value is expected to be at 1.0, but it can be lowered to allow more light to bleed. There is also an extra parameter, **HDR Scale** that allows scaling (making brighter or darker) the light surpasing the threshold.

.. image:: img/environment_glow_threshold.png

- 2) The Bloom effect has a value set greater than 0. As it increases, it sends the whole screen to the glow processor at higher amounts.

.. image:: img/environment_glow_bloom.png

Both will cause the light to start bleeding out of the brighter areas.

Once glow is visible, it can be controlled with a few extra parameters:

- **Intensity** is an overall scale for the effect, it can be made stronger or weaker (0.0 removes it).
- **Strength** is how strong the gaussian filter kernel is processed. Greater values make the filter saturate and expand outwards. In general changing this is not needed, as the size can be more efficienly adjusted with the **Levels**.

The **Blend Mode** of the effect can also be changed:

- **Additive** is the strongest one, as it just adds the glow effect over the image with no blending involved. In general, it's too strong to be used, but can look good with low intensity Bloom (produces a dream-like effect).
- **Screen** is the default one. It ensures glow never brights more than itself, and works great as an all around.
- **Softlight** is the weakest one, producing only a subtle color disturbance arround the objects. This mode works best on dark scenes.
- **Replace** can be used to blur the whole screen or debug the effect. It just shows the glow effect without the image below.

To change the glow effect size and shape, Godot provides **Levels**. Smaller levels are strong glows that appear around objects, while large levels are hazy glows covering the whole screen:

.. image:: img/environment_glow_layers.png

The real strength of this system, though, is to combine layers to create more interesting glow patterns:

.. image:: img/environment_glow_layers2.png
 
Finally, as the highest layers are created by stretching small blurs, it is possible that some blockyness may be visible in some scenes. Enabling **Bicubic Upscaling* gets rids of the blockyness,
at a minimum performance cost.

.. image:: img/environment_glow_bicubic.png

Adjustments
^^^^^^^^^^^

At the end of processing, Godot offers the possibility to do some image adjustments. 

.. image:: img/environment_adjustments.png

The first one is being able to change the typical Brightness, Contrast and Saturation:

.. image:: img/environment_adjustments_bcs.png

The second is by supplying a color correction gradient. A regular black to white gradient like the following one will produce no effect:

.. image:: img/environment_adjusments_default_gradient.png

But creating custom ones will allow to map each channel to a different color:

.. image:: img/environment_adjusments_custom_gradient.png







