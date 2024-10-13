import time
import random

my_list = ['Chemistry','Maths','Physics','Biology']
my_list1 = ['Sandy','Mayank','Rajesh','None']

random_element = random.choice(my_list)
random_element1 = random.choice(my_list1)

time.sleep(1)

print("True or False")
print(random_element,"=",random_element1)

input = input("Is input true or false?: ")

if random_element == "Maths" & random_element1 =="Mayank":
    input = "true"
    print("Correct")

else:
    print("Wrong")