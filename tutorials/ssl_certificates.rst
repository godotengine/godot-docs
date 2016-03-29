.. _doc_ssl_certificates:

SSL certificates
================

Introduction
------------

It is often desired to use SSL connections for communications to avoid
"man in the middle" attacks. Godot has a connection wrapper,
:ref:`StreamPeerSSL <class_StreamPeerSSL>`,
which can take a regular connection and add security around it. The
:ref:`HTTPClient <class_HTTPClient>`
class also supports HTTPS by using this same wrapper.

For SSL to work, certificates need to be provided. A .crt file must be
specified in the project settings:

.. image:: /img/ssl_certs.png

This file should contain any number of public certificates in
http://en.wikipedia.org/wiki/Privacy-enhanced_Electronic_Mail format.

Of course, remember to add .crt as filter so the exporter recognizes
this when exporting your project.

.. image:: /img/add_crt.png

There are two ways to obtain certificates:

Approach 1: self signed cert
----------------------------

The first approach is the simplest, just generate a private and public
key pair, and put the public pair in the .crt file (again, in PEM
format). The private key should go to your server.

OpenSSL has `some
documentation <https://www.openssl.org/docs/HOWTO/keys.txt>`__ about
this. This approach also **does not require domain validation** nor
requires you to spend a considerable amount of money in purchasing
certificates from a CA.

Approach 2: CA cert
-------------------

The second approach consists of using a certificate authority (CA)
such as Verisign, Geotrust, etc. This is a more cumbersome process,
but it's more "official" and ensures your identity is clearly
represented.

Unless you are working with large companies or corporations, or need
to connect to someone else's servers (i.e., connecting to Google or some
other REST API provider via HTTPS) this method is not as useful.

Also, when using a CA issued cert, **you must enable domain
validation**, to ensure the domain you are connecting to is the one
intended, otherwise any website can issue any certificate in the same CA
and it will work.

If you are using Linux, you can use the supplied certs file, generally
located in:

::

    /etc/ssl/certs/ca-certificates.crt

This file allows HTTPS connections to virtually any website (i.e.,
Google, Microsoft, etc.).

Or just pick any of the more specific certificates there if you are
connecting to a specific one.
