# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Dedalus Project'
copyright = '2022 Dedalus Collaboration'
author = 'Dedalus Collaboration'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = ''


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = []
extensions += ['sphinx.ext.mathjax']
extensions += ['autoapi.extension']
extensions += ['sphinx.ext.viewcode']
extensions += ['sphinx.ext.napoleon']
extensions += ['sphinx.ext.extlinks']
extensions += ['nbsphinx']
extensions += ['sphinx_rtd_theme']
extensions += ['sphinx_gallery.load_style']
extensions += ['sphinxcontrib.video']

add_module_names = False
autoapi_dirs = ['../dedalus']
autoapi_ignore = ['*/dedalus/tests/*', '*/dedalus/libraries/dedalus_sphere/*']
autoapi_options = ['members', 'undoc-members']
autoapi_member_order = 'groupwise'
autoapi_python_class_content = 'both'
autoapi_add_toctree_entry = False

napoleon_use_param = False
napoleon_use_keyword = False
napoleon_use_ivar = True

extlinks = {'repo': ('https://github.com/DedalusProject/dedalus/tree/master/%s', None)}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'default'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_logo = 'epic12_4_exp_2_1.25.png'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    "collapse_navigation": "false"
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'DedalusProjectdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'DedalusProject.tex', 'Dedalus Project Documentation',
     'Dedalus Collaboration', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'dedalusproject', 'Dedalus Project Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'DedalusProject', 'Dedalus Project Documentation',
     author, 'DedalusProject', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for nbsphinx galleries
# Using _images/ is a hack to get relocated images which have been included in the pages
nbsphinx_thumbnails = {
    'pages/examples/evp_1d_waves_on_a_string': '_images/waves_on_a_string.png',
    'pages/examples/evp_1d_mathieu': '_images/mathieu_eigenvalues.png',
    'pages/examples/evp_disk_pipe_flow': '_images/pipe_flow.png',
    'pages/examples/ivp_1d_kdv_burgers': '_images/kdv_burgers.png',
    'pages/examples/ivp_2d_rayleigh_benard': '_images/rayleigh_benard.png',
    'pages/examples/ivp_2d_shear_flow': '_images/shear_flow.png',
    'pages/examples/ivp_ball_internally_heated_convection': '_images/internally_heated_convection.png',
    'pages/examples/ivp_disk_libration': '_images/libration.png',
    'pages/examples/ivp_shell_convection': '_images/shell_convection.png',
    'pages/examples/ivp_sphere_shallow_water': '_images/shallow_water.png',
    'pages/examples/lbvp_2d_poisson': '_images/poisson.png',
    'pages/examples/nlbvp_ball_lane_emden': '_images/lane_emden.png',
}
