import random
class LockEngineTester:
    def __init__(self):
        self.state = 0
        self.LOCK_STATE = 7
        self.UNLOCK_STATE = 6
    def padLock(self, input):
        try:
            input = int(input)
            if input < 0:
                 input = -input

            if self.state == 0:
                if input == 9:
                    self.state += 1
                else:
                    self.state = 0

            elif self.state == 1:
                if input == 0:
                    self.state += 1
                elif input == 9:
                    self.state = 1
                else:
                    self.state = 0

            elif self.state == 2:
                if input == 0:
                    self.state += 1
                elif input == 9:
                    self.state = 1
                else:
                    self.state = 0

            elif self.state == 3:
                if input == 9:
                    self.state += 1
                else:
                    self.state = 0

            elif self.state == 4:
                if input == 4:
                    self.state += 1
                elif input == 0:
                    self.state = 2
                elif input == 9:
                    self.state = 1
                else:
                    self.state = 0

            elif self.state == 5:
                if input == 1:
                    self.state = self.UNLOCK_STATE
                    return 'Unlocked'
                elif input == 4:
                    self.state = self.LOCK_STATE
                    return 'Locked'
                elif input == 9:
                    self.state = 1
                else:
                    self.state = 0

            elif self.state == self.UNLOCK_STATE or self.state == self.LOCK_STATE:
                if input == 9:
                    self.state = 1
                else:

                    self.state = 0
        except:
            self.state = 0


def guess_passcode():
    device = LockEngineTester()
    count = 0
    while device.state != device.UNLOCK_STATE:
        ranNum = random.randint(0, 9)
        device.padLock(ranNum)
        count += 1
    return count

def AverageCounter(trials):
    total=0
    minimum = maximum = guess_passcode()
    lst = []
    for i in range(trials - 1):
        count = guess_passcode()
        total += count
        lst.append(count)
    return [min(lst), max(lst), total//trials]

if __name__ == '__main__':
    lst1=AverageCounter(10)
    print('Minimum symbols: ' + str(lst1[0]))
    print('Maximum symbols: ' + str(lst1[1]))
    print('Average symbols: ' + str(lst1[2]))
