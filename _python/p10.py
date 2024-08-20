# Problem statement: Check if the Alphabet is vowel or consonant

alphabet = input("Enter any Alphabet:")
alphabet_l = alphabet.lower()
oval = ["a","e","i","o","u"]
if len(alphabet) != 1:
    exit("Invalid input!!")

if alphabet_l in oval:
    print(alphabet,"is an Oval !!!")
else:
    print(alphabet,"is a consonant !!")

