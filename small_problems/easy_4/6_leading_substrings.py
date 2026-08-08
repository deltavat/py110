def leading_substrings(strand):
#   substrings = []
#   constructor = ''
#   for char in strand:
#       constructor += char
#       substrings.append(constructor)
#   
#   return substrings

    return [strand[:i+1] for i in range(len(strand))]

# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])