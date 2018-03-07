import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')


import terraceOrTrillium

class TerraceOrTrillium(unittest.TestCase):
    def test1(self):
        self.assertEqual(terraceOrTrillium.terrace_or_trillium(True, True, True), 'Terrace')

    def test2(self):
        self.assertEqual(terraceOrTrillium.terrace_or_trillium(True, True, False), 'Terrace')

    def test3(self):
        self.assertEqual(terraceOrTrillium.terrace_or_trillium(True, False, True), 'Terrace')

    def test4(self):
        self.assertEqual(terraceOrTrillium.terrace_or_trillium(True, False, False), 'Trillium')

    def test5(self):
        self.assertEqual(terraceOrTrillium.terrace_or_trillium(False, True, True), 'Terrace')

    def test6(self):
        self.assertEqual(terraceOrTrillium.terrace_or_trillium(False, True, False), 'Trillium')

    def test7(self):
        self.assertEqual(terraceOrTrillium.terrace_or_trillium(False, False, True), 'Terrace')

    def test8(self):
        self.assertEqual(terraceOrTrillium.terrace_or_trillium(False, False, False), 'Trillium')

if __name__ == '__main__':
    unittest.main()