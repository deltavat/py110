def staggered_case(string):
    new_string = []
    tracker = 0
    
    for char in string:
        if tracker % 2 == 0 and char.isalpha():
            new_string.append(char.upper())
            tracker += 1
        elif tracker % 2 == 1 and char.isalpha():
            new_string.append(char.casefold())
            tracker -= 1
        else:
            new_string.append(char)
    
    return ''.join(new_string)

string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True

#uppercase_next = True
#
#for char in string:
#   if char.isalpha():
#       if uppercase_next:
#           new_string.append(char.upper())
#       else:
#           new_string.append(char.lower())
#           
#       uppercase_next = not uppercase_next
#   else:
#       new_string.append(char)