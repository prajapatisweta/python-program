# str1 = input("Write a string: ")
# vowels = 0
# consonants = 0

# for ch in str1:
#     if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
#         vowels = vowels + 1
#     else:
#         consonants = consonants + 1
# print("Total Number of Vowels in this String = ", vowels)
# print("Total Number of Consonants in this String = ", consonants)

def countV(s1):
    cVowel=0
    for ch in s1:
        if ch.lower() in ["a","e","i","o","u"]:
            cVowel+=1
        print("No. of vowels: ",cVowel)
        print("No. of Consonants: ", len(s1)-cVowel)
str1=input("Enter a string: ")
countV(str1)