#list related exercises
def min_element(l):
    if l != []:
        temp = l[0]
        for i in l:
            if i < temp:
                temp = i
        return temp
    return "empty list"
def max_element(l):
    if l != []:
        temp = l[0]
        for i in l:
            if i > temp:
                temp = i
        return temp
    return "empty list"
    
def rev(l):
    new = []
    if l != []:
        for i in l:
            temp = [i]
            new = temp + new 
    return new 
def rev2(l):
    return l[::-1]

def count_occurance(l, obj):
 
    if l == []:
        return 0
    if l[0] == obj:
        return 1 + count_occurance(l[1:], obj)
    elif type(l[0]) == list:
        temp = 0
        for i in l[0]:
            if i == obj:
                temp +=1 
        return temp + count_occurance(l[1:], obj)      
    else:
        return count_occurance(l[1:], obj)

def sum_list(l):
    if l == []:
        return 0
    elif len(l) == 1:
        return l[0]+ sum_list(l[1:])
    else:
        return l[0]+ sum_list(l[1:])
        
     
def sort_list(l):
    new_list = []
    while l != []:
        get_min = min_element(l)
        new_list.append(get_min)
        l.remove(get_min)
    return new_list
    
#non list related 
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
    
    
    
    
    