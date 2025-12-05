# get the word
word = input("Enter a word: ")
print("-"*30)

# make a word from a string
list_word = list(word)

# reverse a list
list_word.reverse()

# make a string from the list
join_word = "".join(list_word)

print(join_word)
