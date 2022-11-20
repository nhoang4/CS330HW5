
from random import randrange
import time

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
    code = ''
    isTrue = True
    startTime = time.time()

    while isTrue:
        code += str(randrange(10))
        checkResult = singularChecker(code)

        if checkResult is not None:
            if checkResult[0] == 'Unlock':
                print(f'Unlock took: {round(time.time() - startTime)}')
                print(f'Unlock code: {checkResult[1]}')
                print(f'N symbols generated: {len(code)}')
                break
            elif checkResult[0] == 'Lock':
                print(f'Lock took: {round(time.time() - startTime)}')
                print(f'Lock code: {checkResult[1]}')
                print(f'N symbols generated: {len(code)}')
                break