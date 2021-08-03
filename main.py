import pandas as pd

# stud = pd.read_csv('https://stepik.org/media/attachments/course/4852/StudentsPerformance.csv')
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_colwidth', None)
# pd.set_option('display.width', 300)
# all =(stud['lunch'].shape[0])
# sel = (stud.loc[stud['lunch'] == 'free/reduced']['lunch'].shape[0])
# print(stud['lunch'].value_counts(normalize=True)['free/reduced'])
workers = [['Ivan', 'Ivanov', 100000, 2], ['Petr', 'Petrov', 150000, 2], ['Sidor', 'Sidorov', 200000, 3]]
for worker in workers:
    if worker[3] < 2:
        print(f'{worker[0]} {worker[1]} is junior')
    elif worker[3] >= 2:
        print(f'{worker[0]} {worker[1]} is middle')
    elif worker[3] > 5:
        print(f'{worker[0]} {worker[1]} is senior')