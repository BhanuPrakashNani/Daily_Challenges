n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
for i in a:
    for j in b:
        if i+j not in a:
            if i+j not in b:
                break
print(str(i)+" "+str(j))