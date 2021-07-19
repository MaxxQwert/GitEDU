def parcheck(graph, start, stop):
    if start == stop:
        return True
    if graph[start] == []:
        return False
    for i in graph[start]:
        if parcheck(graph, i, stop):
            return True
    return False



graph = {'GGG': ['F'],
        'A': [],
        'B' : ['A'],
        'C' : ['A', 'M'],
        'D' : ['U', 'C'],
        'E' : ['D'],
        'F' : ['D'],
        'X' : [],
        'Y' : ['X', 'A'],
        'Z' : ['X'],
        'V' : ['Z', 'Y'],
        'W' : ['V'],
        'M' : [],
        'K' : ['M'],
        'U' : ['Q', 'P'],
        'Q' : [],
        'P' : []}
print(parcheck(graph, 'GGG', 'M'))