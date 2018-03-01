.. _doc_exporting_for_uwp:

Exporting for Universal Windows Platform
========================================

There's no extra requirement to export an ``.appx`` package that can be
installed as a Windows App or submited to the Windows Store. Exporting
packages also works from any platform, not only on Windows.

However, if you want to install and run the app, you need to sign it with a
trusted signature. Currently, Godot supports no signing of packages and you
need to use externals to tools to do so.

Also, make sure the Publisher name you set when export the package matches
the name on the certificate.

Limitations on Xbox One
-----------------------

As described in `UWP documentation <https://msdn.microsoft.com/en-us/windows/uwp/xbox-apps/system-resource-allocation>`__:

- Submitted as an "App"
    - available memory is 1GB
    - share of 2-4 CPU cores
    - shared access of GPU power (45%)

- Submitted as a "Game" (through `Xbox Live Creators Program <https://www.xbox.com/en-US/developers/creators-program>`__)
    - available memory is 5GB
    - 4 exclusive CPU cores and 2 shared CPU cores
    - exclusive access to GPU power (100%)
    
- Exceeding these memory limitations will cause allocation failures and the application will crash.

Creating a signing certificate
------------------------------

This requires the tools ``MakeCert.exe`` and ``Pvk2Pfx.exe`` which comes
with the Windows SDK. If you use Visual Studio, open one of its Developer
Prompts since they come with those tools available and in the path.

You can get more detailed instructions from `Microsoft documentation
<https://msdn.microsoft.com/en-us/library/windows/desktop/jj835832(v=vs.85).aspx>`__.

First, run ``MakeCert`` to create a private key::

    MakeCert /n publisherName /r /h 0 /eku "1.3.6.1.5.5.7.3.3,1.3.6.1.4.1.311.10.3.13" /e expirationDate /sv MyKey.pvk MyKey.cer

Where ``publisherName`` matches the Publisher Name of your package and
``expirationDate`` is in the ``mm/dd/yyyy`` format.

Next, create a Personal Information Exchange (.pfx) file using ``Pvk2Pfx.exe``::

    Pvk2Pfx /pvk MyKey.pvk /pi pvkPassword /spc MyKey.cer /pfx MyKey.pfx [/po pfxPassword]

If you don't specify a password with ``/po`` argument, the PFX will have the
same password as the private key.

You also need to trust this certificate to be able to actually install the
apps. Open the Command Prompt as Administrator and run the following command::

    Certutil -addStore TrustedPeople MyKey.cer

Signing the package
-------------------

Using the ``SignTool.exe`` this requires a single command::

    SignTool sign /fd SHA256 /a /f MyKey.pfx /p pfxPassword package.appx

Installing the package
----------------------

After Windows 10 Anniversary Update you can install packages by just double
clicking the ``.appx`` file from the Windows Explorer.

It's also possible to install using the ``Add-AppxPackage`` PowerShell cmdlet.

Note that if you don't update the version number, you'll have to uninstall the
previous installed package before reinstalling it.
