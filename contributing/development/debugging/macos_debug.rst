Debugging on macOS
==================

Debugging Godot editor
----------------------

Attaching a debugger to the signed macOS process requires the "com.apple.security.get-task-allow" entitlement, which is not enabled by default, since apps can't be notarized as long as it is enabled.
If you want to debug an official build of the editor it should be re-signed with the proper entitlements.

Create an ``editor.entitlements`` text file with the following contents:

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
    <plist version="1.0">
        <dict>
            <key>com.apple.security.cs.allow-dyld-environment-variables</key>
            <true/>
            <key>com.apple.security.cs.allow-jit</key>
            <true/>
            <key>com.apple.security.cs.allow-unsigned-executable-memory</key>
            <true/>
            <key>com.apple.security.cs.disable-executable-page-protection</key>
            <true/>
            <key>com.apple.security.cs.disable-library-validation</key>
            <true/>
            <key>com.apple.security.device.audio-input</key>
            <true/>
            <key>com.apple.security.device.camera</key>
            <true/>
            <key>com.apple.security.get-task-allow</key>
            <true/>
        </dict>
    </plist>

Then use the following command to re-sign the editor:

::

    codesign -s - --deep --force --options=runtime --entitlements ./editor.entitlements ./path/to/Godot.app

Debugging exported project
--------------------------

To allow debugging, select the ``codesign\debugging`` (``com.apple.security.get-task-allow``) entitlement during the export. When it is selected, notarization is not supported and should be disabled.
