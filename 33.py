class MyClass(object):
    def __init__(self):
        self.__XXOO = None

    def setXXOO(self, value):
        print("Set")
        self.__XXOO = value

    def getXXOO(self):
        print("Get")
        return self.__XXOO

    def delXXOO(self):
        print("Del")
        del self.__XXOO

    XXOO = property(getXXOO, setXXOO, delXXOO)


if __name__ == "__main__":
    cs = MyClass()
    cs.XXOO = 100
    print("cs.XXOO=", cs.XXOO)
    del cs.XXOO
    print("------")
    # print("cs.XXOO=", cs.XXOO)
