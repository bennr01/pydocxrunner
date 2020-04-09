"""
Setup file for pydocxrunner
"""
from distutils.core import setup


setup(
    name="pydocxrunner",
    version="0.0.1",
    description="Make .docx files executable for the python interpreter",
    long_description=open('README.md', "r").read(),
    author="bennr01",
    url="https://github.com/bennr01/pydocxrunner",
    extras_require={
        "testing": [
            "tox",
        ],
    },
    py_modules=[
        "pydocxrunner",
        ],
    entry_points={
        "console_scripts": [
            "pydocxrunner = pydocxrunner:main",
        ],
    },
)
