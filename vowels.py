def isVowel(s1):
    s2=s1[0].lower()
    if s2=="a" or s2=="e" or s2=="i" or s2=="o" or s2=="u":
        return True
    else:
        return False
str1=input("Enter an Alphabet: ")
if isVowel(str1):
    print("Alphabet is a vowel")
else:
    print("Alphabet is a consonant")