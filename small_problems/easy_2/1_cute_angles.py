'''
PROBLEM
    INPUT
    • a floating point number representing an angle between 0 and 360 degrees
    
    OUTPUT
    • a string representing that angle in degrees, minutes, and seconds
    
    RULES
        EXPLICIT
        • degree symbol (°) to represent degrees, a single quote (') to represent minutes, and a double quote (") to represent seconds
        • 60 minutes in a degree, and 60 seconds in a minute
        
        IMPLICIT
        • DEGREE = "\u00B0" for degree symbol
        
EXAMPLES
# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"" or dms(254.6) == "254°36'00\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

DATA STRUCTURE
• calculate degrees, minutes and seconds using the number, converting to `int` and *60 as necessary
• account for 60 seconds/minutes edge cases

ALGORITHM
• initialise degrees, minutes, seconds
• degrees are int(number), minutes being the decimal of the number, and seconds being the remaining decimals from minutes
• 60 minutes/seconds edge cases
• return formatted string literal with degrees, minutes and seconds symbol

'''

DEGREE = "\u00B0"

def dms(number):
    degrees = int(number)
    minutes = int((number - degrees) * 60)
    seconds = int(round((((number - degrees) * 60) - minutes) * 60))
    
    if seconds == 60:
        seconds = 0
        minutes += 1
    
    if minutes == 60:
        minutes = 0
        degrees += 1
        
    return f'{degrees}{DEGREE}{minutes:02d}\'{seconds:02d}\"'

# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"" or dms(254.6) == "254°36'00\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")