#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str:
        return 0
    
    hash = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    count = len(roman_string)
   
    
    if count > 1:
        start = hash[roman_string[0]]
        next = hash[roman_string[1]]
        if start < next:
            result = next - start
        else:
            result = next + start

        for num in range(2, count):
            cur = hash[roman_string[num]]
            if  result > cur:
                result += cur
            else:
                result -= cur
    else:
        result = hash[roman_string[0]]

    return result
        
        
    