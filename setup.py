from setuptools import setup, find_packages

setup(
    name="jurisai",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
    ],
    extras_require={
        "docs": [
            "jupyter-book>=0.13.0",
            "sphinx>=4.0",
            "sphinx_rtd_theme",
            "doc8",
            "pydocstyle",
            "myst-parser",
            "sphinx-autodoc-typehints",
            "sphinx_copybutton",
            "nbsphinx",
            "sphinx-togglebutton",
        ],
    }
) 