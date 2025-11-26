# get the word
word = input("Enter a word: ")
gusse = input("Dose the word start with a vowel? ").lower()
print("-"*50)
# vowel
vowel = "iouae"
# first_leter of word
first_leter = word[0].lower()

# check the word stsrt with a vowel
if (first_leter in vowel) and (gusse == "yes"):
    print(f"Bravoo!!\n{word} starts with a vowel")

elif (first_leter not in vowel) and (gusse == "no"):
    print(f"Bravoo!!\n{word} Dose not start with a vowel")

else :
    print("lets try again")


