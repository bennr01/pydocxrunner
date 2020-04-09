"""
Test cases for pydocxrunner.
"""
import os
import shutil
import subprocess
import tempfile
import unittest

import pydocxrunner


class PydocxrunnerTests(unittest.TestCase):
    """
    Tests for pydocxrunner.
    """
    def exec_in_tempdir(self, path):
        """
        Copy & execute target docx file in a temporary directory, then
        return the output. Fail if the execution fails.
        
        This will ensure that the original files are not modified.
        
        @param path: path to execute
        @type path: L{str}
        @return: the stdout output
        @rtype: L{str}
        """
        with tempfile.TemporaryDirectory() as tempdir:
            # get new path
            tf = os.path.join(tempdir, os.path.basename(path))
            # copy file
            shutil.copyfile(path, tf)
            # make executable
            pydocxrunner.make_executable(tf)
            # run
            return subprocess.check_output(
                ["python3", tf],
                universal_newlines=True,
                )
    
    def get_sibling_path(self, filename):
        """
        Return the path of the specified file in the same directory as
        this one.
        
        @param filename: name of sibling file
        @type filename: L{str}
        @return: the path of the specified file.
        @rtype: L{str}
        """
        dp = os.path.dirname(__file__)
        return os.path.join(dp, filename)
    
    def test_helloworld(self):
        """
        Test the helloworld.docx file.
        """
        path = self.get_sibling_path("helloworld.docx")
        output = self.exec_in_tempdir(path)
        self.assertIn("Hello, World!", output)
    
    def test_square_numbers(self):
        """
        Test the square_numbers.docx file.
        """
        path = self.get_sibling_path("square_numbers.docx")
        output = self.exec_in_tempdir(path)
        self.assertIn("0\n1\n4\n9\n16\n25\n36\n49\n64\n81", output)
