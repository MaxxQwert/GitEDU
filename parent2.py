def parcheck(graph, start, stop):
    if start == stop:
        return True
    if graph[start] == []:
        return False
    for i in graph[start]:
        if parcheck(graph, i, stop):
            return True
    return False
cls = {}
for _ in range(int(input())):
    cls_str = input()
    cls_nod = cls_str.split(':')[0].strip(' ')
    if cls_str == cls_nod:
        cls_par = []
    else:
        cls_par = cls_str.split(':')[1].split()
    cls.update({cls_nod:cls_par})
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
    

