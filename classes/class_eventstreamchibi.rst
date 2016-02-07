.. _class_EventStreamChibi:

EventStreamChibi
================

Inherits: :ref:`EventStream<class_eventstream>`
-----------------------------------------------

Category: Core
--------------

Brief Description
-----------------

Driver for MOD playback.

Description
-----------

This driver plays MOD music. MOD music, as all event-based streams, is a music format defined by note events ocurring at defined moments, instead of a stream of audio samples.

Currently, this driver supports the MOD, S3M, IT, and XM formats.

This class exposes no methods.

This class can return its playback positon in seconds, but does not allow to set it, failing with only a console warning.

This class can not return its song length, returning 1.0 when queried.

This class does not limit its volume settings, allowing for overflow/distortion and wave inversion.

