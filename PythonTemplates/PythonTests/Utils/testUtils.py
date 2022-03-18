import doctest

def class_test(obj: object):
    """
    Test all the class functions based on their documentation
    """
    
    print(f'Testing {obj.__class__.__name__} class ......')
    doctest.testmod(extraglobs={f'test_obj': obj})
    print(f'Test End')


def functions_test():
    """
    Test all the module functions based on their documentation
    """
    doctest.testmod()