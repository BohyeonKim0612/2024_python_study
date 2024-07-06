T=input()
for i in range(1,int(T)+1):
    data=input()
    H,W,N=data.split(" ")
    if int(N)%int(H)==0:
        X=int(N)//int(H)
    else:
        X=int(N)//int(H)+1
    if int(N)%int(H)==0:
        Y=H
    else:
        Y=int(N)%int(H)

    if X<10:
        print(str(Y)+"0"+str(X))
    else:
        print(str(Y)+str(X))
    
