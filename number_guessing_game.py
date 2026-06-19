


num_list=[i for i in range(1,1001)]


my_guess=int(input("What is your guess? : "))

is_running=True

while is_running:
    guessed_num=num_list[len(num_list)//2]
    print(f"Computer guessed : {guessed_num}")
    user_reaction=input("high/low/correct(h,l,c) : ").lower()
    if user_reaction=='h':
        num_list=[i for i in range(num_list[0],num_list[num_list.index(guessed_num)])]
    if user_reaction=='l':
        num_list=[i for i in range(num_list[num_list.index(guessed_num)+1],num_list[-1]+1)]
    if user_reaction=='c':
        print("You guessed correctly!!!")
        is_running=False