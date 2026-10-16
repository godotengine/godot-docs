.. _doc_plural_rules:

Plural rules
~~~~~~~~~~~~

.. Note: This list should be synced with core/string/locales.h in the engine.

This is the full list of built-in plural rules available in Godot in human-readable form.
See the `source code <https://github.com/godotengine/godot/blob/4.6.3-stable/core/string/locales.h#L1819-L1855>`__
for their original gettext format form.

These plural rules are automatically used when no plural rule is specified in
:ref:`CSV localization <doc_localization_using_spreadsheets>`. Plural forms are
spelled out in the order they should be specified in the CSV file (from top to
bottom).

.. tip::

    Use your browser's search function (:kbd:`Ctrl + F` or :kbd:`Cmd + F`) to
    quickly find a specific language according to its
    :ref:`locale code <doc_locales>`.

Plural rules
------------

- Languages with no plural forms (``bm bo dz hnj id ig ii in ja jbo jv jw kde kea km ko lkt lo ms my nqo osa root sah ses sg su th to tpi vi wo yo yue zh``):

  - First form for all numbers.

- Languages with the same rules as English (``af an asa ast az bal bem bez bg brx ca ce cgg chr ckb da de dv ee el en eo es et eu fi fo fur fy gl gsw ha haw he hu ia io it jgo ji jmc ka kaj kcg kk kkj kl ks ksb ku ky lb lg lij mas mgo ml mn mr nah nb nd ne nl nn nnh no nr ny nyn om or os pap ps pt rm rof rwk saq sc sd sdh seh sn so sq ss ssy st sv sw syr ta te teo tig tk tn tr ts ug ur uz ve vo vun wae xh xog yi``):

  - First form for 1.
  - Second form for 0, and for 2 and above.

- Languages with the same rules as French (``ak bho csw ff fr guw hy kab ln mg nso pa pt_BR si ti wa``):

  - First form for 0 and 1.
  - Second form for 2 and above.

- Icelandic, Macedonian (``is mk``):

  - First form when the last digit is 1 but the number is not 11.
  - Second form for all other numbers.

- Central Atlas Tamazight (``tzm``):

  - First form for 0, 1, and all numbers from 11 to 99.
  - Second form for 2-10, and for 100 and above.

- Amharic, Assamese, Bengali, Dogri, Persian, Gujarati, Hindi, Kannada, Nigerian Pidgin, Zulu (``am as bn doi fa gu hi kn pcm zu``):

  - First form for 2 and above.
  - Second form for 0 and 1.

- Cebuano, Filipino, Tagalog (``ceb fil tl``):

  - First form for 1, 2, and 3, and for any number that does not end in 4, 6, or 9.
  - Second form for numbers ending in 4, 6, or 9.

- Prussian (``prg``):

  - First form for numbers ending in 0 and for numbers 11-19.
  - Second form for numbers ending in 1, except 11.
  - Third form for all remaining numbers.

- Latvian (``lv``):

  - First form for numbers ending in 1, except 11.
  - Second form for all non-zero numbers (including 11).
  - Third form for 0.

- Lithuanian (``lt``):

  - First form for numbers ending in 1, except 11.
  - Second form for numbers ending in 2-9, excluding the teens (12-19).
  - Third form for 0, for the teens (10-19), and for numbers ending in 0.

- Belarusian, Croatian, Russian, Serbian, Ukrainian (``be hr ru sr uk``):

  - First form for numbers ending in 1, except 11.
  - Second form for numbers ending in 2-4, except the teens (12-14).
  - Third form for everything else.

- Bosnian, Serbo-Croatian (``bs sh``):

  - First form for numbers ending in 1, except 11.
  - Second form for numbers ending in 2-4, except 12-14.
  - Third form for everything else.

- Langi (``lag``):

  - First form for 0.
  - Second form for 1.
  - Third form for 2 and above.

- Anii, Colognian (``blo ksh``):

  - First form for 0.
  - Second form for 1.
  - Third form for 2 and above.

- Tachelhit (``shi``):

  - First form for 0 and 1.
  - Second form for 2-10.
  - Third form for 11 and above.

- Polish (``pl``):

  - First form for 1.
  - Second form for numbers ending in 2-4, except the teens (12-14).
  - Third form for everything else.

- Moldavian (``mo``):

  - First form for 1.
  - Second form for 0 and for numbers whose last two digits are 01-19 (except when the number itself is exactly 1).
  - Third form for numbers whose last two digits are 00 or 20-99.

- Inuktitut, Hebrew, Nama, Northern Sami, Sami, Southern Sami, Lule Sami, Inari Sami, Santali, Skolt Sami (``iu iw naq sat se sma smi smj smn sms``):

  - First form for 1.
  - Second form for 2.
  - Third form for everything else.

- Czech, Slovak (``cs sk``):

  - First form for 1.
  - Second form for 2-4.
  - Third form for 0 and 5 and above.

- Romanian (``ro``):

  - First form for 1.
  - Second form for 0 and for numbers whose last two digits are 01-19.
  - Third form for numbers whose last two digits are 00 or 20-99.

- Irish (``ga``):

  - First form for 1.
  - Second form for 2.
  - Third form for everything else.

- Slovenian (``sl``):

  - First form for numbers ending in 01.
  - Second form for numbers ending in 02.
  - Third form for numbers ending in 03 or 04.
  - Fourth form for everything else.

- Lower Sorbian, Upper Sorbian (``dsb hsb``):

  - First form for numbers ending in 01.
  - Second form for numbers ending in 02.
  - Third form for numbers ending in 03 or 04.
  - Fourth form for everything else.

- Manx (``gv``):

  - First form for numbers ending in 1.
  - Second form for numbers ending in 2.
  - Third form for numbers ending in 00, 20, 40, 60, or 80.
  - Fourth form for everything else.

- Scottish Gaelic (``gd``):

  - First form for 1 and 11.
  - Second form for 2 and 12.
  - Third form for 3-10 and 13-19.
  - Fourth form for everything else (0 and 20+).

- Breton (``br``):

  - First form for numbers ending in 1, except 11, 71, and 91.
  - Second form for numbers ending in 2, except 12, 72, and 92.
  - Third form for numbers ending in 3, 4, or 9, except those in the ranges 13-19, 73-79, and 93-99.
  - Fourth form for non-zero multiples of 1,000,000.
  - Fifth form for everything else.

- Maltese (``mt``):

  - First form for 1.
  - Second form for 2.
  - Third form for 0 and for numbers ending in 03-10.
  - Fourth form for numbers ending in 11-19.
  - Fifth form for everything else.

- Cornish (``kw``):

  - First form for 0.
  - Second form for 1.
  - Third form for numbers ending in 02, 22, 42, 62, or 82, and for certain round numbers.
  - Fourth form for numbers ending in 03, 23, 43, 63, or 83.
  - Fifth form for numbers ending in 01, 21, 41, 61, or 81 (except 1 itself).
  - Sixth form for everything else.

- Arabic, Najdi Arabic (``ar ars``):

  - First form for 0.
  - Second form for 1.
  - Third form for 2.
  - Fourth form for numbers ending in 03-10.
  - Fifth form for numbers ending in 11-99.
  - Sixth form for numbers ending in 00, 01, or 02 (i.e., 100, 101, 102, 200, etc.).

- Welsh (``cy``):

  - First form for 0.
  - Second form for 1.
  - Third form for 2.
  - Fourth form for 3.
  - Fifth form for 6.
  - Sixth form for everything else.
