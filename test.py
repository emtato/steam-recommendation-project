# Description:
# Created by Emilia on 2025-02-27

aaa = ((1, 10), (1, 3), (1, 3), (3, 4), (2, 4))

aaa = sorted(aaa, key=lambda x: (x[0], x[1]))
print(aaa)
