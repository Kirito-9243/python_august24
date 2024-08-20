# Problem statement: Check if the Alphabet is vowel or consonant

alphabet = input("Enter any Alphabet:")
alphabet_l = alphabet.lower()
vowel = ["a","e","i","o","u"]
if len(alphabet) != 1:
    exit("Invalid input!!")

if alphabet_l in vowel:
    print(alphabet,"is an Vowel !!!")
else:
    print(alphabet,"is a consonant !!")

