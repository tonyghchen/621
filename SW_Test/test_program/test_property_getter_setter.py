class MyClass(object):
    def __init__(self):
        self._param=None
    @property
    def param(self):
        print("getParam:",self._param)
        return self._param
    @param.setter
    def param(self,value):
        print("setParam:",self._param)
        self._param=value
    @param.deleter
    def param(self):
       print("delParam:",self._param)
       del self._param

if __name__=="__main__":
    cls=MyClass()
    cls.param=10
    print("current param :",cls.param)
    del cls.param
