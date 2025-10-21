import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.abspath('..'))

# Project information
project = 'Scopix'
copyright = '2024, Mustafa Omar'
author = 'Mustafa Omar'
release = '0.1.0'

# General configuration
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# HTML output
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']