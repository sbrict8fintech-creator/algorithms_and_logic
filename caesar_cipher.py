letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
shift=-5
word=input("Enter a word : ").upper()
new_word=''
index=[letters.index(letter) for letter in word]
new_index=[(num+shift)%26 for num in index]
new_letters=[letters[i] for i in new_index]
for k in new_letters:
    new_word+=k

print(new_word)