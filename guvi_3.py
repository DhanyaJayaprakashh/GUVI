b=input()
#k=["`","!","@","#","$"]
if b >= 'a' and b <= 'z':
    if b == "a" or b == "e" or b == "i" or b == "o" or b == "u":
        print("Vowel")
    if b != "a" and b != "e" and b != "i" and b != "o" and b != "u":
        print ("Consonant")
else:
    print("Invalid")

