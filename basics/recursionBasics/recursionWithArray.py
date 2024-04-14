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
        print(f'{depth}Total Time: {((end - start).total_seconds()) * 1000} milliseconds')
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
def count_occurance_of_key(arr, key):
    if not arr: return 0
    if key == arr[0]:
        return 1 + count_occurance_of_key(arr[1:], key)
    return count_occurance_of_key(arr[1:], key)

# final(count_occurance_of_key(arr=[1,2,3,4,1,2,1,1], key=1))

@displayRecursion
def reverse_an_array(arr):
    if not arr: return []
    curr_val = [arr.pop()]
    return curr_val + reverse_an_array(arr)

# final(reverse_an_array(arr=[1, 2, 3, 4]))
# final(reverse_an_array(arr=[]))

@displayRecursion
def replace_all_negative(arr):
    if not arr: return []

    return [arr[0] if arr[0] > 0 else 0] + replace_all_negative(arr[1:])

# final(replace_all_negative(arr=[2, -3, 4, -1, -7, 8]))

@displayRecursion
def average_of_arr(arr, n=0):
    if n == len(arr): return 0
    if n == 0:
        # adding it to the call stack to only exe at last...
        return (arr[n] + average_of_arr(arr, n + 1)) / len(arr)
    return arr[n] + average_of_arr(arr, n + 1)

# final(average_of_arr(arr=[10, 2, 3, 4, 8, 0]))

@displayRecursion
def is_balanced_parenthesis(arr, val=0):
    if not arr: return val == 0
    if val < 0 : return False

    if arr[0] == '(': return is_balanced_parenthesis(arr[1:], val + 1)
    if arr[0] == ')': return is_balanced_parenthesis(arr[1:], val - 1)

# final(is_balanced_parenthesis(arr=["(","(", ")","(", ")", ")", "(", ")"]))
# final(is_balanced_parenthesis(arr=[x for x in "(()))("]))
# final(is_balanced_parenthesis(arr=[x for x in ")()("]))


@displayRecursion
def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    new_arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new_arr.append(left[i])
            i += 1
        elif left[i] >= right[j]:
            new_arr.append(right[j])
            j += 1
        
    new_arr.extend(left[i:])
    new_arr.extend(right[j:])

    return new_arr

final(merge_sort(arr=[12, 11, 13, 5, 6, 7]))