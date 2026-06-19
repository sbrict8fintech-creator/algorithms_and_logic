# for i in range(1,10001):
#     str_num=str(i)
#     length=len(str_num)
#     sumn=0
#     for j in str_num:
#         sumn=sumn+(int(j)**length)
#     if sumn==i:
#         print(f"{i} is a narcissistic number")


for i in range(1,10001):
    int_list=[]
    num=i
    sum_all=0
    while num>0:
        remainder=num%10
        int_list.append(remainder)
        num=num//10
    for nums in int_list:
        sum_all+=nums**len(int_list)
    if sum_all==i:
        print(f"{i} is a narcissistic number")