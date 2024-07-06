M = [None]*10
N = [None]*10
D = [None]*10

for i in range(10):
    M[i] = int(input())
for i in range(10):
    num=0
    for j in range(i+1):
        num+=M[j]
    N[i] = num
    D[i] = (100-num)**2    
Ans = D.index(min(D))
if Ans!=9 and D[Ans]==D[Ans+1]:
    Ans += 1
print(N[Ans])