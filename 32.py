class MyClass(object):
    def __init__(self):
        self.__param = None

    def getParam(self):
        print("Get self.__param", self.__param)
        return self.__param

    def setParam(self, value):
        print("Set self.__param", self.__param)
        self.__param = value

    def delParam(self):
        print("Del self.__param", self.__param)
        del self.__param

    param = property(getParam, setParam, delParam)


if __name__ == "__main__":
    cls = MyClass()
    cls.param = 100
    print("Current Param:", cls.param)
    del cls.param
