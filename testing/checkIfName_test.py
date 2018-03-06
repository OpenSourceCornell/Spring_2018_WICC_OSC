import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')


import checkIfName

class checkIfNameTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(checkIfName.check_if_name('David Gries'), True)

    def test2(self):
        self.assertEqual(checkIfName.check_if_name('Alex Greenberg'), True)

    def test2(self):
        self.assertEqual(checkIfName.check_if_name('JohnSmith'), False)


if __name__ == '__main__':
    unittest.main()
