numFlowers = int(input())
fList = []
hList = []


def checkList(listC):
    hList = []
    goodList = 1
    for i in range(0, numFlowers):
        sortList = sorted(listC[i])
        if(sortList != listC[i]):
            goodList = 0
    
    if(goodList == 1):
        for i in range(0, numFlowers):
            hList.append(listC[i][0])
        for i in range(0, numFlowers):
            if(sorted(hList) != hList):
                goodList = 0
    return goodList

def rotList(listR):
    row = []
    plist = []
    for j in range(0, numFlowers):
        for i in range(0, numFlowers):
            row.append(listR[i][j])
        row.reverse()
        plist.append(row)
        row = []
    return plist

for i in range(0, numFlowers):
    fList.append(list(map(int, input().split())))
if(checkList(fList) == 1):
    for i in range(0, numFlowers):
        print(' '.join(list(map(str, fList[i]))))
else:
    fList2 = rotList(fList)
    if(checkList(fList2) == 1):
        for i in range(0, numFlowers):
            print(' '.join(list(map(str, fList2[i]))))
    fList3 = rotList(fList2)
    if(checkList(fList3) == 1):
        for i in range(0, numFlowers):
            print(' '.join(list(map(str, fList3[i]))))
    fList4 = rotList(fList3)
    if(checkList(fList4) == 1):
        for i in range(0, numFlowers):
            print(' '.join(list(map(str, fList4[i]))))
