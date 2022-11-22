import Part2
import unittest
lockCode = '900944'
unlockCode = '900941'

class TestStringMethods(unittest.TestCase):
    def testCase1(self):
        device = Part2.LockEngineTester()
        for i in range(len(lockCode)):
            if i == len(lockCode) - 1:
                self.assertEqual(device.padLock(lockCode[i]), 'Locked')
            else:
                device.padLock(lockCode[i])

    def testCase2(self):
        device = Part2.LockEngineTester()
        for i in range(len(unlockCode)):
            if i == len(unlockCode) - 1:
                self.assertEqual(device.padLock(unlockCode[i]), 'Unlocked')
            else:
                device.padLock(unlockCode[i])

    def testCase3(self):
        randomCode = '1245668g900944'
        device = Part2.LockEngineTester()
        for i in range(len(randomCode)):
            if i == len(randomCode) - 1:
                self.assertEqual(device.padLock(randomCode[i]), 'Locked')
            else:
                device.padLock(randomCode[i])

    def testCase4(self):
        emptyCode = ''
        device = Part2.LockEngineTester()
        self.assertEqual(device.padLock(emptyCode), None)

if __name__ == '__main__':
    unittest.main()