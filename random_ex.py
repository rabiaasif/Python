import doctest
#list related exercises
def min_element(l):
    """
    >>> min_element([100,"1", 5, "43"])
    '1'
    
    >>> min_element([])
    Traceback (most recent call last):
      File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/doctest.py", line 1315, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.min_element[1]>", line 1, in <module>
        min_element([])
      File "<wingdb_compile>", line 29, in min_element
    ValueError: List is empty
    
    >>> min_element([100,-1, -100, 1000])
    -100
    
    >>> min_element([100,0, 143, 1000])
    0
    
    >>> min_element([100,"test", 143, 1000])
    0
    """
     
    if l != []:
        temp = int(l[0])
        for i in l:
            if int(i) < int(temp):
                temp = i
        return temp
    else:
        raise ValueError("List is empty")

def max_element(l):
    """
    >>> max_element([100,"1", 5, "43"])
    100
    
    >>> max_element([])
    Traceback (most recent call last):
      File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/doctest.py", line 1315, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.min_element[1]>", line 1, in <module>
        min_element([])
      File "<wingdb_compile>", line 29, in min_element
    ValueError: List is empty
    
    >>> max_element([100,-1, -100, 1000])
    1000
    
    >>> max_element([100,0, 143, 1000])
    1000
    
    >>> max_element([1000,"test", 143, 1000])
    1000
    """    
    if l != []:
        temp = int(l[0])
        for i in l:
            if int(i) > int(temp):
                temp = i
        return temp
    else:
        raise ValueError("List is empty")
    
def rev(l):
    """
    >>> rev([100,"1", 5, "43"])
    ['43', 5, '1', 100]
    
    >>> rev([])
    []
    
    >>> rev([100,-1, -100, 1000])
    [1000, -100, -1, 100]
    
    >>> rev([100,0, 143, 1000])
    [1000, 143, 0, 100]
    
    >>> rev([1000,"test", 143, 1000])
    [1000, 143, 'test', 1000]
    """      
    new = []
    if l != []:
        for i in l:
            temp = [i]
            new = temp + new 
    return new 

def rev2(l):
    """
    >>> rev2([100,"1", 5, "43"])
    ['43', 5, '1', 100]
    
    >>> rev2([])
    []
    
    >>> rev2([100,-1, -100, 1000])
    [1000, -100, -1, 100]
    
    >>> rev2([100,0, 143, 1000])
    [1000, 143, 0, 100]
    
    >>> rev2([1000,"test", 143, 1000])
    [1000, 143, 'test', 1000]
    """     
    return l[::-1]

def count_occurance(l, obj):
    """
    >>> count_occurance([1,1,1,1], 1)
    4
    
    >>> count_occurance([2,1,4,1,[10,01,1,1]], 1)
    5
    
    >>> count_occurance([], 1)
    0
    
    >>> rev2([100,0, 143, 1000])
    [1000, 143, 0, 100]
    
    >>> rev2([1000,"test", 143, 1000])
    [1000, 143, 'test', 1000]
    """       
 
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
    """
    >>> count_occurance([1,1,1,1], 1)
    4
    
    >>> count_occurance([2,1,4,1,[10,01,1,1]], 1)
    5
    
    >>> count_occurance([], 1)
    0
    
    >>> sum_list([])
    0
    
    >>> sum_list([1,2,3,4,5])
    15
    
    >>> sum_list([-1,1])
    0
    """     
    
    if l == []:
        return 0
    elif len(l) == 1:
        return l[0]+ sum_list(l[1:])
    else:
        return l[0]+ sum_list(l[1:])
        
     
def sort_list(l):
    """
    >>> sort_list([1,2,3,4])
    [1, 2, 3, 4]
    
    >>> sort_list([])
    []
    
    >>> sort_list([4])
    [4]
    
    >>> sort_list([4,3,2,1])
    [1, 2, 3, 4]
    """     
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
    
    print str(int(new_o)*int(new_a))
    
def isogram(phrase):
    tracker = {}
    for i in phrase:
        if i in tracker:
            tracker[i] += 1
        else:
            tracker[i] = 0
    for i in tracker.values():
        if i > 0:
            return False
    return True
        


   
#if __name__ == "__main__":
    #import doctest
    #doctest.testmod()
        
    

        
        
        
    
    
    
    