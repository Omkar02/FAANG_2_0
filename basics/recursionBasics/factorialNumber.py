def factorialNumber(n):
    if n in [0, 1]:
        # base case
        return 1
    
    # recurcive case
    return n * factorialNumber(n - 1)

def naturalNumber(lower, upper):
    if lower > upper:
        return
    print(lower)

    naturalNumber(lower+1, upper)


def countVowels(word, n):
    def isVowel(c): 
        return 1 if c.lower() in 'aeiou' else 0
    
    if n == 0: return 0
    if n == 1: return isVowel(word[0])

    return countVowels(word, n - 1) + isVowel(word[n - 1])



# print(factorialNumber(5))
# naturalNumber(0, 5)


word = "Educative"
print(countVowels(word, len(word))) 