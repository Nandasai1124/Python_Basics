
d={}
n=int(input())
for i in range(n):
    k=input()
    v=input()
    d[k]=v
key=input()
value=input()
d.update({key:value})
print(d)