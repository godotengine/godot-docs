.. _doc_consoles:

Console support in Godot
========================

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
- Get access to developer hardware and software (also known as devkit or SDK = 
  Software development Kit).
  The cost of those devkits is confidential.
  The SDK hardware is usually a console specially made for developers. The 
  software consists of tools and APIs which have to be integrated into your game 
  and build process. 
- Port the engine to the console platform or pay a company to do it. Porting is 
  the porcess of integrating the consoles manufactors software and requirements 
  into the game and build process. There countless other smaller and bigger 
  consideration and reuirements to be fullfilled (think Steam capsules), and 
  adjustment to the controlls of your game to be made to support the specific 
  console hardware. This process can take months. 
- To be published, your game needs to be rated in the regions you'd like to sell
  it in. For example, in North America, the `ESRB <https://www.esrb.org/>`__
  handles game ratings. In Europe, this is done by
  `PEGI <https://pegi.info/>`__. Indie developers can generally get a rating
  for cheaper compared to more established developers.

Due to the complexity of the process, many studios and developers decide to 
outsource console porting (see thrid-party providers below).

.. note::

    In practice, the process is quite similar to Unity and Unreal Engine.
    In other words, there is no engine that is legally allowed to
    distribute console export templates without requiring the user to prove that
    they are a licensed console developer.

Besides the need to be a signed and licensed developer and having access to the 
console SDK, Godot developers also need export templates to export their game to 
consoles. Currently you either need to create these export tempates 
yourself, hire someone to do it for you, or license premade export templates 
from a third party, like those listed below.

There are active talks between Godot lead devs and console manufactors to 
improve this process. If you are a licensed developer and would like to port 
to console using Godot, please message Juan Linietsky at
<https://godotengine.org/governance/>.

Third-party support
-------------------

Console ports of Godot are offered by third-party companies (which have
ported Godot on their own). These companies also offer publishing of
your games to various consoles.

Following is the list of providers:

- `Lone Wolf Technology <http://www.lonewolftechnology.com/>`_ offers
  Switch and PS4 porting and publishing of Godot games.
- `Pineapple Works <https://pineapple.works/>`_ offers
  Switch and Xbox One porting and publishing of Godot games.

If your company offers porting and/or publishing services for Godot games,
feel free to
`open an issue or pull request <https://github.com/godotengine/godot-docs>`_
to add your company to the list above.
