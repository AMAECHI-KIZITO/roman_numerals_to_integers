''' Roman Numerals to integer'''

def numerals_to_integer(s:str):
    choices={
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    
    result=0
    
    for i in range(len(s)):
        if i+1 < len(s) and choices[s[i]] < choices[s[i+1]]:
            result = result - choices[s[i]]
        else:
            result = result + choices[s[i]]
        
    print(result)

convert=input('Enter a Roman Numeral: ')
convert=convert.upper()
numerals_to_integer(convert)
