__author__ = "Owen Feehan"
__copyright__ = "Owen Feehan"
__license__ = "MIT"


def configure(app):

    # -- Project information -----------------------------------------------------

    app.config.project = "anchor_python_visualization"
    app.config.copyright = "2021, Owen Feehan"
    app.config.author = "Owen Feehan"

    # The short X.Y version
    app.config.version = "0.1"

    # The full version, including alpha/beta/rc tags
    app.config.release = "0.1"

    # -- General configuration ---------------------------------------------------

    # Add any Sphinx extension module names here, as strings. They can be
    # extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
    # ones.
    app.config.extensions = [
        "sphinx.ext.autodoc",
        "sphinx.ext.viewcode",
        "sphinx.ext.todo",
        "sphinx.ext.intersphinx",
        "autoapi.extension",
    ]

    # See https://sphinx-autoapi.readthedocs.io/en/latest/reference/config.html#advanced-options
    app.config.autoapi_type = "python"
    app.config.autoapi_dirs = ["../src"]
    app.config.autoapi_options = [
        "members",
        "undoc-members",
        "show-inheritance",
        "show-module-summary",
        "imported-members",
    ]
    app.config.autoapi_ignore = ["*docs/*", "*test/*", "build/*"]

    app.config.intersphinx_mapping = {
        "python": ("https://docs.python.org/3", None),
        "pandas": ("http://pandas.pydata.org/pandas-docs/dev", None),
        "numpy": ("https://numpy.org/doc/stable/", None),
        "matplotlib": ("https://matplotlib.org", None),
        "plotly": ("https://plotly.com/python-api-reference/", None),
    }

    # Add any paths that contain templates here, relative to this directory.
    app.config.templates_path = ["_templates"]

    # The language for content autogenerated by Sphinx. Refer to documentation
    # for a list of supported languages.
    #
    # This is also used if you do content translation via gettext catalogs.
    # Usually you set "language" from the command line for these cases.
    app.config.language = "en"

    # List of patterns, relative to source directory, that match files and
    # directories to ignore when looking for source files.
    # This pattern also affects html_static_path and html_extra_path.
    app.config.exclude_patterns = [
        "_build",
        "Thumbs.db",
        ".DS_Store",
        "**/build",
        "**/docs",
    ]

    # -- Options for HTML output -------------------------------------------------

    # The theme to use for HTML and HTML Help pages.  See the documentation for
    # a list of builtin themes.
    #
    app.config.html_theme = "classic"

    # Makes the docs occupy as much width as possible in the browser screen.
    app.config.html_theme_options = {"sidebarwidth": "15%", "body_max_width": "80%"}

    # Add any paths that contain custom static files (such as style sheets) here,
    # relative to this directory. They are copied after the builtin static files,
    # so a file named "default.css" will overwrite the builtin "default.css".
    app.config.html_static_path = ["_static"]

    # -- Extension configuration -------------------------------------------------

    # -- Options for todo extension ----------------------------------------------

    # If true, `todo` and `todoList` produce output, else they produce nothing.
    app.config.todo_include_todos = True
