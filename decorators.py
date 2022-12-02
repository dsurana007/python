import time
def decorator_1(original_func):
    print("In the decorator function before executing original {} function".format(original_func.__name__))
    def wrapper_func(*args,**kwargs):
        print("in the wrapper function before calling the original function {}".format(original_func.__name__))
        original_func(*args,**kwargs)
        print("After executing the main display function{}".format(original_func.__name__))
        return original_func
    return wrapper_func


@decorator_1
def display(name,age):
    print("#############this is the original display function displaying the name and the age ################")
    print("the name is {} and the age is {}".format(name,age))
    print("#############################")

display('dhiraj',39)
display('niraj',38)
