import random, time
def rolldice():
    return random.randint(1,6)
print("Welcome to DICE ROLL!!!")

def menu():
    print("Enter 1 for rolling die.")
    time.sleep(2)
    print("Enter 2 for exiting.")
    time.sleep(2)

menu()

choice = int(input("Enter your choice: "))
time.sleep(2)
print("DRUMROLSSSSSSS")
time.sleep(3)

if choice == 1:
    print("You rolled ",rolldice())
    time.sleep(3)
    menu()
    time.sleep(3)
    choice = int(input("You want to roll again? enter 1, else 2 for exiting.... "))
    time.sleep(3)
    print("DRUMROLSSSSSSS")

if choice == 2:
    print('''Thankyou for using DICE ROLL, 
you're now succesfully exitied from the game!''')
    