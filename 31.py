class MyCounter:
    __secretCount = 10
    publicCount = 11

    def __init__(self):
        pass

    def __secretFun(self):
        print("私有方法")
        self.__secretCount += 1
        self.publicCount += 1

    def publicFun(self):
        print("公有方法")
        self.__secretFun()
        print("__secretCount", self.__secretCount)
        print("publicCount", self.publicCount)


if __name__ == "__main__":
    cnt = MyCounter()
    cnt.publicFun()
    print("cnt.publicCount=", cnt.publicCount)
    print("MyCounter.publicCount=", MyCounter.publicCount)
