.. _doc_instancing_continued:

Instancing (continued)
======================

Recap
-----

Instancing has many handy uses. At a glance, with instancing you have:

-  The ability to subdivide scenes and make them easier to manage.
-  A more flexible alternative to prefabs (and much more powerful given
   instances work at many levels).
-  A way to design more complex game flows or even UIs (UI Elements are
   nodes in Godot too).

Design language
---------------

But the real strong point of instancing scenes is that it works as an
excellent design language. This is pretty much what makes Godot special
and different to any other engine out there. The entire engine was designed
from the ground up around this concept.

When making games with Godot, the recommended approach is to leave aside
other design patterns such as MVC or Entity-Relationship diagrams and
start thinking games in a more natural way. Start by imagining the
visible elements in a game, the ones that can be named not by just a
programmer but by anyone.

For example, here's how a simple shooter game can be imagined:

.. image:: /img/shooter_instancing.png

It's pretty easy to come up with a diagram like this for almost any kind
of game. Just write down the elements that come to mind, and then the
arrows that represent ownership.

Once this diagram exists, making a game is about creating a scene for
each of those nodes, and use instancing (either by code or from the editor) to represent ownership.

Most of the time programming games (or software in general) is spent
designing an architecture and fitting game components to that
architecture. Designing based on scenes replaces that and makes
development much faster and more straightforward, allowing to
concentrate on the game itself. Scene/Instancing based design is
extremely efficient at saving a large part of that work, since most of
the components designed map directly to a scene. This way, none or
little architectural code is needed.

The following is a more complex example, an open-world type of game with
lots of assets and parts that interact:

.. image:: /img/openworld_instancing.png

Make some rooms with furniture, then connect them. Make a house later,
and use those rooms as the interior.

The house can be part of a citadel, which has many houses. Finally the
citadel can be put on the world map terrain. Add also guards and other
NPCs to the citadel by previously creating their scenes.

With Godot, games can grow as quickly as desired, as only more scenes
have to be made and instanced. The editor UI is also designed to be
operated by non programmers too, so an usual team development process
involves 3D or 2D artists, level designers, game designers, animators,
etc all working with the editor interface.

Information overload!
---------------------

Do not worry too much, the important part of this tutorial is to create
awareness on how scenes and instancing are used in real life. The best
way to understand all this is to make some games.

Everything will become very obvious when put to practice, so, please do
not scratch your head and go on to the next tutorial!
