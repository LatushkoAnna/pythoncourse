import shutil
import unittest
import os


def func(path):
    os.makedirs(path)
    file_name = path + '/test_file.txt'
    with open(file_name, 'w') as f:
        f.write('test')


class PathTest(unittest.TestCase):
    def setUp(self):
        func('C:/Users/USER/OneDrive/Рабочий стол/folder_name')

    def test_text(self):
        with open('C:/Users/USER/OneDrive/Рабочий стол/folder_name/test_file.txt', 'r') as f:
            text = f.read()
        self.assertEqual(text, 'test')

    def tearDown(self):
        shutil.rmtree('C:/Users/USER/OneDrive/Рабочий стол/folder_name')


if __name__ == '__main__':
    unittest.main()
