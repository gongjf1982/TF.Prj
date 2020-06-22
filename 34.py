class MyClass(object):
    def __init__(self):
        self.__S1 = "S1"
        self.__S2 = "S2"

    def getS1(self):
        print("Get S1")
        return self.__S1

    def setS1(self, value):
        print("Set S1")
        self.__S1 = value

    def delS1(self):
        print("Del S1")
        del self.__S1

    S1 = property(getS1, setS1, delS1)

    @property
    def S2(self):
        print("Get S2")
        return self.__S2

    @S2.setter
    def S2(self, value):
        print("Set S2")
        self.__S2 = value

    @S2.deleter
    def S2(self):
        print("Del S2")
        del self.__S2


if __name__ == "__main__":
    cs = MyClass()
    # print(cs.S1)
    # cs.S1 = "S11111"
    # print(cs.S1)
    # del cs.S1

    print(cs.S2)
    cs.S2 = "S22222"
    print(cs.S2)
    del cs.S2