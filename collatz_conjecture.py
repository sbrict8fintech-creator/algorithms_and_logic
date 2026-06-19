number=int(input("Input a number : "))

while number!=1:
    print(number)
    if number%2==0:
        number/=2
        continue
    if number%2!=0:
        number=(3*number)+1
print(number)
