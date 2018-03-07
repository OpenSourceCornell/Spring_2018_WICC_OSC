import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')


import checkIfPhoneNumber

class checkIfPhoneNumberTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(checkIfPhoneNumber.check_if_phone_number('201-400-2019'), True)

    def test2(self):
        self.assertEqual(checkIfPhoneNumber.check_if_phone_number('212-303-32324'), False)

    def test2(self):
        self.assertEqual(checkIfPhoneNumber.check_if_phone_number('323:323:2323'), False)


if __name__ == '__main__':
    unittest.main()
