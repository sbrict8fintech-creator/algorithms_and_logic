upper=int(input("Input upper limit : "))

for i in range(1,upper+1):
    factors=0
    for j in range(1,i+1):
        for k in range(1+i+1):
            if j*k==i:
                factors+=1
    if factors==2:
        print(f"{i} is a prime number✅")
    else:
        print(f"{i} is not a prime number")


# upper = int(input("Input upper limit: "))
#
# for i in range(2, upper + 1):  # Start at 2 (1 is not prime)
#     is_prime = True
#
#     for j in range(2, i):  # Check numbers from 2 up to i-1
#         if i % j == 0:  # If it divides evenly, it's not prime
#             is_prime = False
#             break  # Stop checking once we find one factor
#
#     if is_prime:
#         print(f"{i} is prime ✅")
#
