# -*- coding: utf-8 -*-
#
# Stripped down sphinx config
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/stable/config

import os

# Define CURDIR
CURDIR = os.path.abspath(os.path.dirname(__file__))

# Pulls in ./prolog.txt and appends it to every rst file processed by sphinx in this repo
rst_prolog = open(os.path.join(CURDIR, 'prolog.txt'),'r').read() #.decode('utf8') # No need to decode in python3

# Pulls in ./epilog.txt and appends it to every rst file processed by sphinx in this repo
rst_epilog = open(os.path.join(CURDIR, 'epilog.txt'),'r').read() #.decode('utf8')

# Sanitize strings

def sanitize_strings(s):
    return str(s.strip().replace(" ",""))

# -- Project information -----------------------------------------------------

project = 'PROJECT NAME'
copyright = '2018, Ground Labs'
author = 'Ground Labs'
project_description = 'Short description'
category = 'Documentation'

# The short X.Y version
version = '1.0'
# The full version, including alpha/beta/rc tags
release = version+' beta'


# -- General configuration ---------------------------------------------------

extensions = [
    "sphinxcontrib.fulltoc",
    "sphinxprettysearchresults",
]

templates_path = ['_templates']

# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

language = None

exclude_patterns = []

pygments_style = 'emacs'

# -- Options for HTML output -------------------------------------------------

html_theme = 'basic'
# html_theme_path = ['_theme']
# html_theme_options = {}
html_static_path = ['_static'] #, '_theme/nsdmdh/_static']
html_sidebars = {'**':['searchbox.html','localtoc.html']}

# -- Options for HTMLHelp output ---------------------------------------------

htmlhelp_basename = sanitize_strings(project)


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    # 'preamble': '',
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, sanitize_strings(project)+'.tex', project,
     author, 'manual'),
]

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, sanitize_strings(project), project,
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, sanitize_strings(project), project,
     author, sanitize_strings(project), project_description,
     category),
]
