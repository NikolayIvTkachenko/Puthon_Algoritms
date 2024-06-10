#https://python-scripts.com/range

from functools import reduce
import pandas as pd

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

bin_colors002 = {
    "manual_color": "Yellow",
    "approved_color": "Green",
    "refused_color": "Red"
}

print(bin_colors002)

print(bin_colors002.get('approved_color'))
print(bin_colors002['approved_color'])

bin_colors002['approved_color'] = "Purple"
print(bin_colors002)

#sets

green01 = {'green', 'leaves', 'green'}
print(green01)

yellow = {'dandelions', 'fire hydrant', 'leaves'}
red = {'fire hydrant', 'blood', 'rose', 'leaves'}

print(yellow|red)
print(yellow&red)

#data frame

df = pd.DataFrame([
    ['1', 'Fares', 32, True],
    ['2', 'Elena', 23, False],
    ['3', 'Steven', 40, True]
])

df.columns = ['id', 'name', 'age', 'decision']

print(df)
print(df[['name', 'age']])
