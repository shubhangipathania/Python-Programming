#Without any recursion
# n=int(input("Enter the number:"))
# for i in range(n,0,-1):
#       if(n==1):
#             print("*")
#       else:
#             print("*"*i)

#with recursion 
def pattern(n):
      if(n==0):
            return
      print("*"*n)
      pattern(n-1)

pattern(3)


