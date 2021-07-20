def triangle(t):
   X = 2*t - 2
   for m in range(0, t):
      for n in range(0, X):
         print(end=" ")
      X = X - 2
      for n in range(0, m+1):
         print("$ ", end="")
      print("\r")
t = 4
triangle(t)
