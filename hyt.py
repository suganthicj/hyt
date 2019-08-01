x11=int(input())
l=list(map(int,input().split()))
y11=[]
for i in l:
	if i<x11:
		y11.append(i)
y11.sort()
print(*y11)
