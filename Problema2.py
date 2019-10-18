"""
andresvallejoz1991
"""
notas = [(5, 5, 10), (10, 2, 4), (10, 1, 9), (10, 2, 3)]

suma = lambda x: x[0]+x[1]+x[2]


print(list(map(suma,notas)))
