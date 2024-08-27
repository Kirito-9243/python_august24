word1 = input("Enter any word:")
word2 = input("Enter the right rotated of the 1st word:")
if word1 == word2:
    print(f"{word1} = {word2} , invalid rotated word!!")
else:
    accii_word1 = 0
    accii_word2 = 0
    for i in range(len(word1)):
        accii_word1 += (ord(word1[i])-96)
    for i in range(len(word2)):    
        accii_word2 += (ord(word2[i])-96)

    if accii_word1 ==  accii_word2:
        print(f"The right rotated word is of the word '{word1}'")
    else:
        print(f"The right rotated word is not of the word '{word1}'")


