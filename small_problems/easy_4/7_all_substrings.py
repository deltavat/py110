def leading_substrings(strand):
    return [strand[:i + 1] for i in range(len(strand))]

def substrings(strand):
#   final_list = []
#   for i in range(len(strand)):
#       final_list.extend(leading_substrings(strand[i:]))
#   
#   return final_list
    return [substring for i in range(len(strand)) for substring in leading_substrings(strand[i:])]


expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True