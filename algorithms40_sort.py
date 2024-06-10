
var1 = 1
var2 = 2

var1, var2 = var2, var1

print(var1, var2)

list01 = [2, 5, 2, -2, -7, 9, 0, 4]


#Bubble sort
def BubbleSort(list):
    lastElementIndex = len(list)-1
    for passNo in range(lastElementIndex, 0, -1):
        for idx in range(passNo):
            if list[idx]>list[idx+1]:
                list[idx], list[idx+1] = list[idx+1], list[idx]
    return list
print("Bubble sort")
print(BubbleSort(list01))

list01 = [2, 5, 2, -2, -7, 9, 0, 4]
#insertion sort
def InsertionSort(list):
    for i in range(1, len(list)):
        #print(i)
        j = i - 1
        #print(j)
        element_next = list[i]
        while(list[j] > element_next) and (j >= 0):
            #print("before ", j)
            list[j+1] = list[j]
            j = j - 1
            #print(j)
        list[j+1] = element_next
    return list
print("insertion sort")
print(InsertionSort(list01))

list01 = [2, 5, 2, -2, -7, 9, 0, 4]
#merge sort

def MergeSort(list):
    if len(list) > 1:
        mid = len(list)//2
        left = list[:mid]
        right = list[mid:]

        MergeSort(left)
        MergeSort(right)

        a = 0
        b = 0
        c = 0
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                list[c] = left[a]
                a = a + 1
            else:
                list[c] = right[b]
                b = b + 1
            c = c + 1

        while a < len(left):
            list[c] = left[a]
            a = a + 1
            c = c + 1

        while b < len(right):
            list[c] = right[b]
            b = b + 1
            c = c + 1
    return list
print("MergeSort")
print(MergeSort(list01))


list01 = [2, 5, 2, -2, -7, 9, 0, 4]
#Shell sort
def ShellSort(list):
    distance = len(list)//2
    while distance > 0:
        for i in range(distance, len(list)):
            temp = list[i]
            j = i
            while j >= distance and list[j - distance] > temp:
                list[j] = list[j - distance]
                j = j-distance
            list[j] = temp
        distance = distance//2
    return list
print("ShellSort")
print(ShellSort(list01))