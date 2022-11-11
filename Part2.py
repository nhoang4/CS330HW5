from Part1 import singularChecker
from random import randrange
import time

code = ''
isTrue = True
count = 0

startTime = time.time()

while isTrue:
    code += str(randrange(10))
    count += 1

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