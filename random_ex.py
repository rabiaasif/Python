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
    
def next_num(n):
    '''
    exercise I was given, given an input like  n = [9, 2, 1] (number is 129) return the next number
    '''
   
    n.reverse()
    
    if n[-1] < 9:
        n[-1] = n[-1]+1 
    
        print n
    else:
        index = len(n)-1
        while index != 0:
            if n[index] == 9 :
                n[index] = 0
                if n[index-1] != 9:
                    n[index-1] += 1
            index = index -1 
          
        print n 
        
def add_array(array, other):
    '''
    given array and other ex [1,1,1] and [1,2,3], add the numbers of each index togehter
    '''
    index = 0
    if len(array) == len(other):
        for i in array:
            array[index] = array[index] + other[index]
            print array[index]
            index +=1 
    else:
        index =  abs(len(other) - len(array))
        while index < len(array):
            array[index] = array[index] + other[0]
            print array[index]
            index +=1     
def multiply(array, other):
   # array = [0,1] -> 10
    #other = [0, 2] -> 20 10x 20 = 200 
    array.reverse()
    other.reverse()
    new_a = '' 
    new_o = ''
    for i in array:
        new_a += str(i)
    for i in other:
        new_o += str(i)
    
    print str(int(new_o)*int(new_a)):
        
    

        
        
        
    
    
    
    