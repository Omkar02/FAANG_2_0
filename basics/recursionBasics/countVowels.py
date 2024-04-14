def isVowels(char):
    return 1 if char.lower() in 'aeiou' else 0

def countVowels(string):
    if len(string) == 0:
        # base case 
        return 0
    
    # recursice case
    return countVowels(string[1:]) + isVowels(string[0])


string = "Educative"
string = "E"
print(countVowels(string))