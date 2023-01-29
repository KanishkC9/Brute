import time;
from datetime import datetime



def bruteforce():
    inputString = "abcdefghijklmnopqrstuvwxyz"
    inputNum = "1234567890"
    length = 4 ## variable length
    start = datetime.now().timestamp()
    global finish
    def recursePassword(input, passLength , currentPass, passwordToGuess):
        global passwordGuessed
        global finish
        if(passLength == length):
            print(currentPass)
            if(currentPass == passwordToGuess):
                end = datetime.now().timestamp()
                finish = end - start
                return True
            return False
        for char in input: 
           found =  recursePassword(input,passLength + 1, currentPass + char, passwordToGuess)
           if(found):
                return True

        
    yourPass = "daad" # change input strinf accordingly
    recursePassword(inputString,0,"",yourPass)
    print("Your Passcode ", yourPass ," was guessed in " ,(finish) , 'seconds')



bruteforce()