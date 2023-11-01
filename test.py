# 1
#date = '2025-12-31'
#new_date = tuple(date.split('-')[::-1])
#print(new_date)
# 2
#lst = ['1', '2', '3', '4', '5']
#sum_of_elements = sum(int(x) for x in lst)
#print(sum_of_elements)
# 3
#lst = [1, 2, 3, 4, 5, 6]
#mid = len(lst) // 2

#first_half_sum = sum(lst[:mid])
#second_half_sum = sum(lst[mid:])

#result = first_half_sum / second_half_sum

#print(result)

# 4
#def find_divisors(numbers):
#result = []
#for num in numbers:
#divisors = []
#for i in range(1, num+1):
#if num % i == 0:
#divisors.append(i)
#result.append(divisors)
#return resul
#  5
#dct1 = {
#'a': 1,
#'b': 2,
#}
#dct2 = {
#'c': 3,
#'d': 4,
#}
# 6
#def find_min_max(numbers):
#result = {}
#result['max'] = max(numbers)
#result['min'] = min(numbers)
#return result
# 7
# def find_divisors(numbers):
#result = []
#for num in numbers:
#divisors = []
#for i in range(1, num+1):
#if num % i == 0:
#divisors.append(i)
#result.append(divisors)
#return result
# 8
#def generate_random_numbers(N, start, end):
#result = []
#previous_number = None
#for _ in range(N):
#number = random.randint(start, end)
#while number == previous_number:
#number = random.randint(start, end)
#result.append(number)
#previous_number = number
#return result
# 9
#def random_color():
# Список доступных цветов
#colors = ["красный", "синий", "зеленый", "желтый", "оранжевый", "фиолетовый", "розовый", "голубой"]

# Выбираем случайный цвет из списка
#random_index = random.randint(0, len(colors) - 1)
#return colors[random_index]

# Пример использования функции
#random_color_result = random_color()
#print("Случайный цвет:", random_color_result)
# 10
#def split_into_syllables(word):
#vowels = "аеёиоуыэюя"
#syllables = []

#word = word.lower()
#i = 0

#while i < len(word):
#if word[i] in vowels:
#start = i
#while i + 1 < len(word) and word[i + 1] not in vowels:
#i += 1
#syllables.append(word[start:i+1])
#i += 1

#return syllables

#word_example = "программирование"
#print(split_into_syllables(word_example))
# 11
#import random

#def shuffle_list(input_list):
#shuffled_list = input_list.copy()
#random.shuffle(shuffled_list)
#return shuffled_list

# Пример использования функции:
#my_list = [1, 2, 3, 4, 5]
#shuffled = shuffle_list(my_list)
#print(shuffled)


