from datetime import datetime
import os

os.system('clear')
depthNumber = [0]

def displayRecursion(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        res = func(*args, **kwargs)
        end = datetime.now()
        depth = '\t' * depthNumber[0] 
        print(f'{depth}---------- | def {func.__qualname__}(args = {args}, kwargs = {kwargs}) | ----------')
        print(f'{depth}Total Time: {((end - start).total_seconds())* 1000} milliseconds')
        print(f'{depth}Description: {func.__doc__}') if func.__doc__ else ""
        print(f'{depth}Result: {res}')
        
        depthNumber[0] += 1
        return res
    return wrapper

def final(res):
    depthNumber[0] = 0
    print(f'Final result = {res}')
    print('-' * 100 + '\n')
# -------------------------| Code |---------------------------------------- 

@displayRecursion
def remove_tabs_and_spaces(string):
    if not string: return ""

    if string[0] in ['\t', ' ']:
        return remove_tabs_and_spaces(string[1:])
    return string[0] + remove_tabs_and_spaces(string[1:])

# final(remove_tabs_and_spaces(string="Hello\tWorld!    "))

@displayRecursion
def remove_all_adj_duplicates(string):
    if not string: return ""
    if len(string) == 1: return string

    if string[0] == string[1]:
        return remove_all_adj_duplicates(string[1:])
    return string[0] + remove_all_adj_duplicates(string[1:])

# final(remove_all_adj_duplicates(string="Hellooo"))

@displayRecursion
def merge_two_sorted_string(strOne, strTwo):
    if not strOne: return strTwo
    if not strTwo : return strOne

    if strOne[0] > strTwo[0]:
        # if we are considering it we need to move on....
        return strTwo[0] + merge_two_sorted_string(strOne, strTwo[1:])
    if strOne[0] < strTwo[0]:
        return strOne[0] + merge_two_sorted_string(strOne[1:], strTwo)

# final(merge_two_sorted_string(strOne="acu", strTwo="bst"))

@displayRecursion
def calculate_len(string):
    if not string: return 0

    return 1 + calculate_len(string[1:])

# final(calculate_len(string="Educative"))

@displayRecursion
def sum_of_digits_in_string(string):
    if not string: return 0

    if string[0].isnumeric():
        return int(string[0]) + sum_of_digits_in_string(string[1:])
    return sum_of_digits_in_string(string[1:])

# final(sum_of_digits_in_string(string="3a4b5"))

@displayRecursion
def is_palidrome(string):
    if len(string) == 1 or not string:
        return True

    if string[0] == string[-1]:
        return True and is_palidrome(string[1:-1])
    else: return False


final(is_palidrome(string="madam"))