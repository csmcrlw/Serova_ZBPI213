#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Задание 1

def fact(x):
    
    if x == 0 or x == 1:
        return 1
    else:
        return x * fact(x-1)
    
    
# Задание 2

def filter_even(ls):
    return list(filter(lambda x: x % 2 == 0, ls))


# Задание 3

def square(ls):
    return list(map(lambda x: x**2, ls))


# Задание 4

def bin_search(ls, item):
    
    low = 0
    high = len(ls) - 1
    
    while low <= high: 
        mid = low + high
        guess = ls[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return -1    # значение, которое вернёт функция, если элемент в списке отсутствует


# Задание 5

def is_palindrome(string):
    
    marks = ''' —!()-[]{};?@#$%:'"\,./^&;*_'''
    for x in marks:
        string = string.replace(x, '')
    string = string.lower()
    left_pos = 0
    right_pos = len(string) - 1
    
    while right_pos >= left_pos:
        if not string[left_pos] == string[right_pos]:
            return 'NO'
        left_pos += 1
        right_pos -= 1
    return 'YES'


# Задание 6

def calculate(file_name):

    calculator = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y,
                 '**': lambda x, y: x ** y,
                 '//': lambda x, y: x // y,
                 '%': lambda x, y: x % y
                 }
    
    with open(file_name, 'r', encoding='utf-8') as f:
        
        items = f.read().splitlines()
        res = []
        
        for item in items:
            item = item.split('    ')
            res.append(str(calculator[item[0]](int(item[1]), int(item[2]))))
        return ','.join(res)

    
# Задание 7

def substring_slice(first_file, second_file):

    with open(first_file, 'r', encoding="utf-8") as f1,     open(second_file, 'r', encoding="utf-8") as f2:

        string_file = f1.read().splitlines()
        nums_file = [[int(i) for i in item.split(' ')] for item in f2.read().split('\n')]
        res = []
        
        for i in range(len(nums_file)):
            string = string_file[i][nums_file[i][0]:nums_file[i][1] + 1]
            res.append(string)
        return ' '.join(res)
    
    
# Задание 8

from json import load
from re import findall

def decode_ch(string_of_elements):
    
    with open('periodic_table.json', 'r', encoding='utf-8') as f:
        
        periodic_table = load(f)
        string = findall(r'[A-Z][a-z]*', string_of_elements)
        res = [periodic_table[i] for i in string]
        return ''.join(res)


# Задание 9

class Student:
    
    def __init__(self, name, surname, grades=[3, 4, 5]):
        self.name = name
        self.surname = surname
        self.fullname = f'{name} {surname}'
        self.grades = grades
        
    def greeting(self):
        return f'Hello, I am Student'
        
    def mean_grade(self):
        return sum(self.grades) / len(self.grades)
    
    def is_otlichnik(self):
        return ['NO', 'YES'][self.mean_grade() >= 4.5]
    
    def __add__(self, other):
        return f'{self.name} is friends with {other.name}'
    
    def __str__(self):
        return self.fullname
    
    
# Задание 10

class MyError(Exception):
    
    def __init__(self, msg):
        self.msg = msg

