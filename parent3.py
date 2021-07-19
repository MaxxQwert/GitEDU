def parcheck(graph, start, stop):
    if start == stop:
        return True
    if graph[start] == []:
        return False
    for i in graph[start]:
        if parcheck(graph, i, stop):
            return True
    return False
cls = {'a':[],
'b' : ['a'],
'c' : ['a'],
'f' : ['a'],
'd' : ['c', 'b'],
'g' : ['d', 'f'],
'i' : ['g'],
'm' : ['i'],
'n' : ['i'],
'z' : ['i'],
'e' : ['m', 'n'],
'y' : ['z'],
'x' : ['z'],
'w' : ['e', 'y', 'x']}

exc = []
cls_str = []
n = int(input())
cls_str.append(input())
for i in range(n-1):
    cls_str.append(input())
    for j in range(i,-1,-1):
        if parcheck(cls, cls_str[i+1], cls_str[j]) and cls_str[i+1] not in exc:
            exc.append(cls_str[i+1])
for s in exc:
    print(s)
    

