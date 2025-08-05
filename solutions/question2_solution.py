"""
Question 2: Python - Missing Characters

Summary: Implement a function missingCharacters that takes a string consisting of lowercase letters and digits. The function 
should return a new string containing all digits and lowercase English letters that are not present in the input string. The 
digits should come first in ascending order, followed by characters, also in ascending order.

"""

def missingCharacters(s):
    
    """
    Returns a string containing all digits (0-9) and lowercase English letters (a-z)
    that are not present in the input string `s`. Digits appear first in ascending order,
    followed by letters in ascending order.
    """

    
    # Store missing digits and letters
    temp_list = []
    
    # Check for missing digits (0–9)
    for number in range(10):
        # add the numbers, which are missing in string s to the temp list
        if str(number) not in s:
            temp_list.append(str(number))
    
    # Check for missing lowercase letters (a–z)
    for character in range(97, 123):
        # add the characters, which are missing in string s to the temp list
        if chr(character) not in s:
            temp_list.append(chr(character))
            
    # Combine all missing characters into a single string
    result_string = ''.join(temp_list)
    return result_string

if __name__ == '__main__':
    s = 'abcd1234'
    result = missingCharacters(s)
    print(result)
