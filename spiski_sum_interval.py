"""
sum_of_intervals([
    [1, 1],
])
# 0
sum_of_intervals([
    [1, 2],
    [50, 100],
[60, 70],
])
# 51
sum_of_intervals([
    [1, 2],
    [5, 10],])
"""


def sum_of_intervals(interval):
    a = []
    b =[]
    for i, j in interval:
        a.append(i)
        b.append(j)
    max1 = max(a)
    min1 = min(b)
    sum = min1 + max1


    return sum

        #if set(list_1).issubset(list_2)


print(sum_of_intervals([
        [7, 10],
        [1, 4],
        [2, 5],
    ]))
