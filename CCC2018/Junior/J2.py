numSpaces = int(input())
ySpaces = []
nSpaces = []
same = 0
for char in input():
    ySpaces.append(char)
for char in input():
    nSpaces.append(char)
    
for i in range(0, numSpaces):
    if(ySpaces[i] == nSpaces[i] and ySpaces[i] == 'C'):
        same += 1
        
print(same)
