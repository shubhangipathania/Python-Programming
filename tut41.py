n,m=map(int,input().split())
array=list(map(int,input().split()))
a=set(map(int,input().split()))
b=set(map(int,input().split()))
happiness=0
for i in array:
    if(i in (a)):
        happiness=happiness+1
    elif(i in (b)):
        happiness=happiness-1
    else:
        happiness=0
print(happiness)
        


n,m=map(int,input().split())
print(n,m)
array=list(map(int,input().split()))
print(array)
n = int(input())
integer_list = tuple(map(int, input().split()))
t=integer_list
print(t)
x=hash(t)
print(abs(x))