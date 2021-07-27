def checkPangram(s1):
    a1="abcdefghijklmnopqrstuvwxyz"
    for alpha in a1:
        if alpha in s1.lower():
            continue
        else:
            print("Sentence is not a Pangram")
            break
    else:
        print("Sentence is a Pangram")

statement=input("Enter a sentence: ")
checkPangram(statement)