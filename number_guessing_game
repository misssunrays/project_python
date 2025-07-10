# generate a random number
# make a guess
# if not a valid num 
# print error
# if num entered <actual num
# print low
# if num entered>actual num
# print high
# if num entered=actual num
# print congrats message

import random

actual_num=random.randint(0,100)
while(True):
    try:
      num=int(input("enter your Guess (between 1 to 100): "))
      if num<actual_num:
            print("low")
      elif num>actual_num:
            print("high")
      elif num==actual_num:
            print("You guessed it right. The number is ",actual_num)
            break
            
    except ValueError:
        print("--PLEASE ENTER A VALID VALUE--")    

    
    #here python tries to convert any string or float if inputed like a 
    #or 3.5 then it cannot and throws a value error. which is why except block
    #is used that responds to this kind of error.

    
           
  