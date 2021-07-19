import os
pypath = []
for dirpath, dirnames, filenames in os.walk("main"):
    for filename in filenames:
        if filename.endswith('py'):
            pypath.append(dirpath)
            break
pypath.sort()
cont = '\n'.join(pypath)
print(cont)
with open('pypath.txt', 'w') as f:
    f.write(cont)