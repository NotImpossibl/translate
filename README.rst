Translate Toolkit
-----------------

.. image:: https://img.shields.io/gitter/room/translate/pootle.svg?style=flat-square
   :alt: Join the chat at https://gitter.im/translate/pootle
   :target: https://gitter.im/translate/pootle

.. image:: https://github.com/translate/translate/workflows/Test/badge.svg
    :alt: Build Status
    :target: https://github.com/translate/translate/actions

.. image:: https://img.shields.io/codecov/c/github/translate/translate/master.svg?style=flat-square
    :alt: Test Coverage
    :target: https://codecov.io/gh/translate/translate/branch/master

.. image:: https://api.dependabot.com/badges/status?host=github&repo=translate/translate
    :target: https://app.dependabot.com/accounts/translate/repos/3769696
    :alt: Requirements

.. image:: https://img.shields.io/pypi/v/translate-toolkit.svg?style=flat-square
    :alt: Released version
    :target: https://pypi.python.org/pypi/translate-toolkit/

.. image:: https://img.shields.io/pypi/pyversions/translate-toolkit.svg?style=flat-square
    :alt: Supported Python versions
    :target: https://pypi.python.org/pypi/translate-toolkit/

.. image:: https://img.shields.io/pypi/l/translate-toolkit.svg?style=flat-square
    :target: https://pypi.python.org/pypi/translate-toolkit/
    :alt: License

Translate 工具包是一套软件和文档，旨在帮助本地化人员提高工作效率，减少挫折感。该工具包是 Translate 项目的一部分，托管在 <https://github.com/translate>。

该软件包括将本地化格式转换为通用 PO 和新兴 XLIFF 格式的程序。此外，还有检查和管理 PO 和 XLIFF 文件的程序。在线文档包括使用工具、运行本地化项目以及如何本地化从 OpenOffice.org 到 Mozilla 的各种项目的指南。

该软件的核心包含一组用于处理各种本地化存储格式的类： DTD、属性、OpenOffice.org GSI/SDF、CSV、MO、Qt .ts、TMX、TBX、WordFast txt、Gettext .mo、Windows RC，当然还有 PO 和 XLIFF。它还提供了在这些格式之间进行转换的脚本。

工具包中还有 Python 程序，用于创建字数统计、合并译文以及对翻译文件执行各种检查。

该软件的核心包含一组用于处理各种本地化存储格式的类
本地化存储格式： DTD, properties, OpenOffice.org GSI/SDF、
CSV、MO、Qt .ts、TMX、TBX、WordFast txt、Gettext .mo、Windows RC，以及
当然还有 PO 和 XLIFF。 它还提供了在这些格式之间进行转换的脚本。
格式之间进行转换的脚本。

该工具包还包含 Python 程序，用于创建字数统计、合并翻译和对翻译文件进行各种检查。
翻译并对翻译文件执行各种检查。


Important Links
---------------

* `Latest release downloads <https://github.com/translate/translate/releases>`_
* `Documentation
  <http://docs.translatehouse.org/projects/translate-toolkit/en/latest/>`_,
  also use ``--help`` with any of the commands.
* The Translate Toolkit is released under the `GPL
  <https://github.com/translate/translate/blob/master/COPYING>`_ with
  `contributions from many people
  <https://github.com/translate/translate/blob/master/CREDITS>`_.
* `Reporting issues <https://github.com/translate/translate/issues>`_
* `Installation <http://docs.translatehouse.org/projects/translate-toolkit/en/stable/installation.html>`_


Joining the Translate Project
-----------------------------
If you would like to join the translate project mailing list then visit:
<http://lists.sourceforge.net/lists/listinfo/translate-devel>.

The vision of the Translate Project is to be a meta project for localizers
built on the premise that your language deserves to be a project on its own
right not a poor cousin of the main project.

Most projects are inattentive to the needs and difficulties experienced by
localizers. To that end the aim is to work towards creating tools and
documentation that allows localizers to focus on what they do best: translating
software.

Requirements
------------

There are several extra requirements which you might to install to get full
feature set. This cal be easily specified during pip installation::

    # Install with XML support
    pip install translate-toolkit[XML]

    # Install all optional dependencies
    pip install translate-toolkit[all]

