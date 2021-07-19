import os
pypath = sorted(dirpath + filename for dirpath, dirnames, filenames in os.walk("main") for filename in filenames if filename.endswith('py'))
with open('pypath.txt', 'w') as f:
    for i in pypath:
        print(i)
        f.write(i + '\n')
