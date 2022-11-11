def keyController(inputStr):
    lockCode = '900944'
    unlockCode = '900941'

    for i in range(len(inputStr)):
        if inputStr[i] == lockCode[0]:
            nextNinput = inputStr[i:i + (len(lockCode))]

            if nextNinput == lockCode:
                print('Lock')
            elif nextNinput == unlockCode:
                print('Unlock')

def singularChecker(inputStr):
    lockCode = '900944'
    unlockCode = '900941'

    for i in range(len(inputStr)):
        if inputStr[i] == lockCode[0]:
            nextNinput = inputStr[i:i + (len(lockCode))]

            if nextNinput == lockCode:
                return ['Lock', lockCode]
            elif nextNinput == unlockCode:
                return ['Unlock', unlockCode]

if __name__ == '__main__':
    keyController('913520334412451033444123970001112334451334410101')