# OUT = 0
# IN = 1

# def countWords(string):
#     state = OUT
#     wc = 0

#     for i in range(len(string)):

#         if (string[i] == ' ' or string[i] == '\n' or
#             string[i] == '\t'):
#             state = OUT

#         elif state == OUT:
#             state = IN
#             wc += 1

#     return wc

# string =input("Enter a sentence: ")
# print("No. of words : " + str(countWords(string)))

def countWords(s1):
    c1=1
    for i in range(0,len(s1)):
        if s1[i]==" " and s1[i+1]!=" ":
            c1+=1
        if s1[i]=="," and s1[i+1]!=",":
            c1+=1
        if s1[i]=="#" and s1[i+1]!="#":
            c1+=1
    print("No. of words: ", c1)
s1=input("Enter any Sentence: ")
countWords(s1)
