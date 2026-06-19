def tribonacci(x):
    nums=[0,1,1]
    for i in range(x-3):
        next_num=nums[i]+nums[i+1]+nums[i+2]
        nums.append(next_num)
    for num in nums:
        print(num,end=' ')

input_length=int(input("How long sequence do you want? :"))

tribonacci(input_length)