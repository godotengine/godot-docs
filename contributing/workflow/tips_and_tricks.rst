.. _doc_contributing_workflow_tips_and_tricks:

Tips and tricks
===============

This page contains a collection of tips and tricks to help you contribute more
efficiently. These are directed at "power users" who are already contributing
to the project and are looking for ways to streamline the process.

Open issues faster using browser search shortcuts
-------------------------------------------------

If you chat with engine developers outside of GitHub, you may encounter
plain issue numbers like "issue #12345" in conversations, without a link.
Rather than navigating the GitHub issue tracker to find the issue, you can
add a custom search engine to your browser to open issues faster.

For Chrome:

1. Go to the search engine settings page using ``chrome://settings/searchEngines``.
2. Scroll down to "Site search" in the lower middle of the page and click "Add".
3. Fill in the form with name "Godot GitHub", shortcut "#", and URL ``https://github.com/godotengine/godot/issues/%s``.
4. You can now type ``# 12345`` in the address bar to open issue #12345 (be sure to include the space).

For Firefox, the instructions are similar, but the "Add" button is hidden by default, so it needs to be enabled first:

1. Go to the ``about:config`` page.
2. Type ``browser.urlbar.update2.engineAliasRefresh`` in the search bar.
3. Click the "+" button to add a new boolean with this name (it should say ``true``).
4. Go to the search settings page using ``about:preferences#search``.
5. Scroll down to the bottom to find "Search Shortcuts" and click "Add".
6. Fill in the form with name "Godot GitHub", URL ``https://github.com/godotengine/godot/issues/%s``, and alias "#".
7. You can now type ``# 12345`` in the address bar to open issue #12345 (be sure to include the space).

The same shortcut works for both issues and PRs.
For example, number 12345 itself is actually a PR, and so ``# 12345``
will lead to ``https://github.com/godotengine/godot/pull/12345``.
