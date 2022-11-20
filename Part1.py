def keyController(inputStr):
    lockCode = '900944'
    unlockCode = '900941'

    for i in range(len(inputStr)):
        if inputStr[i] == lockCode[0]:
            nextNinput = inputStr[i:i + (len(lockCode))]

            if nextNinput == lockCode:
                val = ('Lock')
            elif nextNinput == unlockCode:
                val = ('Unlock')
    return val

if __name__ == '__main__':
    isTrue = True
    while (isTrue):
        code = input('Enter your code: ')
        if keyController(code)=='Unlock':
            print('Door Unlocked.')
            break
        else:
            print ('Incorrect Code.')
