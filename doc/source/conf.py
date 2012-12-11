#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
##
## This file is part of Sardana
## 
## http://www.tango-controls.org/static/sardana/latest/doc/html/index.html
##
## Copyright 2011 CELLS / ALBA Synchrotron, Bellaterra, Spain
## 
## Sardana is free software: you can redistribute it and/or modify
## it under the terms of the GNU Lesser General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
## 
## Sardana is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU Lesser General Public License for more details.
## 
## You should have received a copy of the GNU Lesser General Public License
## along with Sardana.  If not, see <http://www.gnu.org/licenses/>.
##
##############################################################################

import sys
import os

def set_src():
    import sys
    import os.path as osp
    sar_dir = osp.join(osp.dirname(osp.abspath(__file__)), osp.pardir, osp.pardir, 'src')
    sys.path.insert(0, osp.abspath(sar_dir))

# try to use code from src distribution
set_src()
import sardana

as_pdf_extension = True
try:
    import rst2pdf.pdfbuilder
except ImportError:
    as_pdf_extension = False
    
def fix_sardana_for_doc():
    
    def type_getattr(self, name):
        if name not in self._pending_type_names:
            self._pending_type_names[name] = name
        return self._pending_type_names[name]
    
    import sardana.macroserver.msparameter
    sardana.macroserver.msparameter.TypeNames.__getattr__ = type_getattr

fix_sardana_for_doc()

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.append(os.path.abspath('sphinxext'))

# -- General configuration -----------------------------------------------------

#autosummary_generate = True

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.pngmath',
              'sphinx.ext.autosummary',
              'sphinx.ext.autodoc',
              'sphinx.ext.doctest',
              'sphinx.ext.graphviz',
              'sphinx.ext.inheritance_diagram',
              'sphinx.ext.intersphinx',
              'sphinx.ext.todo',
              'sphinx.ext.viewcode',
              'sardanaextension',
              'ipython_console_highlighting',
              'spock_console_highlighting',
]

if as_pdf_extension:
    extensions.append('rst2pdf.pdfbuilder')
    
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'contents'

# General information about the project.
project = u'sardana'
copyright = u'2012, ALBA - CELLS, Creative Commons Attribution-Share Alike 3.0'
copyright = u"""Except where otherwise noted, content on this site is
licensed under a Creative Commons Attribution 3.0 License"""

#Ideally we would like to put the following html code for copyright... but how?
'''<a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/es/"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-sa/3.0/es/88x31.png" /></a><br /><span xmlns:dc="http://purl.org/dc/elements/1.1/" href="http://purl.org/dc/dcmitype/Text" property="dc:title" rel="dc:type">Taurus Documentation</span> by <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">CELLS - ALBA</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/es/">Creative Commons Attribution-Share Alike 3.0 Spain License</a>.'''

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '.'.join(sardana.Release.version.split('.')[:2])
# The full version, including alpha/beta/rc tags.
release = sardana.Release.version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = []

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = False

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'
pygments_style = 'spock_console_highlighting.SpockStyle'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
html_theme = 'default'
#html_theme = 'sphinxdoc'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = []
#html_theme_path = ['themes']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "logo.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {'index': ['indexsidebar.html']}

# Additional templates that should be rendered to pages, maps page names to
# template names.
html_additional_pages = { 'index' : 'index.html' }

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'sardanadoc'


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
latex_paper_size = 'a4'

# The font size ('10pt', '11pt' or '12pt').
latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('contents', 'sardana.tex', u'Sardana Documentation',
   u'Sardana team', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = '_static/sardana_screenshot.png'

latex_elements = {
    'fontpkg': '\\usepackage{palatino}',
}
latex_show_urls = 'footnote'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True

todo_include_todos = True

autodoc_member_order = "bysource"

# -- Options for Graphviz  -----------------------------------------------------

inheritance_node_attrs = dict(shape='box', fontcolor='black', 
                              height=0.4,
                              color='brown', style='rounded')

inheritance_graph_attrs = dict(rankdir="UD", ratio='compress')

graphviz_output_format = 'png' # 'svg'

#inheritance_graph_attrs = dict(rankdir="LR", size='"6.0, 8.0"',
#                               fontsize=14, ratio='compress')

# -- Options for reference to other documentation ------------------------------

intersphinx_mapping = {
    'http://docs.python.org/dev': None,
    'http://docs.scipy.org/doc/scipy/reference' : None,
    'http://docs.scipy.org/doc/numpy' : None,
    'http://ipython.org/ipython-doc/stable/' : None,
    'http://www.tango-controls.org/static/PyTango/latest/doc/html' : None,
    'http://www.tango-controls.org/static/taurus/latest/doc/html' : None,
    'http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/html' : None,
    'http://matplotlib.sourceforge.net/' : None,
    'http://packages.python.org/guiqwt/' : None,
}

