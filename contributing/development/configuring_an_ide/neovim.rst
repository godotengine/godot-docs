.. _doc_configuring_an_ide_rider:

Neovim
======

`Neovim <https://neovim.io/>`__ is a hyper-extensible vim-based editor that is fully free to use and open-source under the Apache 2.0 license.
On it's own, it is as simple as a plain-text editor, but with plugins it can be extended to be a fully fledged IDE of your own design.

Setting Up Neovim
-----------------

Neovim is configured with a lua scripting API, it is recommended to use a package manager such as `lazy.nvim <https://github.com/folke/lazy.nvim>`__ to make management of plugins and configs easier. Users new to Neovim can use an existing distribution, or pre-made configs to get started. See `kickstart.nvim <https://github.com/nvim-lua/kickstart.nvim>`__ for an effective starting point for a custom neovim config, as it includes most basic functionality pre-configured and has comments explaining various components.

- For new Neovim users, using the ``:Tutor`` command is recommended to learn the basic keymaps and operation of the software.
- Keep in mind that Neovim is a modal, keyboard based editor, and may take some adjustment.
- Neovim is a terminal-based editor, so basic understanding of terminal navigation is recommended.
- | To begin editing the config, or installing a pre-made one, the configuration files can be found in the following locations:
  | Windows: ``Appdata/Local/nvim``
  | Linux, MacOS, BSD: ``~/.config/nvim``

Setting Up Godot Project
------------------------

Once Neovim is configured to the user's liking, the project can be set-up by following the following steps:

- Ensure all tools are installed
    a. SCons
    b. Clang
    c. Terminal Emulator (Any work, Windows provides an option in the Microsoft Store)
    d. Neovim Language Plugins through the Mason plugin, or manual config (clangd, codelldb, optionally cpplint)

- | Run SCons with the command ``scons platform=windows devbuild=yes compiledb=yes`` to run the build system.
  | The compiledb=yes argument ensures that a compilation database file is generated, which is necessary for correct clangd function.
  | The ``dev_build`` parameter makes sure the debug symbols are included, allowing to e.g. step through code using breakpoints.
- You should now be able to open the project by running ``nvim`` in a terminal window open to the project directory.
- The project can be rebuilt at any time by running the ``:terminal`` Neovim command and running SCons with the previous arguments.

Using a LSPs, DAPs, and more in Neovim
--------------------------------------

LSPs (Language Server Protocols) are used for various language functions, such as auto-completion, syntax highlighting, etc. 
DAPs (Debug Adapter Protocols) are used for various debugging functions. 
Linters and formatters are simply used for automatically formatting the code. 

- Mason.nvim is used to manage LSPs, DAPs, linters, and formatters for Neovim.
- Users also need to install LSP and DAP support plugins to enable these features.
- It is recommended to use additional plugins such as `MasonLSPConfig <https://github.com/williamboman/mason-lspconfig.nvim>`__ and `MasonNvimDAP <https://github.com/jay-babu/mason-nvim-dap.nvim>`__ to handle automatically configuring the LSPs and DAPs you install with ``:MasonInstall``.
- 


If you run into any issues, ask for help in one of
`Godot's community channels <https://godotengine.org/community>`__.
