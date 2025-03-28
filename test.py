# Description:
# Created by Emilia on 2025-02-27
from traceback import print_tb

aaa = ((1, 10), (1, 3), (1, 3), (3, 4), (2, 4))

aaa = sorted(aaa, key=lambda x: (x[0], x[1]))
print(aaa)

a = [2, 3, 4, 5, 6]
print()

c = 3

if c:
    print('s')
dict= {1:3, 3:5}
for i, item in enumerate(dict):
    print(i, item)

