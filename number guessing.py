import random


start=int(input("enter the start :\n"))
end=int(input("enter the end :\n "))
              

ran_number=random.randint(start,end)

user_integer=0

while user_integer != ran_number:

    user_integer=int(input("enter the number :"))
    
    if user_integer < ran_number :
        print("too high")

    elif user_integer > ran_number:
        print("Too low")

print("youuuu're correct !")