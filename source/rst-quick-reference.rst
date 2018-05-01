.. This is a comment
..
   _so: is this!
..
   [and] this!
..
   this:: too!
..
   |even| this:: !

*********************************
reStructuredText Quick Reference
*********************************

.. contents:: Table of Contents
    :local:
    :depth: 1

Basic Formatting
================

**bold**

*italics*

``this is a code sample``

.. code-block:: javascript
   :lineno-start: 999
   :emphasize-lines: 3,6

   const o = ()=> console.log("this is also a code block")
   o()
   // this is a comment
   // Enable line numbers with the :linenos: option
   // You can start from a specific line with :lineno-start: <line>
   // Highlight specific lines with :emphasize-lines: <line>,<line2>..

usingmarkup\ **in**\ strings\ :superscript:`thisissuperscript`\ :subscript:`thisissubscript`

author name, :title-reference:`this is a book title` (NY: New York University Press, 2018)

Headers
=======

Section headers are created by underlining (and optionally overlining) the section title with a punctuation character, at least as long as the text:

.. code-block:: rst

   =================
   This is a heading
   =================

The structure is determined contextually from the succession of headings — there is no way to explicitly determine header levels. Python documentation suggests the following conventions:

* ``#`` with overline, for parts
* ``*`` with overline, for chapters
* ``=``, for sections
* ``-``, for subsections
* ``^``, for subsubsections
* ``"``, for paragraphs

Lists
=====

.. rubric:: List

* Item 1
* Item 2
    * Nested item 1
    * Nested item 2
* Item 3

.. rubric:: List

1. Item 1
2. Item 2
    1. Nested item 1
    2. Nested item 2
3. Item 3

.. rubric:: List

#. Item 1
#. Item 2
    #. Nested item 1
    #. Nested item 2

.. code-block:: rst

    .. rubric:: List

    * Item 1
    * Item 2
        * Nested item 1
        * Nested item 2
    * Item 3

    .. rubric:: List

    1. Item 1
    2. Item 2
        1. Nested item 1
        2. Nested item 2
    3. Item 3

    .. rubric:: List

    #. Item 1
    #. Item 2
        #. Nested item 1
        #. Nested item 2

Hyperlinks
==========

This is how to write hyperlinks_. Hyperlink targets can accept `spaces in names`_ by enclosing the hyperlink text in backticks.

.. _hyperlinks: http://example.com
.. _spaces in names: http://example.com

Internal hyperlinks have no link specified in the directive. Instead, internal hyperlink targets can be specified by writing the hyperlink directive above the target element. For example, this hyperlink goes here_.

.. _here:

.. topic:: Hyperlink target
   
   This is the hyperlink target.

.. code-block:: rst

    This is how to write hyperlinks_. Hyperlink targets can accept `spaces in names`_ by enclosing the hyperlink text in backticks.

    .. _hyperlinks: http://example.com
    .. _spaces in names: http://example.com

    Internal hyperlinks have no link specified in the directive. Instead, internal hyperlink targets can be specified by writing the hyperlink directive above the target element. For example, this hyperlink goes here_.

    .. _here:

    .. topic:: Hyperlink target
       
       This is the hyperlink target.

Admonitions
===========


.. admonition:: custom caption

   This is a custom admonition


.. caution::

   Caution!
   
   Write more than one line

List of admonitions available:

* admonition
* attention
* caution
* danger
* error
* hint
* important
* note
* tip
* warning

.. admonition:: admonition

    This is an admonition.

.. attention::

    This is a call to attention.

.. caution::

    This is a caution.

.. danger::

    This is dangerous.

.. error::

    This is an error.

.. hint::

    This is a hint.  

.. important::

    This is important.

.. note::

    This is a note.

    There is more than one line.

.. tip::

    This is a tip. 

.. warning::

    This is a warning


Images
======

The ``.. image:: <path>`` directive allows you to specify ``:height: <h>`` and ``:width: <w>`` options. Also can apply the ``:scale: <percent>`` option. Use the ``:target: <url>`` option to turn the image into a clickable link.


.. image:: /_static/core_assets/logo.jpg
   :width: 50%
   :target: http://example.com
   :class: .noBorder

The ``.. figure:: <path>`` directive inserts an image, and allows caption content. Accepts either a ``:scale: <percent>`` or a ``:figwidth: <w>`` option. ``:figclass: <class>`` option allows you to assign the figure a class.


