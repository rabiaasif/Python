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
  
if __name__ == "__main__":
    
    import doctest
    doctest.testmod()