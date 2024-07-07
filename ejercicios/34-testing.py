import doctest
def suma(a,b):
    
    """La función debería sumar correctamente
    >>> suma(5,10)
    15
    """
    return a+b
if __name__ == "__main__" :
    print(doctest.testmod())