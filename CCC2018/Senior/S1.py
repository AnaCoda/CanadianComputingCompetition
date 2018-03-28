numVils = int(input())
vils = []
nhoods = []

for i in range(0, numVils):
    vils.append(int(input()))

vils.sort()

for i in range(1, numVils - 1):
    nhoods.append(abs(vils[i] - vils[i-1]) + abs(vils[i] - vils[i+1]))
print(round(min(nhoods)/2, 1))
