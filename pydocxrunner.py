# -*- coding: utf-8 -*-
"""
pydocxrunner - make docx files executable.
"""
import argparse
import urllib.request
import zipfile


__author__ = "bennr01"


SCRIPT = """# -*- coding: utf-8 -*-
'''
This script executes the content of this docx file.
'''
import os
import docx2txt


def get_content():
    '''
    Return the content of the docx file.
    
    @return: the content of the docx file this file is contained in
    @rtype: L{str}
    '''
    path = os.path.dirname(__file__)
    return docx2txt.process(path)


def execute(content):
    '''
    Execute the file content.
    '''
    exec(content)


def main():
    '''
    The main function.
    '''
    content = get_content()
    execute(content)


if __name__ == "__main__":
    main()
"""

DOCX2TXT_URL = "https://raw.githubusercontent.com/ankushshah89/python-docx2txt/master/docx2txt/docx2txt.py"


def make_executable(path):
    """
    Make a .docx file executable.
    
    @param path: path to file which should be made executable
    @type path: L{str}
    """
    with zipfile.ZipFile(path, "a") as zf:
        add_dependencies_to_zipfile(zf)
        #with zf.open("__main__.py", "w") as fout:
        #    fout.write(SCRIPT.encode("utf-8"))
        zf.writestr("__main__.py", SCRIPT)


def add_dependencies_to_zipfile(zf):
    """
    Write the dependencies to the given zipfile.
    
    @param zf: zipfile to write to
    @type zf: L{zipfile.ZipFile}
    """
    # install python-docx2txt
    response = urllib.request.urlopen(DOCX2TXT_URL)
    content = response.read()
    zf.writestr("docx2txt.py", content)
    


def main():
    """
    The main function.
    """
    parser = argparse.ArgumentParser(description="Make .docx files executable by the python interpeter")
    parser.add_argument("path", help="file to make executable")
    ns = parser.parse_args()
    
    make_executable(ns.path)


if __name__ == "__main__":
    main()
