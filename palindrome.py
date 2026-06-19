word=input("Enter the original word : ").lower()
rev_check=len(word)-1
marks=0
for i in range(len(word)):
    if word[i]==word[rev_check]:
        marks+=1
        rev_check-=1
    else:
        rev_check-=1
if marks==len(word):
    print(f"'{word}' is a palindrome word.")
else:
    print(f"'{word}' is not a palindrome word.")