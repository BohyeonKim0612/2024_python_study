n=int(input())
c={}

for i in range(1,n+1):
    if i==1:
        c[i]=0
    elif i%3==0 and i%2==0:
        c[i]=min(c[i//3]+1,c[i//2]+1,c[i-1]+1)
    elif i%3==0:
        c[i]=min(c[i//3]+1,c[i-1]+1)
    elif i%2==0:
        c[i]=min(c[i//2]+1,c[i-1]+1)
    else:
        c[i]=c[i-1]+1


print(c[n])