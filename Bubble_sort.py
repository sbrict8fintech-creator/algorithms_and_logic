print("Bubble sort algorithm")
print()


while True:
    unsorted=input("Input your unsorted integer list separated by commas : ").split(',')
    unsorted=[int(i) for i in unsorted]
    if len(unsorted)==0 or len(unsorted)==1:
        print("Please enter at least two integers to sort!")
    else:
        break
order=input("Ascending(A) or Descending(D) ? :")
sorting=unsorted.copy()


if order.upper()=='A':
    j=1
    for k in range(len(sorting)):
        for i in range(len(sorting)-j):
            if sorting[i]>sorting[i+1]:
                mem=sorting[i]
                sorting[i]=sorting[i+1]
                sorting[i+1]=mem
        j+=1


elif order.upper()=='D':
    j = 1
    for k in range(len(sorting)):
        for i in range(len(sorting) - j):
            if sorting[i] < sorting[i + 1]:
                mem = sorting[i]
                sorting[i] = sorting[i + 1]
                sorting[i + 1] = mem
        j += 1


else:
    print("Please enter A or D!")


print(f'The unsorted list : {unsorted}')
print(f'The sorted list : {sorting}')