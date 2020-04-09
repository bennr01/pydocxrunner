"""
Setup file for pydocxrunner
"""
from setuptools import setup


setup(
    name="pydocxrunner",
    version="0.0.2",
    description="Make .docx files executable for the python interpreter",
    long_description=open('README.md', "r").read(),
    long_description_content_type="text/markdown",
    keywords="docx executable",
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
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Utilities",
    ],
)
