
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

#Seletion sort
list01 = [2, 5, 2, -2, -7, 9, 0, 4]

def SelectionSort(list):
    for fill_slot in range(len(list) - 1, 0, -1):
        max_index = 0
        for location in range(1, fill_slot + 1):
            if list[location] > list[max_index]:
                max_index = location
        list[fill_slot], list[max_index] = list[max_index], list[fill_slot]
    return list

print("SelectionSort")
print(SelectionSort(list01))


list01 = [2, 5, 2, -2, -7, 9, 0, 4]
#Linear Search
def LinearSearch(list, item):
    index = 0
    found = False

    while index < len(list) and found is False:
        if list[index] == item:
            found = True
        else:
            index = index + 1
    return found

print("Linear Search")
print(LinearSearch(list01, 9))
print(LinearSearch(list01, 99))

list01 = [2, 5, 2, -2, -7, 9, 0, 4]
#BinarySearch
def BinarySearch(list, item):
    first = 0
    last = len(list)-1
    found = False
    while first<=last and not found:
        midpoint = (first + last)//2
        if list[midpoint] == item:
            found = True
        else:
            if item < list[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found

print("BinarySearch")
sorted_list = BubbleSort(list01)
print(BinarySearch(sorted_list, 9))
print(BinarySearch(sorted_list, 99))


list01 = [2, 5, 2, -2, -7, 9, 0, 4]
#InterpolarySerach
def IntPolsearch(list, x):
    idx0 = 0
    idxn = (len(list)-1)
    found = False

    while idx0 <= idxn and x >= list[idx0] and x <= list[idxn]:
        mid = idx0 + int(((float(idxn - idx0)/(list[idxn] - list[idx0])) * (x - list[idx0])))
        if list[mid] == x:
            found = True
            return found
        if list[mid] < x:
            idx0 = mid + 1
    return found

print("InterpolarySerach")
sorted_list = BubbleSort(list01)
print(IntPolsearch(sorted_list, 9))
print(IntPolsearch(sorted_list, 99))