# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# Workaround for sphinxcontrib.googleanalytics
import sphinx.application
import sphinx.errors
sphinx.application.ExtensionError = sphinx.errors.ExtensionError

# -- Project information -----------------------------------------------------

project = 'Applied Language Technology'
copyright = '2020- Tuomo Hiippala, CC BY-NC 4.0'
# author = 'Tuomo Hiippala'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['myst_nb', 'sphinxembeddedvideos.youtube', 'sphinxcontrib.googleanalytics']

# Use sphinx to parse RST; myst-nb for notebooks
source_suffix = {
    '.rst': 'restructuredtext',
    '.ipynb': 'myst-nb',
    '.myst': 'myst-nb',
}

# Configure Google Analytics
googleanalytics_id = "G-QDXYHY09XJ"
googleanalytics_enabled = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['README.md']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_book_theme"
html_title = ""
html_logo = "../img/logo.png"

html_theme_options = {
	"use_download_button": True,
	"use_repository_button": True,
	"use_edit_page_button": False,
	"repository_url": "https://github.com/Applied-Language-Technology/website/",
	"path_to_docs": "source/",
	"repository_branch": "master",
	"launch_buttons": {"binderhub_url": "https://mybinder.org",
					    "notebook_interface": "jupyterlab"}
	}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Set nbsphinx options
jupyter_execute_notebooks = "force"