.. note:: Please check ``requirements/*.txt``::

       pip install -r requirements/optional.txt

   Will install all optional dependencies convering support for many other
   formats.

The Toolkit requires Python 3.8 or newer.

The package lxml is required. You should install version 4.6.3 or later.
<http://lxml.de/> Depending on your platform, the easiest way to install might
be through your system's package management. Alternatively you can try ::

    pip install lxml

which should install the newest version from the web.

For Mac OSX, the following pages might be of help:
<http://lxml.de/build.html#building-lxml-on-macos-x>
<http://lxml.de/installation.html#macos-x>

The package lxml has dependencies on libxml2 and libxslt. Please check the lxml
site for the recommended versions of these libraries if you need to install
them separately at all. Most packaged versions of lxml will already contain
these dependencies.

When the environment variable USECPO is set to 1, the toolkit will attempt to
use libgettextpo from the gettext-tools package (it might have a slightly
different name on your distribution). This can greatly speed up access to PO
files, but has not yet been tested as extensively. Feedback is most welcome.

The package iniparse is necessary for ini2po and po2ini:
<https://pypi.org/project/iniparse/>

The python-Levenshtein package will improve performance for fuzzy matching if
it is available. This can improve the performance of pot2po, for example.  It
is optional and no functionality is lost if it is not installed, only speed.
<http://sourceforge.net/projects/translate/files/python-Levenshtein/>

Functions in the `lang.data` module can supply functions to translate language
names using the `pycountry` package. It can even translate names in the format
``Language (Country)`` such as ``English (South Africa)`` This is used by
Pootle and Virtaal. If the package is not installed, the language names will
simply appear in English. It is therefore recommended you install the
`pycountry` package.

The package vobject is needed for ical2po and po2ical.

The aeidon package (or gaupol if aeidon is not available) is needed for sub2po
and po2sub. Some Unicode encoded files (including most files from
<http://dotsub.com/>) require version 0.14 or later.
<http://home.gna.org/gaupol/>
Gaupol might need the 'Universal Encoding Detector'
<http://pypi.python.org/pypi/chardet>

Trados TXT TM support requires the BeautifulSoup parser
<http://www.crummy.com/software/BeautifulSoup/>

Markdown support requires the mistletoe parser
<https://github.com/miyuchina/mistletoe>

Program overview
----------------

Use ``--help`` to find the syntax and options for all programs.

* Converters::

        oo2po    - convert between OpenOffice.org GSI files and PO
        oo2xliff - convert between OpenOffice.org GSI files and XLIFF
        moz2po   - convert between Mozilla files and PO
        csv2po   - convert PO format to CSV for editing in a spreadsheet program
        php2po   - PHP localisable string arrays converter.
        ts2po    - convert Qt Linguist (.ts) files to PO
        txt2po   - convert simple text files to PO
        html2po  - convert HTML to PO (beta)
        md2po    - convert Markdown to PO
        xliff2po - XLIFF (XML Localisation Interchange File Format) converter
        prop2po  - convert Java .properties files to PO
        po2wordfast - Wordfast Translation Memory converter
        po2tmx   - TMX (Translation Memory Exchange) converter
        pot2po   - PO file initialiser
        csv2tbx  - Create TBX (TermBase eXchange) files from Comma Separated
                   Value (CSV) files
        ini2po   - convert .ini files to to PO
        ical2po  - Convert iCalendar files (*.ics) to PO
        sub2po   - Convert many subtitle files to PO
        resx2po  - convert .Net Resource (.resx) files to PO

* Tools (Quality Assurance)::

        pofilter - run any of the 40+ checks on your PO files
        pomerge  - merge corrected translations from pofilter back into
                   your existing PO files.
        poconflicts - identify conflicting use of terms
        porestructure - restructures po files according to poconflict directives
        pogrep   - find words in PO files

* Tools (Other)::

        pocompile - create a Gettext MO files from PO or XLIFF files
        pocount   - count translatable file formats (PO, XLIFF)
        podebug   - Create comment in your PO files' msgstr which can
                    then be used to quickly track down mistranslations
                    as the comments appear in the application.
        posegment - Break a PO or XLIFF files into sentence segments,
                    useful for creating a segmented translation memory.
        poswap    - uses a translation of another language that you
                    would rather use than English as source language
        poterminology - analyse PO or POT files to build a list of
                        frequently occurring words and phrases
