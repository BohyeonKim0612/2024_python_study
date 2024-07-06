I = input().split()
A = int(I[0])-1
B = int(I[1])

N = []
counter = 1

while len(N)<B+1:
    N += [counter]*counter
    counter += 1

print(sum(N[A:B]))