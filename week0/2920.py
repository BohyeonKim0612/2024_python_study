Raw = input().split()
A = [int(i) for i in Raw]
counter = 0

for i in range(1,len(A)):
    if A[i-1]<A[i]:
        counter += 1
if counter==len(A)-1:
    print("ascending")
elif counter==0:
    print("descending")
else:
    print("mixed")
    