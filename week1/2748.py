n=input()
counter=0
P0=0
P1=1
P2=1

while counter<int(n):
    P2=P0+P1
    counter+=1
    P0=P1
    P1=P2

print(P0)

