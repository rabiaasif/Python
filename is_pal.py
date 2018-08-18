
def is_pal(word):
    '''
    1) Check if a string is a palindrome:
    ex: 'madam' or 'pop' → 1
    'nurse' or 'sensibill' → 0
    '''
    word = str(word)
    if len(word) == 0:
        return 1 
    elif word[0] == word[-1]:
        return is_pal(word[1:-1])
    else:
        return 0
    
def occurs_once(lst):
    '''
    2) Find the only element in an array that only occurs once.
    ex: [1, 3, 3, 4, 9, 2, 3, 1, 9, 4] ---> 2
    '''
    temp = {} #store values in dictionary to keep count of occurences 
    for i in lst:
        if i in temp:
            temp[i] += 1
        else: 
            temp[i] = 0
            
    result = [] #store values that only occur once in an array (incase there are multiple values that occur exp: [1, 3, 3, 4, 9, 2, 3, 1, 9, 4,2, 100, 101010, 999] has multiple values that occur once 
    for key in temp: 
        if temp[key] == 0:
            result.append(key)
    if result ==[]:
        return 'No Value' #if no values occur once 
    else:
        return result #return list of results that occur more than once

        
def occurs_once_2(lst):
    '''
    2) Find the only element in an array that only occurs once.
    ex: [1, 3, 3, 4, 9, 2, 3, 1, 9, 4] ---> 2
    '''
    temp = {} #store values in dictionary to keep count of occurences 
    for i in lst:
        if i in temp:
            temp[i] += 1
        else: 
            temp[i] = 0
            
    for key in temp: 
        if temp[key] == 0:
            return key
    return 'No Value' #if no values occur once 
    