upper=int(input("Input upper limit : "))

for i in range(2,upper):
    count=0
    if i==2:print(f"{i} is a prime number")
    else:
        for j in range(1,i+1):
            if i%j==0:count+=1
    if count==2:
        print(f"{i} is a prime number")

