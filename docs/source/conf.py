import datetime
import os
import sys

import xwrf


cwd = os.getcwd()
parent = os.path.dirname(cwd)
sys.path.insert(0, parent)


# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    # 'IPython.sphinxext.ipython_console_highlighting',
    # 'IPython.sphinxext.ipython_directive',
    'sphinx.ext.napoleon',
    'myst_parser',
    'sphinxext.opengraph',
    'sphinx_copybutton',
    'sphinx_comments',
    'sphinxcontrib.autodoc_pydantic',
]

autodoc_member_order = 'groupwise'

# MyST config
myst_enable_extensions = ['amsmath', 'colon_fence', 'deflist', 'html_image']
myst_url_schemes = ['http', 'https', 'mailto']

comments_config = {
    'utterances': {'repo': 'NCAR/xwrf', 'optional': 'config', 'label': '💬 comment'},
    'hypothesis': False,
}

# sphinx-copybutton configurations
copybutton_prompt_text = r'>>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: '
copybutton_prompt_is_regexp = True

extlinks = {
    'issue': ('https://github.com/NCAR/xwrf/issues/%s', 'GH#'),
    'pr': ('https://github.com/NCAR/xwrf/pull/%s', 'GH#'),
}
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# Autosummary pages will be generated by sphinx-autogen instead of sphinx-build
autosummary_generate = []
autodoc_typehints = 'none'

# Napoleon configurations

napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_use_param = False
napoleon_use_rtype = False
napoleon_preprocess_types = False

autodoc_pydantic_model_show_json = True
autodoc_pydantic_settings_show_json = False


# The suffix of source filenames.
# source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
current_year = datetime.datetime.now().year
project = 'xwrf'
copyright = f'2020-{current_year}, xwrf development team'
author = 'xwrf developers'


# The short X.Y version.
version = xwrf.__version__.split('+')[0]
# The full version, including alpha/beta/rc tags.
release = xwrf.__version__


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', '**.ipynb_checkpoints', 'Thumbs.db', '.DS_Store']


# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'furo'
html_title = ''

html_context = {
    'github_user': 'NCAR',
    'github_repo': 'xwrf',
    'github_version': 'main',
    'doc_path': 'docs',
}
html_static_path = ["_static"]
html_theme_options = dict(
    # analytics_id=''  this is configured in rtfd.io
    # canonical_url="",
    light_logo="xwrf_logo_bg_light.svg",
    dark_logo="xwrf_logo_bg_dark.svg",
    sidebar_hide_name=True
)
html_favicon = "_static/xwrf_favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['../_static']

# Sometimes the savefig directory doesn't exist and needs to be created
# https://github.com/ipython/ipython/issues/8733
# becomes obsolete when we can pin ipython>=5.2; see ci/requirements/doc.yml
# ipython_savefig_dir = os.path.join(
#     os.path.dirname(os.path.abspath(__file__)), '_build', 'html', '_static'
# )

# savefig_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'source', '_static')

# os.makedirs(ipython_savefig_dir, exist_ok=True)
# os.makedirs(savefig_dir, exist_ok=True)

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'


# Output file base name for HTML help builder.
htmlhelp_basename = 'xwrfdoc'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
}


latex_documents = [('index', 'xwrf.tex', 'xwrf Documentation', author, 'manual')]

man_pages = [('index', 'xwrf', 'xwrf Documentation', [author], 1)]

texinfo_documents = [
    (
        'index',
        'xwrf',
        'xwrf Documentation',
        author,
        'xwrf',
        'One line description of project.',
        'Miscellaneous',
    )
]

ipython_warning_is_error = False
ipython_execlines = []


intersphinx_mapping = {}
