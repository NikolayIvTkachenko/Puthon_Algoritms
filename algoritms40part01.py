#https://python-scripts.com/range

from functools import reduce

bin_colors = ['Red', 'Green', 'Blue', 'Yellow']
print(bin_colors[2:])
print(bin_colors[0:2])
print(bin_colors[0:-1])
print(bin_colors[0:-2])
print(bin_colors[-2:-1])

a01 = [1, 2, [100, 200, 300], 6]
print(max(a01[2]))
print(a01[2][1])

for aColor in bin_colors:
    print(aColor + " Square")

arr002 = list(filter(lambda x: x > 100, [-5, 200, 300, -10, 10, 1000]))
print(arr002)

arr003 = list(map(lambda x: x ** 2, [11, 22, 33, 44, 55, 66]))
print(arr003)

def doSum(x1, x2):
    return x1+x2

x001 = reduce(doSum, [100, 122, 33, 4, 5, 6])
print(x001)

x002 = range(6)
print(x002)
for n in x002:
    print(n)

addNum = range(3, 29, 2)
print(addNum)
for n in addNum:
    print(n)