.. figure:: _static/core_assets/logo.jpg
   :scale: 50 %
   :alt: map to buried treasure
   :figwidth: 100%
   :figclass: .asdf
   :class: .border

   This is the caption of the figure (a simple paragraph).

   The legend consists of all elements after the caption.  In this
   case, the legend consists of this paragraph and the following
   table:

   +---------------------------+-----------------------+
   | Symbol                    | Meaning               |
   +===========================+=======================+
   | ``.. image:: tent.png``   | Campground            |
   +---------------------------+-----------------------+
   | ``.. image:: waves.png``  | Lake                  |
   +---------------------------+-----------------------+
   | ``.. image:: peak.png``   | Mountain              |
   +---------------------------+-----------------------+

Tables
======
You can insert tables as ASCII tables or using the ``csv-table::`` directive.

ASCII tables:

.. code-block:: rst

    +---------------------------+-----------------------+
    | Header                    | Header                |
    +===========================+=======================+
    | ``thing``                 | Campground            |
    +---------------------------+-----------------------+
    | ``thing``                 | Lake                  |
    +---------------------------+-----------------------+
    | ``thing``                 | Mountain              |
    +---------------------------+-----------------------+

is rendered as:

+---------------------------+-----------------------+
| Header                    | Header                |
+===========================+=======================+
| ``thing``                 | Campground            |
+---------------------------+-----------------------+
| ``thing``                 | Lake                  |
+---------------------------+-----------------------+
| ``thing``                 | Mountain              |
+---------------------------+-----------------------+

Using the ``csv-table::`` directive:

.. code-block:: rst

  .. csv-table:: Title
    :header: "name", "firstname", "age"
    :widths: 20, 20, 10

    "Smith", "John", 40
    "Smith", "John, Junior", 20

is rendered as: 

.. csv-table:: Title
    :header: "name", "firstname", "age"
    :widths: 20, 20, 10

    "Smith", "John", 40
    "Smith", "John, Junior", 20

Body elements
=============

.. sidebar:: Sidebar title
   :subtitle: Optional subtitle
   :class: sidebar_class
   :name: this_sidebar

   This is a sidebar. You can use the ``:subtitle: <text>`` and the ``:class: <class>`` option. The ``:name: <name>`` option assigns the sidebar an ID.

   Place the sidebar at the top of the text paragraph or element that you want the sidebar to sidebar.

.. epigraph::

   No matter where you go, there you are.

   -- Buckaroo Banzai

Lorem dim sum Rice noodle roll deep fried crab claw soup dumpling cold chicken claw xo spicy rice noodle roll honey glazed BBQ pork soy sauce chicken roast duck. Jin deui Chicken feet Potstickers stir fried radish cake Steamed Bun with Butter Cream hot raw fish slices porridge traditional steamed glutinous rice.

Deep fried garlicky fish ball chee cheong fun with barbecued pork steamed radish cake steamed bun with premium lotus paste cabbage roll paekuat.

Cha siu sou Cheong fan pan fried bitter melon beef dumpling mango pudding coconut milk pudding black sesame soft ball deep fried bean curd skin rolls.

Stir fried radish cake Steamed Bun with Butter Cream hot raw fish slices porridge traditional steamed glutinous rice with zhu hao sauce crispy yam puff crispy dragon roll honeydew puree with sago.

Jiu cai bau Zhaliang Pei guen Lo baak gou Taro cake. Dried scallop and leek puff deep fried seaweed roll BBQ pork puff Pan friend pork dumpling Pot sticker water chestnut cake bitter melon beef dumplings turnip cake leek dumplings deep fried taro turnover.

.. topic:: This is a topic
   :class: classname
   :name: asdf

   A topic is like a block quote with a title, or a self-contained section with no subsections. Use the "topic" directive to indicate a self-contained idea that is separate from the flow of the document. Topics may occur anywhere a section or transition may occur. Body elements and topics may not contain nested topics.

   The directive's sole argument is interpreted as the topic title; the next line must be blank. All subsequent lines make up the topic body, interpreted as body elements.

Writing References
==================

Footnotes
---------

