#selective import will fail with main()
#selective import will fail when using module when the function is inside the entity main()
#therefore a (dunder variable)__name__ variable is used
#this is mainly used when two or more python file is interlinked
#it will only be executed if the module is being run as the main program.
import P11
from P11 import *



def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def main():
    print(add(a, b))
    print(sub(a, b))

a,b=10,1
main()