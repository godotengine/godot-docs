.. _doc_signals:

Signals
=======

Introduction
------------

Signals are Godot's version of the *observer* pattern. They allow a node to
send out a message that other nodes can listen for and respond to. For example,
rather than continuously checking a button to see if it's being pressed, the
button can emit a signal when it's pressed.

.. note:: You can read more about the observer pattern here: http://gameprogrammingpatterns.com/observer.html

Signals are a way to *decouple* your game objects, which leads to better organized
and more manageable code. Instead of forcing game objects to expect other objects
to always be present, they can instead emit signals that any interested objects can
subscribe to and respond.

Below you can see some examples of how you can use signals in your own projects.

Timer example
-------------

To see how signals work, let's try using a :ref:`Timer <class_Timer>` node. Create
a new scene with a Node and two children: a Timer and a :ref:`Sprite <class_Sprite>`.
You can use the Godot icon for the Sprite's texture, or any other image you
like. Attach a script to the root node, but don't add any code to it yet.

Your scene tree should look like this:

.. image:: img/signals_node_setup.png

In the Timer node's properties, check the "On" box next to *Autostart*. This will
cause the timer to start automatically when you run the scene. You can leave the
*Wait Time* at 1 second.

Next to the "Inspector" tab is a tab labeled "Node". Click on this tab and you'll
see all of the signals that the selected node can emit. In the case of the Timer
node, the one we're concerned with is "timeout". This signal is emitted whenever
the Timer reaches ``0``.

.. image:: img/signals_node_tab_timer.png

Click on the "timeout()" signal and click "Connect...". You'll see the following
window, where you can define how you want to connect the signal:

.. image:: img/signals_connect_dialog_timer.png

On the left side, you'll see the nodes in your scene and can select the node that
you want to "listen" for the signal. Note that the Timer node is red - this is
*not* an error, but is a visual indication that it's the node that is emitting
the signal. Select the root node.

.. warning:: The target node *must* have a script attached or you'll receive
             an error message.

On the bottom of the window is a field labeled "Method In Node". This is the name
of the function in the target node's script that you want to use. By default,
Godot will create this function using the naming convention ``_on_<node_name>_<signal_name>``
but you can change it if you wish.

Click "Connect" and you'll see that the function has been created in the script:

.. tabs::
 .. code-tab:: gdscript GDScript

    extends Node

    func _on_Timer_timeout():
        pass # replace with function body

 .. code-tab:: csharp

    public class TimerExample : Node
    {
        private void _on_Timer_timeout()
        {
            // Replace with function body.
        }
    }

Now we can replace the placeholder code with whatever code we want to run when
the signal is received. Let's make the Sprite blink:

.. tabs::
 .. code-tab:: gdscript GDScript

    extends Node

    func _on_Timer_timeout():
        $Sprite.visible = !$Sprite.visible

 .. code-tab:: csharp

    public class TimerExample : Node
    {
        public void _on_Timer_timeout()
        {
            var sprite = (Sprite) GetNode("Sprite");
            sprite.Visible = !sprite.Visible;
        }
    }

Run the scene and you'll see the Sprite blinking on and off every second. You can
change the Timer's *Wait Time* property to alter this.

Connecting signals in code
~~~~~~~~~~~~~~~~~~~~~~~~~~

You can also make the signal connection in code rather than with the editor. This
is usually necessary when you're instancing nodes via code and so you can't use
the editor to make the connection.

First, disconnect the signal by selecting the connection in the Timer's "Node"
tab and clicking disconnect.

.. image:: img/signals_disconnect_timer.png

To make the connection in code, we can use the ``connect`` function. We'll put it
in ``_ready()`` so that the connection will be made on run. The syntax of the
function is ``<source_node>.connect(<signal_name>, <target_node>, <target_function_name>)``.
Here is the code for our Timer connection:

.. tabs::
 .. code-tab:: gdscript GDScript

    extends Node

    func _ready():
        $Timer.connect("timeout", self, "_on_Timer_timeout")

    func _on_Timer_timeout():
        $Sprite.visible = !$Sprite.visible

 .. code-tab:: csharp

    public class TimerExample : Node
    {
        public override void _Ready()
        {
            var timer = (Timer) GetNode("Timer");
            timer.Connect("timeout", this, nameof(_on_Timer_timeout));
        }

        public void _on_Timer_timeout()
        {
            var sprite = (Sprite) GetNode("Sprite");
            sprite.Visible = !sprite.Visible;
        }
    }

Custom signals
--------------

You can also declare your own custom signals in Godot:


