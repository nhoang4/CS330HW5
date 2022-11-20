# import unittest
from Part1 import keyController
#
#
# class MyTestCase(unittest.TestCase):
#     def TestCase1(self)
#         self.assertEqual(keyController('900941'), 'Unlocked at position: 1' + '\n' + 'Door Unlocked')
#
# if __name__ == '__main__':
#     unittest.main()

import unittest

class TestStringMethods(unittest.TestCase):

    def testCase1(self):
        self.assertEqual(keyController('900941'), 'Unlock')

    def testCase2(self):
        self.assertEqual(keyController('900944'), 'Lock')

    def testCase3(self):
        self.assertEqual(keyController('900941909240859489009339328059284900944835701495900941'), 'Unlock')

if __name__ == '__main__':
    unittest.main()