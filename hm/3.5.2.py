# put your python code here
'''Вам дано описание наследования классов в формате JSON.
Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта есть поле name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.

Пример:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

﻿Эквивалент на Python:

class A:
    pass

class B(A, C):
    pass

class C(A):
    pass

Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не наследуется явно от одного класса более одного раза.

Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.

<имя класса> : <количество потомков>

Выводить классы следует в лексикографическом порядке.

Sample Input:

[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
Sample Output:

A : 3
B : 1
C : 2'''

import json
d = {}
l_n = []
data_raw = json.loads(input())
for row in data_raw:
    l_n.append(row['name'])
    for parent in  row['parents']:
        if parent not in d.keys():
            d[parent] = set()
            d[parent].add(row['name'])
        else:
            d[parent].add(row['name'])
d = {x : set(d[x]) for x in d.keys()}
def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            if graph.get(vertex) is not None:
                stack.extend(graph[vertex] - visited)
    return visited
result_d = {}
for l in l_n:
    result_d[l] = dfs(d, l)
for x in sorted(result_d):
    print(x + ' : ' + str(len(result_d[x])))
