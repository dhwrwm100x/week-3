a=0
b=0
arr=[]
for i in (3):
    arr.append(list(map(int, input().split())))
for i in range(len(arr)):
    if (i%2==0):
        a=i
    else:
        b=i
print('odd = ',b)
print('even = ',a)
