numList = []

for i in range(0, 4):
    numList.append(int(input()))
    
if((numList[0] == 8 or numList[0] == 9) and (numList[3] == 8 or numList[3] == 9) and (numList[1] == numList[2])):
    print("ignore")
else:
    print("answer")
