num1 = int(input("Enter number to check if Armstrong Number or not: "))
num2 = int(input("Enter number to check if Armstrong Number or not: "))

def armstrong(num1, num2):
    for num in (num1, num2):
        a = 1
        count = 0
        while a <= num:
            a *= 10
            count += 1

        if num>9 :
            b = 10
            c = 1
            x = count - 1
            d = 10**x
            arms = (num // d) ** count

            while num // b != 0:
                rem =  num // b
                c *= 10

            if num == arms:
                print(num)
            num+=1



armstrong(num1, num2)




