# tests.py

import unittest
from functions.get_files_info import get_files_info

class TestAgent(unittest.TestCase):
    def test_get_file_info_current_dir(self):
        print("Result for current directory:")
        print(f'{get_files_info("calculator",".")}\n')

    def test_get_file_info_pkg(self):
        print("Result for 'pkg' directory:")
        print(f'{get_files_info("calculator","pkg")}\n')

    def test_get_file_info_bin(self):
        print("Result for '/bin' directory:")
        print(f'{get_files_info("calculator","/bin")}\n')

    def test_get_file_info_self(self):
        print("Result for '../' directory:")
        print(f'{get_files_info("calculator","../")}\n')

if __name__ == "__main__":
    unittest.main()