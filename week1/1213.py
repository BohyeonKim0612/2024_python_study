H=list(input())
C={}

for i in H:
    C[i]=H.count(i)

C_sorted=dict(sorted(C.items()))
V=list(C_sorted.values())

counter=0

for j in V:
    if j%2==1:
        counter+=1

S=""
M=""
if counter>1:
    print("I'm Sorry Hansoo")
else:
    for key, value in C_sorted.items():
        if value%2==0:
            S+=str(key*(value//2))
        elif value%2==1:
            M+=str(key)
            S+=str(key*(value//2))
    print(S+M+"".join(reversed(S)))