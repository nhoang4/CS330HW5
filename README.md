# *Security Engine*
__Name:__ *Nhan Hoang (A20490094)*                

__Hawk-email:__ *nhoang4@hawk.iit.edu*

__This project was built using__ [CS330_Programming_Project](http://www.cs.iit.edu/~virgil/cs330/mail.fall2022/pa.html) 
***
### Part 1:
- ***keyController*** is for the string of password to be passed in and the locking engine will return the state of the lock if found the unlocked or locked key.

**Main** replicate that of a controller engine (an infinite loop until encounter a correct code).

### Part 2: 
- ***singularChecker*** does the same thing that the predecessor ***keyController*** does but break once find the Unlock or Lock Code. 

**Main** simulates a lock-cracker. It will show how much time it will be taking to find the Unlock or Lock code and will also show how many symbols that have been randomly generated until the founded Code.
***
### Instruction for Testing:

1. Assuming the Code folder is unzipped
2. cd into that Code folder
3. Give run commands on your own

          python3 Part1.py
          python3 Part2.py

There are 2 test cases:
1. Engine remains Locked after a Code input - Test Case #1
2. Engine Unlocked and trigger *'Door Unlocked'* after Code Input - Test Case #2

