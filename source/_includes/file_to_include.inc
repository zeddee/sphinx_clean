
.. it appears that titles are not being parsed correctly
   by the sphinx build engine.
   -----
   Title
   -----
   gives an 'Unexpected section title' error, even though it follows
   docutils heading hierarchy conventions

.. rubric:: This is an include

You can write directives in an ``.. include::``, like this:

.. code-block:: text

   this directive is part of the include
