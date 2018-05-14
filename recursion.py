'''   zip(l1,l2, f) zips up lists l1 and l2, combining 
    corresponding 
    members of l1 and l2 with f, so...zip([1,2,3],[5,20,100], 
    times)=[5,40,300]. I assume times(x,y)=x*y.
    foldr, foldl (look these up)
    
     '''

# USE RECURSION
def is_increasing(L):
    if len(L)==1:
        return True 
    else:
        if L[0] < L[1]:
            return is_increasing(L[1:])
        else:
            return False 
def is_decreasing(L):
    if len(L)==1:
        return True
    else:
        if L[0] > L[1]:
            return is_decreasing(L[1:])
        else:
            return False 
        
def power(x,y):
    '''return x^y)
    '''
    if y == 1:
        return x
    else:
        return x*power(x,y-1)

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

def reverse(l):
    if l ==[]:
        return l
    else:
        return [l[-1]] + reverse(l[:-1])
    
def is_pal(s):
    if s=='' or len(s)==1:
        return True
    elif s[0] == s[-1]:
        return is_pal(s[1:-1])
    
def all_equal(l):
    '''returns whether all members of l are the same'''
    if len(l)<2:
        return True 
    else:
        last_one = l[-1]
        all_others = all_equal(l[:-1])
        return last_one==all_others

def strip_element(l,e):
    '''return l with e removed, so strip_element([1,2,3,4,3,2,3,6,4,2], 2)
    returns [1,3,4,3,3,6,4]'''
    if e in l:
        l.remove(e)
        return strip_element(l,e)
    else:
        return l

def flatten(l):
    ''' need help :(
    returns a list of all non-list members of l (a standard exercise), 
    so flatten([[1,2,3],[4,[5]], 6,7,[9,10,11,12],[4,[15,16]]]) returns 
    [1,2,3,4,5,6,7,9,10,11,12,4,15,16]'''
    
    new_list = []
    
    if l == []:
        return new_list
    
    if len(l) ==  1:
        if type(l[0]) is not list:
            new_list.append(l[0])
            return new_list
        else:
            new_list += flatten[0]

        
    if len(l) > 1:
        m = len(l)//2
        l1 = l[:m]
        l2 = l[m+1:]
        

def any_true(l,p):
    '''returns True if p(x) is true for some x in l, False otherwise'''

    pass 

def map(l,f):
    
    '''returns the list [f(x) : where x is in l], so map([1,2,3,4], 
    double) 
    returns [2,4,6,8]. I assume double(x)=2*x'''

    pass

def all_true(l,p):
    '''returns True if p(x) is true for all x in l, False otherwise'''

    pass
        
def gcd(number,divisor):
    if divisor == 1:
        return 1
    if divisor == 0:
        return number
    else:
        return gcd(number,number%divisor)
def my_max(a,b):
    if a == None:
        return b
    if b == None:
        return a
    elif a>b:
        return a 
    else:
        return b

def max1(L):
    
    if L== []:
        return None
    else:
        return my_max(L[-1],max1(L[:-1]))
        
def my_min(a,b):
    
    if b == None:
        return a
    if a == None:
        return b 
    if a<b:
        return a 
    else:
        return b

def min1(l):
    
    if l==[]:
        return None
    else:
        return my_min(min1(l[:-1]),l[-1])

def sum1(n):
    
    if n <1:
        return n
    else:
        return n + sum1(n-1)
    
def fib(n):
    
    if n == 0 or n ==1 :
        return n
    else:
        return fib(n-1) + fib(n-2)
        