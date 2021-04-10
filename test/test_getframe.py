import sys
from pprint import pprint

def func1():
    print("Im in function 1")
    print("Im in function %s"%(sys._getframe().f_code.co_name))
    pprint(dir(sys._getframe().f_code))
    for a in dir(sys._getframe().f_code):
        print(a,getattr(sys._getframe().f_code,a))
    func2("%s::%s"%(sys._getframe().f_code.co_filename,
                    sys._getframe().f_code.co_name
                    )
        )
    
def func2(caller=None):
    print("This is func2 called by",caller)
    print("__name__ =",__name__)
    print("__module__ =",__module__)
    
if __name__ == '__main__':
    func1()
    
