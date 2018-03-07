import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')


import passExam

class passExamTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(passExam.pass_exam(1), False)

    def test2(self):
        self.assertEqual(passExam.pass_exam(5), False)

    def test3(self):
        self.assertEqual(passExam.pass_exam(20), True)

    def test4(self):
        self.assertEqual(passExam.pass_exam(40), False)


if __name__ == '__main__':
    unittest.main()