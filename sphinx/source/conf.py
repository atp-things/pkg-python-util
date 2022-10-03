# Configuration file for the Sphinx documentation builder.
import os
import sys

sys.path.insert(0, os.path.abspath("../../src/"))
import atpthings

# -- Project information -----------------------------------------------------

project = "atpthings"
copyright = "2022, andrazpolak"
author = "andrazpolak"

version = atpthings.__version__
release = str(version)
print(f"Building Documentation for atpthings: {atpthings.__version__}")
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
    "sphinx_copybutton",
    "myst_parser",
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

# The theme
html_theme = "pydata_sphinx_theme"
# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False
html_static_path = ["_static"]
html_theme_options = {
    "logo": {
        "text": "ATP-Things PyPkg",
    },
    "github_url": "https://github.com/atp-things/pkg-python-util",
    "collapse_navigation": True,
    "external_links": [
        {
            "name": "PYPI",
            "url": "https://pypi.org/project/atpthings/",
        },
        {
            "name": "Conda",
            "url": "https://anaconda.org/andrazpolak/atpthings",
        },
        {
            "name": "ATP-Things",
            "url": "https://atp-things.github.io",
        },
    ],
    "navbar_end": ["version-switcher", "theme-switcher", "navbar-icon-links"],
    "switcher": {
        "json_url": "/versions.json",
        "version_match": version,
    },
}
html_logo = "./_static/logo-square.svg"
html_favicon = "./_static/logo-square.svg"
html_context = {"default_mode": "light"}

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

source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}
