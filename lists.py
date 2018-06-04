def min(l):
    if l != []:
        temp = l[0]
        for i in l:
            if i < temp:
                temp = i
        print temp
        return temp
    return "empty list"
def max(l):
    if l != []:
        temp = l[0]
        for i in l:
            if i > temp:
                temp = i
        print temp
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

        
        
        
    
    
    
    
    
    