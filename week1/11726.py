n=input()
counter=1
P1=1
P2=2
P3=3

while counter<int(n):
    P3=P1+P2
    counter+=1
    P1=P2
    P2=P3

print(P1%10007)