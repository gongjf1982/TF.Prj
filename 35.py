class MyClass(object):
    def __init__(self):
        self.__par = None

    @property
    def par(self):
        print("Get Par")
        return self.__par

    @par.setter
    def par(self, value):
        print("Set par")
        self.__par = value

    @par.deleter
    def par(self):
        print("Del Par")
        del self.__par


if __name__ == "__main__":
    jack = MyClass()
    jack.par = 123456
    print(jack.par)
    del jack.par
