def pyramid(p):
   for i in range(0, p):
      for j in range(0, i+1):
         print("* ",end="")
      print("\r")
p = 4
pyramid(p)
