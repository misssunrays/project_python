#rock paper scissor
#algorithm
# ask from the User if they want r p s
#generate random choices
#compare with input
#win or lose or tie
import random
#instead of putting each r s and p we use tuple so that an unchangable
#list is created and we can access items from there.
choices_opt=("r","p","s")
#here we have done similar approach creating dictionary.
#emoji shrtut=win+.
emoji={
    'r':" 🪨",
    'p':"📃",
    's':"✂️"
}

while(True):
    user_choice=input("Enter you choice(r/p/s)").lower()
    if user_choice not in choices_opt:
        print("Invalid choice!")
    computer_choice=random.choice(choices_opt)
    print(f'you chose{emoji[user_choice]}')
    print(f'computer chose{emoji[computer_choice]}')
    #win lose condition
    if user_choice==computer_choice:
        print("TIE!")

    elif( 
        (user_choice=='r' and computer_choice=='s') or
        (user_choice=='s' and computer_choice=='p') or
        (user_choice=='p' and computer_choice=='r')):
        print("YOU WIN!")
    else:
        print("YOU LOSE!")    

    response=input("Do you want to continue?(y/n)").lower()
    if response=='n':
        break







