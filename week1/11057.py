n=int(input())
d=[[0]*10 for _ in range(n)]

for m in range(10):
    d[0][m]=1

for j in range(1,n):
    for i in range(10):
        d[j][i]=sum(d[j-1][k] for k in range(i+1))

print(sum(d[n-1][m] for m in range(10))%10007)