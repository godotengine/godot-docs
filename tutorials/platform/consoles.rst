.. _doc_consoles:

Console support in Godot
========================

Console porting process
-----------------------

In order to develop for consoles in Godot, you need access to the console SDK and
export templates for it. These export templates need to be developed either by
yourself or someone hired to do it, or provided by a third-party company.

Currently, the only console Godot officially supports is Steam Deck (through the
official Linux export templates).

The reason other consoles are not officially supported are:

- To develop for consoles, one must be licensed as a company.
  As an open source project, Godot has no legal structure to provide console ports.
- Console SDKs are secret and covered by non-disclosure agreements.
  Even if we could get access to them, we could not publish the platform-specific
  code under an open source license.

As explained, however, it is possible to port your games to consoles thanks to
services provided by third-party companies.

.. note::

    In practice, the process is quite similar to Unity and Unreal Engine. In other
    words, there is no engine that is legally allowed to distribute console export
    templates without requiring the user to prove that they are a licensed console
    developer.

Console publishing process
--------------------------

Regardless of the engine used to create the game, the process to publish a game
to a console platform is as follows:

- Register a developer account on the console manufacturer's website, then sign
  NDAs and publishing contracts. This requires you to have a registered legal
  entity.
- Gain access to the publishing platform by passing the acceptance process. This
  can take up to several months. Note that this step is significantly easier if
  an established publisher is backing your game. Nintendo is generally known to
  be more accepting of smaller developers, but this is not guaranteed.
- Get access to developer tools and order a console specially made for
  developers (*devkit*). The cost of those devkits is confidential.
- Port the engine to the console platform or pay a company to do it.
- To be published, your game needs to be rated in the regions you'd like to sell
  it in. For example, game ratings are handled by `ESRB <https://www.esrb.org/>`__
  in North America, and `PEGI <https://pegi.info/>`__ in Europe. Indie developers
  can generally get a rating for cheaper compared to more established developers.

Due to the complexity of the process, many studios and developers prefer to
outsource console porting.

You can read more about the console publishing process in this article:
`Godot and consoles, all you need to know <https://godotengine.org/article/godot-consoles-all-you-need-know/>`__

Third-party support
-------------------

Console ports of Godot are offered by third-party companies (which have
ported Godot on their own). These companies also offer publishing of
your games to various consoles.

Following is the list of providers:

- `Lone Wolf Technology <https://www.lonewolftechnology.com/>`_ offers
  Switch and Playstation 4 porting and publishing of Godot games.
- `Pineapple Works <https://pineapple.works/>`_ offers
  Switch, Xbox One & Xbox Series X/S (GDK) porting and publishing of Godot games (GDScript/C#).
- `RAWRLAB games <https://www.rawrlab.com/>`_ offers
  Switch porting of Godot games.
- `mazette! games <https://mazette.games/>`_ offers
  Switch, Xbox One and Xbox Series X/S porting and publishing of Godot games.
- `Olde Sküül <https://oldeskuul.com/>`_ offers
  Switch, Xbox One, Playstation 4 & Playstation 5 porting and publishing of Godot games.
- `Tuanisapps <https://www.tuanisapps.com/>`_ offers
  Switch porting and publishing of Godot games.
- `Seaven Studio <https://www.seaven-studio.com/>`_ offers
  Switch, Xbox One, Xbox Series, PlayStation 4 & PlayStation 5 porting of Godot games.
- `Sickhead Games <https://www.sickhead.com>`_ offers console porting to Nintendo Switch, PlayStation 4, PlayStation 5, Xbox One, and Xbox Series X/S for Godot games.
- `W4 Games <https://www.w4games.com/>`_ offers console ports for Nintendo Switch, Xbox Series X/S, and Playstation 5 for you to port your game yourself.

If your company offers porting, or porting *and* publishing services for Godot games,
feel free to
`contact the Godot Foundation <https://godot.foundation/#contact>`_
to add your company to the list above.
