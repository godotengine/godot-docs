.. _doc_splash_screen_editing:

How to disable the booting splash screen?
=====

Go to scene>project settings>application>boot_splash

.. img:: /img/boot_splash.png

Uncheck the checkbox Or choose a custom splash screen

.. img:: /img/boot_splash_options.png

Adding more splash screen
-----

Godot is awesome, why not let everyone know about it?

If you want to add one more splash screen after the engine's one, you can create a new scene with the splash screen and set it as the first scene and change to the next scene afterward.

.. img:: /img/splash_main_scene.png

You can do this by creating a scene with a animationplayer node and use the finished() signal for changing the scene, remember to **enable autoplay** in the animationplayer.

::

    #Change scene after splash screen
    extends AnimationPlayer

    func _ready():
	    pass


    func _on_AnimationPlayer_finished():
	    get_tree().change_scene("scene_after_splash")
