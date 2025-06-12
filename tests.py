# tests.py

import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

class TestAgent(unittest.TestCase):
    def test_get_file_contents_lorem(self):
        print("Result for main.py:")
        print(f'{write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")}\n')

    def test_get_file_contents_morelorem(self):
        print("Result for main.py:")
        print(f'{write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")}\n')

    def test_get_file_contents_temp(self):
        print("Result for main.py:")
        print(f'{write_file("calculator", "/tmp/temp.txt", "this should not be allowed")}\n')

    """def test_get_file_contents_main(self):
        print("Result for main.py:")
        print(f'{get_file_content("calculator", "main.py")}\n')

    def test_get_file_contents_calculator(self):
        print("Result for pkg/calculator.py:")
        print(f'{get_file_content("calculator", "pkg/calculator.py")}\n')

    def test_get_file_contents_cat(self):
        print("Result for /bin/cat:")
        print(f'{get_file_content("calculator", "/bin/cat")}\n')

    def test_get_file_contents_lorem(self):
        print("Result for lorem.txt:")
        print(f'{get_file_content("calculator", "lorem.txt")}\n')

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
        print(f'{get_files_info("calculator","../")}\n') """


if __name__ == "__main__":
    unittest.main()