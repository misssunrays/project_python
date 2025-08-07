import random
# ask the user to play or not
while(True):
    choice=input("roll the dice or not?(y/n)").lower()
    if choice=='y':
        num1= random.randint(1,6)
        num2= random.randint(1,6)
        print(f'({num1},{num2})')
    elif choice=='n':
        print("--Thank You for playing--") 
        break
        
    else:
        print("INVALID CHOICE")
           




# if yes then, 
# generate a random number
# print it
# else
# terminate
# or
# exit
