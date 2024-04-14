def reverse_str(word):
    print(word)
    if len(word) == 0:
        return word
    
    return reverse_str(word[1:]) + word[0]

print(reverse_str(word="hello world"))