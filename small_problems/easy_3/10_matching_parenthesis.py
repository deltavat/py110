def is_balanced(phrase):
    status = 0
    
    for char in phrase:
        if char == '(':
            status += 1
        elif char == ')':
            status -= 1
        
        if status < 0:
            return False
    
    return status == 0

print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True