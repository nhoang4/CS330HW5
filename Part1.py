def keyController(inputStr):
    lockCode = '900944'
    unlockCode = '900941'
    val=''
    for i in range(len(inputStr)):
        if inputStr[i] == lockCode[0]:
            nextNinput = inputStr[i:i + (len(lockCode))]

            if nextNinput == lockCode:
                print('Locked at position: '+ str(i + 1))
                val = ('Lock')
            elif nextNinput == unlockCode:
                print('Unlocked at position: ' + str(i + 1))
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
            print ('Door Locked.' +'\n')

