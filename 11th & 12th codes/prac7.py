num=int(input("Enter the start range of even number: "))
num1=int(input("Enter the end range of even number: "))
print(f"list of even number from{num} to {num1}")
while num <= num1:
    if num % 2 == 0:
        print(num)
    num +=1