import random
class LockEngine:
    #unlockCode = 900941
    #lockCode = 900944
    def __init__(self):
        self.state = 0
        self.LOCK_STATE = 7
        self.UNLOCK_STATE = 6

    def printer(self):
        if self.state== self.LOCK_STATE:
            print('Locked')
        elif self.state== self.UNLOCK_STATE:
            print('Unlocked')

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
                    self.printer()

                elif input == 4:
                    self.state = self.LOCK_STATE
                    self.printer()

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


if __name__ == '__main__':
    device = LockEngine()
    while True:
        INP = input()
        device.padLock(INP)