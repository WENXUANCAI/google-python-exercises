x = ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'];
def front_x(words):
    x_words = [word for word in words if word.startswith('x')]
    non_x_words = [word for word in words if not word.startswith('x')]
    sorted_x_words = sorted(x_words)
    sorted_non_x_words = sorted(non_x_words)
    return sorted_x_words + sorted_non_x_words

print(front_x(x))
def fix_start(s):
    first_char = s[0]
    modified_s = first_char + s[1:].replace(first_char, '*')
    return modified_s

# Example usage:
result = fix_start('babble')
print(result)  # Output will be 'ba**le'