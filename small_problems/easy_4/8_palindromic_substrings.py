def leading_substrings(strand):
    return [strand[:i + 1] for i in range(len(strand))]

def substrings(strand):
    return [substring for i in range(len(strand)) for substring in leading_substrings(strand[i:])]

def palindromes(strand):
    return [substring for substring in substrings(strand) if substring == substring[::-1] and len(substring) > 1]

print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                                    [
                                            'll', '-madam-', '-madam-did-madam-',
                                            'madam', 'madam-did-madam', 'ada',
                                            'adam-did-mada', 'dam-did-mad',
                                            'am-did-ma', 'm-did-m', '-did-',
                                            'did', '-madam-', 'madam', 'ada', 'oo',
                                    ])    # True

print(palindromes('knitting cassettes') ==
                                    [
                                            'nittin', 'itti', 'tt', 'ss',
                                            'settes', 'ette', 'tt',
                                    ])    # True