#
# '''
# import unittest
# def date_str_trans_motorcade(str):
#     str = str.replace('-', ' ')
#     str = tuple(str.split(' '))
#     str = str[::-1]
#     return str
# class TestUM(unittest.TestCase):
#     def testEqual(self):
#         self.failUnlessEqual(date_str_trans_motorcade('2025-12-31'), ('31', '12', '2025'))
# '''
#
# # Задание 2
# '''
# import unittest
# def sum_list(list):
#     sum = 0
#     for i in range(0, len(list)):
#         list[i] = int(list[i])
#         sum += list[i]
#     return sum
# class testUM(unittest.TestCase):
#     def testEqual(self):
#         self.failUnlessEqual(sum_list(['1','2','3','4','5']), 15)
# '''
#
# # Задание 3
# '''
# import unittest
# def one_division_two(list):
#     sum1 = 0
#     sum2 = 0
#     for i in range(0, len(list) // 2):
#         sum1 += list[i]
#     for i in range(len(list) // 2, len(list)):
#         sum2 += list[i]
#     return sum1 / sum2
# list = [1, 2, 3, 4, 5, 6]
# division_result = 0.4
# class testUM(unittest.TestCase):
#     def testEqual(self):
#         self.failUnlessEqual(one_division_two(list), division_result)
# '''
#
# # Задание 4
# '''
# import unittest
# def merge_dictionaries(dictionary1, dictionary2):
#     return dictionary1 | dictionary2
# dct1 = {
# 	'a': 1,
# 	'b': 2,
# }
# dct2 = {
# 	'c': 3,
# 	'd': 4,
# }
# dct3 = dct1 | dct2
# class testUM(unittest.TestCase):
#     def testEqual(self):
#         self.failUnlessEqual(merge_dictionaries(dct1, dct2), dct3)
# '''
#
# # Задание 5
# '''
# import unittest
# def sum_val_dictionary(dictionary):
#     sum = 0
#     #for i in range(0, len(dictionary)):
#         #for j in range(0, len(dictionary[i])):
#             #sum += dictionary[i][j]
#     for i in dictionary:
#         for j in dictionary:
#             sum += dictionary[i][j]
#     return sum
# dct = {
# 	1: {
# 		1: 11,
# 		2: 12,
# 		3: 13,
# 	},
# 	2: {
# 		1: 21,
# 		2: 22,
# 		3: 23,
# 	},
# 	3: {
# 		1: 24,
# 		2: 25,
# 		3: 26,
# 	},
# }
# result_sum = 177
# class testUM(unittest.TestCase):
#     def testEqual(self):
#         self.failUnlessEqual(sum_val_dictionary(dct), result_sum)
# '''
#
# # Задание 5
# '''
# import unittest
# def min_max_list(list):
#     min = 1
#     max = 0
#     for i in range(0, len(list)):
#         if min > list[i]:
#             min = list[i]
#         if max < list[i]:
#             max = list[i]
#     return {
#         'min': min,
#         'max': max,
#     }
# list = [1, 2, 3, 4, 5]
# print(min_max_list(list))
# class testUM(unittest.TestCase):
#     def testEqual(self):
#         self.failUnlessEqual(min_max_list(list), {'min': 1, 'max': 5})
# '''
#
# # Задание 6
# '''
# import unittest
# def count_division(list):
#     d = dict()
#     for i in range(0, len(list)):
#         for j in range(1,list[i]+1):
#             if list[i] % j == 0:
#                 d[j] = list[i] // j
#         list[i] = d
#         d = dict()
#     return list
# list = [1, 2, 3]
# result_list = [{1: 1}, {1: 2, 2: 1}, {1: 3, 3: 1}]
# class testUM(unittest.TestCase):
#     def testEqual(self):
#         self.failUnlessEqual(count_division(list), result_list)
# '''
#
#
# # Задание 8
# '''
# import unittest, random
# def random_elements(list):
#     return list[random.randint(0,len(list))]
# list = ['red','orange','yellow','green','blue']
# print(random_elements(list))
# class testUM(unittest.TestCase):
#     def testEqual(self):
#         self.failIfEqual(random_elements(list), 'purple')
# '''
#
# # Задание 9
# '''
# import unittest
# def counts_syllables(let):
#     let = let.lower()
#     vowels = ['а', 'о', 'у', 'э', 'ы', 'я', 'ё', 'е', 'ю', 'и'] # можно внести слоги, но их очень много
#     count = 0
#     for i in range(0, len(let)):
#         for j in range(0, len(vowels)):
#             if let[i] == vowels[j]:
#                 count += 1
#     return count
# letter = 'Привет'
# #print(counts_syllables(letter))
# class testUM(unittest.TestCase):
#     def testEqual(self):
#         self.failUnlessEqual(counts_syllables(letter), 2)
# '''
#
# # Задание 10
# '''
# import unittest, random
# def shuffle_list(list):
#     random.shuffle(list)
#     return list
# list = [1, 2, 3, 4, 5]
# #print(shuffle_list(list))
# class testUM(unittest.TestCase):
#     def testEqual(self):
#         self.failIfEqual(shuffle_list(list), [1, 2, 3, 4, 5])
# '''