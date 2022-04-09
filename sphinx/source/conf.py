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
import sys

sys.path.insert(0, os.path.abspath("../.."))

# -- Project information -----------------------------------------------------

project = "atpthings"
copyright = "2022, andrazpolak"
author = "andrazpolak"

# The full version, including alpha/beta/rc tags
release = "0.0.13"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "numpydoc",
    "sphinx.ext.autodoc",  # automatically construct the documentation.
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    # "sphinxext.github",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# GitHub extension

# github_project_url = "https://github.com/atp-things/pkg-python-util"
# -- Options for HTML output -------------------------------------------------

pygments_style = "sphinx"

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"
# html_theme = "alabaster"

# Logo
# html_logo = '_static/numpylogo.svg'
# html_favicon = '_static/favicon/favicon.ico'

# html_theme_options = {
#     "logo_link": "index",
#     "github_url": "https://github.com/atp-things/pkg-python-util",
#     "collapse_navigation": True,
# }

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


autosummary_generate = True

intersphinx_mapping = {
    "dateutil": ("https://dateutil.readthedocs.io/en/latest/", None),
    "matplotlib": ("https://matplotlib.org/stable/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "ipykernel": ("https://ipykernel.readthedocs.io/en/latest/", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable/", None),
    "pandas-gbq": ("https://pandas-gbq.readthedocs.io/en/latest/", None),
    "py": ("https://pylib.readthedocs.io/en/latest/", None),
    "python": ("https://docs.python.org/3/", None),
    "pytest": ("https://pytest.org/en/stable/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/reference/", None),
    "statsmodels": ("https://www.statsmodels.org/devel/", None),
    "pyarrow": ("https://arrow.apache.org/docs/", None),
}


# -----------------------------------------------------------------------------
# Source code links
# -----------------------------------------------------------------------------
# link_github = True
# # You can add build old with link_github = False

# if link_github:
#     import inspect
#     from packaging.version import parse

#     extensions.append('sphinx.ext.linkcode')

#     def linkcode_resolve(domain, info):
#         """
#         Determine the URL corresponding to Python object
#         """
#         if domain != 'py':
#             return None

#         modname = info['module']
#         fullname = info['fullname']

#         submod = sys.modules.get(modname)
#         if submod is None:
#             return None

#         obj = submod
#         for part in fullname.split('.'):
#             try:
#                 obj = getattr(obj, part)
#             except AttributeError:
#                 return None

#         if inspect.isfunction(obj):
#             obj = inspect.unwrap(obj)
#         try:
#             fn = inspect.getsourcefile(obj)
#         except TypeError:
#             fn = None
#         if not fn or fn.endswith('__init__.py'):
#             try:
#                 fn = inspect.getsourcefile(sys.modules[obj.__module__])
#             except (TypeError, AttributeError, KeyError):
#                 fn = None
#         if not fn:
#             return None

#         try:
#             source, lineno = inspect.getsourcelines(obj)
#         except (OSError, TypeError):
#             lineno = None

#         linespec = (f"#L{lineno:d}-L{lineno + len(source) - 1:d}"
#                     if lineno else "")

#         startdir = Path(matplotlib.__file__).parent.parent
#         fn = os.path.relpath(fn, start=startdir).replace(os.path.sep, '/')

#         if not fn.startswith(('matplotlib/', 'mpl_toolkits/')):
#             return None

#         version = parse(matplotlib.__version__)
#         tag = 'main' if version.is_devrelease else f'v{version.public}'
#         return ("https://github.com/matplotlib/matplotlib/blob"
#                 f"/{tag}/lib/{fn}{linespec}")
# else:
#     extensions.append('sphinx.ext.viewcode')
