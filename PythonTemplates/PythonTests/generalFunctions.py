from Utils.testUtils import functions_test

def foo(a:int, b:int=0, c:int=0):
    """[summary]

    Args:
        a (int): [description]
        b (int, optional): [description]. Defaults to 0.
        c (int, optional): [description]. Defaults to 0.
        
    >>> foo(1,2,3)
    7
    """
    print(a + b + c)
    


if __name__ == '__main__':
    print(f'Testing {__file__.split("/")[-1]} module  functions......')
    functions_test()
    print(f'Test End')