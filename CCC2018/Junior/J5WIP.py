def find_shortest_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in graph:
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

numPages = int(input())
pages = []
poss = []
dicto = {}
poss = list(map(int, input().split()))
for i in range(1, numPages + 1):
    dicto.update({str(i):[]})
    if(i != 1):
        poss = list(map(int, input().split()))
    if(poss[0] == 0):
        dicto[str(i)].append('0')
    else:
        pages.append(poss[0])
        for j in range(1, poss[0] + 1):
            dicto[str(i)].append(str(poss[j]))
            
#print(dicto)

alll = 1

for i in range(2, numPages + 1):
    if(find_shortest_path(dicto, '1', str(i)) == None):
        alll = 0

if(alll == 1):
    print('Y')
else:
    print('N')
    
print(len(find_shortest_path(dicto, '1', '0')) - 1)
