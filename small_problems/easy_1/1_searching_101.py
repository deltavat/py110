'''
PROBLEM
    INPUT
    • six integers entered by user, one at a time.
    
    OUTPUT
    • one sentence stating if the last number was present in the previous 5 numbers (displayed with commas).
    
    RULES
        EXPLICIT
        • program solicits six (6) numbers from the user, one at a time with input()
        • program prints a message that describes whether the sixth number appears among the first five
        
        IMPLICIT
        • negatives and 0s should function normally
        • assuming user inputs integers, exception handler or non-int guard clause not necessary  (convert to int on input)

EXAMPLES
Example 1:
Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 17

17 is in 25,15,20,17,23.


Example 2:
Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 18

18 isn't in 25,15,20,17,23.

DATA STRUCTURE
• input_list = empty list that will store user inputs, returned as user_list
• number_iterator = list to keep count of no. of inputs and store 'nth' words

ALGORITHM
• create an empty list
• create an iterator list for 'nth' words to loop through & keep count of no. of inputs
• add every number input into the empty list & return list
• check if last list element exists in the first five elements of the input list
• output if it does, or doesn't
• might use tuple unpacking to grab the first five values instead of traditional ways because I prefer it more.

CODE
'''

def get_user_input():
    input_list = []
    number_iterator = ['1st', '2nd', '3rd', '4th', '5th', 'last']
    for nth in number_iterator:
        input_list.append(int(input(f'Enter the {nth} number: ')))
    
    return input_list

user_list = get_user_input()
a, *b, c = str(user_list[:5])
previous_five = ''.join(b).replace(', ', ',')

if user_list[-1] in user_list[:5]:
    print(f'{user_list[-1]} is in {previous_five}.')
else:
    print(f'{user_list[-1]} isn\'t in {previous_five}.')