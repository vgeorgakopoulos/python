def oneDivisionBy_X_Plus(x,y):
 if y==0: # termination logic point for recursion
     return 1
 return 1 / (x + oneDivisionBy_X_Plus(x,y-1))

print(oneDivisionBy_X_Plus(1,3))