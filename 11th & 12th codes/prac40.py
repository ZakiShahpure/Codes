a = int(input("Enter: "))
b = int(input("Enter: "))
smaller = b
hcf = 1

if a>b:
    smaller = b
else:
    smaller = a
i = 2
while i<smaller+1:
    if a%i==0 and b%i==0:
        hcf = i
    elif a%i!=0 and b%i!=0:
        hcf = 1
    i+=1

print(hcf)