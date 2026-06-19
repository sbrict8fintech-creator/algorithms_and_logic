for i in range(2,1000):
    factors=[]
    for j in range(1,i):
        if i%j==0:
            factors.append(j)
        else:continue
    num=0
    for x in factors:
        num+=x
    if num==i:
        print(f"{i} is a perfect number")