Lorem ipsum [#f1]_ dolor sit amet ... [#f2]_. Use a rubric\ [#f3]_ to designate an informal heading.

.. rubric:: Footnotes

.. [#f1] Text of the first footnote.
.. [#f2] Text of the second footnote.
.. [#f3] rubric n. 1. a title, heading, or the like, in a manuscript, book, statute, etc., written or printed in red or otherwise distinguished from the rest of the text. An informal heading that doesn't correspond with the document structure.

.. code-block:: rst

    Lorem ipsum [#f1]_ dolor sit amet ... [#f2]_. Use a rubric\ [#f3]_ to designate an informal heading.

    .. rubric:: Footnotes

    .. [#f1] Text of the first footnote.
    .. [#f2] Text of the second footnote.
    .. [#f3] rubric n. 1. a title, heading, or the like, in a manuscript, book, statute, etc., written or printed in red or otherwise distinguished from the rest of the text. An informal heading that doesn't correspond with the document structure.

Citations
---------

Lorem ipsum\ [Refd]_ dolor sit amet.

\[…\]

.. [Refd] Book or article reference, URL or whatever.

.. code-block:: rst

    Lorem ipsum\ [Ref]_ dolor sit amet.

    \[…\]

    .. [Ref] Book or article reference, URL or whatever.

Variables
=========

Variables are defined using the following syntax:

.. code-block:: rst

   .. |<variable_name>| <directive>::<arg>
      [:dir_options:]

      [<dir_content>]


Simple text variables use the ``.. replace:: <text>`` directive.

This is a variable: |varname|

.. |varname| replace:: variable name

An example of a more complex text replacement:

.. code-block:: rst
   
   But still, that's nothing compared to a name like |j2ee-cas|__.

   .. |j2ee-cas| replace::
      the Java `TM`:superscript: 2 Platform, Enterprise Edition Client
      Access Services
   __ http://developer.java.sun.com/developer/earlyAccess/
      j2eecas/

Gives us:

But still, that's nothing compared to a name like
|j2ee-cas|__.

.. |j2ee-cas| replace::
   the Java `TM`:superscript: 2 Platform, Enterprise Edition Client
   Access Services
__ http://developer.java.sun.com/developer/earlyAccess/
   j2eecas/

Variables can also use the ``.. images::`` directive. For example, |sub_image|.

.. |sub_image| image:: /_static/core_assets/logo.jpg
   :width: 100px

Use variables to insert unicode characters. For example, ``.. |copy| unicode:: 0xA9 .. copyright sign`` inserts |copy|.

.. |copy| unicode:: 0xA9 .. copyright sign


Includes
============

You can include external content using the ``include::`` directive:

.. code-block:: rst

    .. include:: _includes/file_to_include.inc

This will be rendered as:

.. admonition:: Example

    .. include:: _includes/file_to_include.inc

.. note::

    * Heading levels in includes will follow the heading 
      conventions of the including page (i.e. this page)
    * If the heading levels used in the included file does not 
      follow the heading conventions of the including page, you may 
      encounter unexpected behaviour re: TOC and heading rendering.

More options:

.. code-block:: none

    start-line : integer
    Only the content starting from this line will be included. (As usual in Python, the first line has index 0 and negative values count from the end.)
    end-line : integer
    Only the content up to (but excluding) this line will be included.
    start-after : text to find in the external data file
    Only the content after the first occurrence of the specified text will be included.
    end-before : text to find in the external data file
    Only the content before the first occurrence of the specified text (but after any after text) will be included.
    literal : flag (empty)
    The entire included text is inserted into the document as a single literal block.
    code : formal language (optional)
    The argument and the content of the included file are passed to the code directive (useful for program listings). (New in Docutils 0.9)
    number-lines : [start line number]
    Precede every code line with a line number. The optional argument is the number of the first line (defaut 1). Works only with code or literal. (New in Docutils 0.9)
    encoding : name of text encoding
    The text encoding of the external data file. Defaults to the document's input_encoding.
    tab-width : integer
    Number of spaces for hard tab expansion. A negative value prevents expansion of hard tabs. Defaults to the tab_width configuration setting.
    With code or literal the common options :class: and :name: are recognized as well.

    Combining start/end-line and start-after/end-before is possible. The text markers will be searched in the specified lines (further limiting the included content).

HTML metadata
=============

Adding metadata to HTML pages helps SEO.

An example of a ``.. meta::`` directive:

.. code-block:: rst
   
   .. meta::
      :description lang=en: The reStructuredText plaintext markup language.
      :description lang=de: Ich spreche nein Deutsche.
      :keywords: plaintext, markup language
      :http-equiv=Content-Type: text/html; charset=ISO-8859-1
