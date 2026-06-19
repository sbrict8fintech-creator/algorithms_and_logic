number=input("Input your number : ")

armstrong_num=0

for num in number:
    armstrong_num=armstrong_num+(int(num)**len(number))

if armstrong_num==int(number):
    print(f"{number} is a armstrong number.")
else:
    print(f"{number} is not a armstrong number.")
