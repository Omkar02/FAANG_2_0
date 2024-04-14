from datetime import datetime

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
def power_of_number(num, exponent):
    if exponent == 0: return 1
    return num * power_of_number(num, exponent - 1)

# final(power_of_number(2, 7))

@displayRecursion
def sum_of_integers(n):
    if n == 0: return 0
    return n + sum_of_integers(n - 1)

# final(sum_of_integers(5))

@displayRecursion
def mod_function(dividend, divisor):
    if divisor == 0: raise ZeroDivisionError
    if divisor > dividend: return dividend

    return mod_function(dividend - divisor, divisor)

# final(mod_function(10, 4))

@displayRecursion
def greatest_common_divisor(numOne, numTwo):
    if numOne == numTwo: return numOne
    if numOne > numTwo:
        return greatest_common_divisor(numOne - numTwo, numTwo)
    else:
        return greatest_common_divisor(numOne, numTwo - numOne)


# final(greatest_common_divisor(20, 2))

@displayRecursion
def pascal_triangle(n):
    if n == 1: return [1]
    line = [1]
    prev_line = pascal_triangle(n - 1)
    for i in range(len(prev_line) - 1):
        line.append(prev_line[i] + prev_line[i + 1])
    line.append(1)
    return line

# final(pascal_triangle(9))


@displayRecursion
def integer_to_binary(n):
    if n <= 1: return str(n)
    # Floor division: 
    # division that results into whole number 
    # adjusted to the left in the number line
    return integer_to_binary(n // 2) + integer_to_binary(n % 2)

# final(integer_to_binary(20.2))

@displayRecursion
def foo(i, j):
    if i == 0 :
        return j
    else :
        return foo(i - 1, i + j)
      
# Driver Code
# print(foo(4, 7))

@displayRecursion
def double_func_pattern(n):
    if n > 100 :
      return n - 5
    return double_func_pattern(double_func_pattern(n + 11))
  
# Driver Code
# print(double_func_pattern(45))