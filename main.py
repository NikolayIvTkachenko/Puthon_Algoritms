import search_max_value


arr1 = [8, 4, 1, 5, 3, 2, 4, 0, 7, 9]
arr2 = [8, 4, 1, -77, -2, -34, 5, 66, 3, 2, 4, 0, 7, 9, 45]
arr3 = [8, 4, 1, -77, -2, -34, 5, 66, 3, 2, 4, 0, 7, 9, 45, -65, 87, 105]

maxvalue = search_max_value.flawed(arr1)
print(maxvalue)

maxvalue = search_max_value.largest(arr2)
print(maxvalue)

maxvalue = search_max_value.alternate(arr2)
print(maxvalue)

first, second = search_max_value.largest_two(arr2)
print(first, second)


first, second = search_max_value.sorting_two(arr2)
print(first, second)

first, second = search_max_value.double_two(arr2)
print(first, second)

first, second = search_max_value.mutable_two(arr2)
print(first, second)

first, second = search_max_value.tournament_two(arr3)
print(first, second)











# # Кортеж из чисел, в том числе с плавающей точкой и комплексных
# numbers_tuple = (1, 2, 3, 4, 5, 2.5, 3 + 4j)
# # Кортеж из строк
# fruits_tuple = ('яблоко', 'банан', 'апельсин')
# # Кортеж из логических значений
# my_tuple = (True, False)
# # Кортеж из других кортежей
# nested_tuple = ((1, 2), ('a', 'b'))
# # Кортеж из списков
# my_tuple = ([1, 2, 3], ['a', 'b', 'c'])
# # Кортеж из словарей
# my_tuple = ({'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25})
# # Кортеж из разных типов данных
# mixed_tuple = (1, 'hello', [1, 2, 3], {'a': 10})







# def print_hi(name):
#     print(f'Hi, {name}')
#
# if __name__ == '__main__':
#     print_hi("Test")
# print("Test text")
# print("---------")
# print("-" * 6)
# print("*" * 8)
# a = [4, 5, 7, 1, 3, 7, 0]
# print(a)