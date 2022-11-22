# *Security Engine*
__Name:__ *Nhan Hoang (A20490094)*                

__Hawk-Email:__ *nhoang4@hawk.iit.edu*

__This project is built in Python using__ [CS330_Programming_Project](http://www.cs.iit.edu/~virgil/cs330/mail.fall2022/pa.html) 
***
### Part 1:
- ***LockEngine*** is a class that contains all the methods that as a whole simulates that of an locking engine (Locked and Unlocked when passing in the correct series of digits)


**Main** replicates that of a controller engine (an infinite loop and will return the Lock's 'engine state' encountering a correct code).

### Part 2: 
- ***LockEngineTester*** does the same thing that the predecessor ***LockEngine*** does but returns instead of printing the Lock's state once find the Unlock or Lock Code. 

**Main** simulates a lock-cracker. It will try to crack the code and return the minimum and the maximum symbols generated as well as average cumulated symbols.  
```
  Note: The runtime for this implementation was way faster than anticipated(10~30s).
        The best record I gathered was 5 seconds to find the Unlocking key.
```
 
***
### Instruction for Testing:

1. Assuming the Code folder is unzipped.
2. cd into that Code folder.
3. Give run commands on your own.
```
          python3 Part1.py
          python3 Part2.py
          python3 Tests.py
```
There are multiple test cases:
1. Engine printed *Locked* after a lockCode input - Test Case #1
2. Engine printed *Unlocked* after a unlockCode input - Test Case #2
3. Engine stayed operational even after wrong input - Test case #3
4. Engine does not interact at all (passing in an empty string) - Test case #4

***
### MEMO:

 A memo describing what you have done, how you have done it, and your findings. 
 In the memo clearly state what is the language of the FA you have implemented. 
 Also indicate what is the regular expression corresponding to that language. 
 Attach the state transition diagram for the FA.

In this project, I have managed to successfully created a functional lock that will print out the state of the door as the code or password are being passed in. As the instruction said, I created two file Part1.py and Part2.py. The first one is to show the mechanism of a lock engine. The second file is used to crack the lock and also returns a average symbols produced while trying to unlock the engine as well as the minimum and the maximum symbols generated.

The language I applied for this project was in Python. Attached with this file is a FA state transition diagram. 

