import os
from random import randint
import time

# step 1: take password from user
pas = input("send the password: ")

# step 2: define all possible characters
keys = [
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
    "A", "a", "B", "b", "C", "c", "D", "d", "E", "e",
    "F", "f", "G", "g", "H", "h", "I", "i", "J", "j",
    "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", 
    "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t",
    "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y",
    "Z", "z", "-", "/", ":", ";", 
    "(", ")", "$", "&", "@", ".", ",", "?", "!", "'",
    "[", "]", "{", "}", "#", "%", "^", "*", "+", "=",
    "_", "\", "|", "~", "<", ">", "€", "£", "¥", "•", 
]

# step 3: initialize variables
pwg = ""
attempts = 0
start_time = time.time()

# step 4: keep guessing until password matches
while pwg != pas:
    pwg = ""
    attempts += 1

    # step 5: generate random password of same length
    for i in range(len(pas)):
        guessPass = keys[randint(0, 4)]
        pwg = str(guessPass) + str(pwg)
        print(pwg)
        print("attacking... please wait!")
        os.system("cls")

# step 6: calculate total time
end_time = time.time()
total_time = end_time - start_time

# step 7: show final result
print(f"The pass is: {pwg}")
print(f"Total Attempts: {attempts}")
print(f"Time Taken: {total_time:.2f} seconds")