.. tabs::
 .. code-tab:: gdscript GDScript

    extends Node

    signal my_signal

 .. code-tab:: csharp

    public class Main : Node
    {
        [Signal]
        public delegate void MySignal();
    }

Once declared, your custom signals will appear in the Inspector and can be connected
in the same way as a node's built-in signals.

To emit a signal via code, use the ``emit`` function:

.. tabs::
 .. code-tab:: gdscript GDScript

    extends Node

    signal my_signal

    func _ready():
        emit("my_signal")

 .. code-tab:: csharp

    public class Main : Node
    {
        [Signal]
        public delegate void MySignal();

        public override void _Ready()
        {
            EmitSignal(nameof(MySignal));
        }
    }

Shooting example
----------------

As another example of signal usage, let's consider a player character that can
rotate and shoot towards the mouse. Every time the mouse button is clicked,
we create an instance of the bullet at the player's location. See :ref:`doc_instancing`
for details.

However, if the bullets are added as children of the player, then they will
remain "attached" to the player as it rotates:

.. image:: img/signals_shoot1.gif

Instead, we need the bullets to be independent of the player's movement - once
fired, they should continue traveling in a straight line and the player can no
longer affect them. Instead of being added to the scne tree as a child of the
player, it makes more sense to add the bullet as a child of the "main" game
scene, which may be the player's parent or even further up the tree.

You could do this by adding the bullet directly:

.. tabs::
 .. code-tab:: gdscript GDScript

    var bullet_instance = Bullet.instance()
    get_parent().add_child(bullet_instance)

 .. code-tab:: csharp

    var bulletInstance = (Sprite) Bullet.Instance();
    GetParent().AddChild(bulletInstance);

However, this will lead to a different problem. Now if you try and test your
"Player" scene independently, it will crash on shooting, because there is no
parent node to access. This makes it a lot harder to test your player code
independently and also means that if you decide to change your main scene's
node structure, the player's parent may no longer be the appropriate node to
receive the bullets.

The solution to this is to use a signal to "emit" the bullets from the player.
The player then has no need to "know" what happens to the bullets after that -
whatever node is connected to the signal can "receive" the bullets and take the
appropriate action to spawn them.


Here is the code for the player using signals to emit the bullet:

.. tabs::
 .. code-tab:: gdscript GDScript

    extends Sprite

    signal shoot(bullet, direction, location)

    var Bullet = preload("res://Bullet.tscn")

    func _input(event):
        if event is InputEventMouseButton:
            if event.button_index == BUTTON_LEFT and event.pressed:
                emit_signal("shoot", Bullet, rotation, position)

    func _process(delta):
        look_at(get_global_mouse_position())

 .. code-tab:: csharp

    public class Player : Sprite
    {
        [Signal]
        delegate void Shoot(PackedScene bullet, Vector2 direction, Vector2 location);

        var Bullet = (PackedScene) ResourceLoader.Load("res://Bullet.tscn");

        public override void _Input(InputEvent event)
        {
            if (input is InputEventMouseButton && Input.IsMouseButtonPressed((int) ButtonList.Left))
            {
                EmitSignal(nameof(Shoot), Bullet, Rotation, Position);
            }
        }

        public override _Process(float delta)
        {
            LookAt(GetGlobalMousePosition());
        }
    }


In the main scene, we then connect the player's signal (it will appear in the
"Node" tab).

.. tabs::
 .. code-tab:: gdscript GDScript

    func _on_Player_shoot(Bullet, direction, location):
        var b = Bullet.instance()
        add_child(b)
        b.rotation = direction
        b.position = location
        b.velocity = b.velocity.rotated(direction)

 .. code-tab:: csharp

    public void _on_Player_Shoot(PackedScene Bullet, Vector2 direction, Vector2 location)
    {
        var bulletInstance = (Area2D) Bullet.Instance();
        AddChild(bulletInstance);
        bulletInstance.Rotation = direction;
        bulletInstance.Position = location;
        bulletInstance.Velocity = bulletInstance.Velocity.Rotated(direction);
    }

Now the bullets will maintain their own movement independent of the player's
rotation:

.. image:: img/signals_shoot2.gif

Conclusion
----------

Many of Godot's built-in node types provide signals you can use to detect
events. For example, an :ref:`Area2D <class_Area2D>` representing a coin emits
a ``body_entered`` signal whenever the player's physics body enters its collision
shape, allowing you to know when the player collected it.

In the next section, :ref:`doc_your_first_game`, you'll build a complete game
including several uses of signals to connect different game components.
