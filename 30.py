class MyClass:
    count = 0
    name = "name"

    def __init__(self, name):
        self.name = name
        print("MyClass name=", MyClass.name, "Self name=", self.name)

    def setCount(self, count):
        self.count = count

    def getCount(self):
        return self.count


if __name__ == "__main__":
    cls1 = MyClass("Gong")
    cls2 = MyClass("Shi")
    cls1.name = "name Gong"
    cls1.count = 111
    cls1.setCount(11)
    cls2.setCount(12)
    print("Gong's Count", cls1.getCount())
    print("Shi's count", cls2.getCount())
    print(cls1.name, ":", cls2.name)
    print(cls1.count, ":", cls2.count)
    print(MyClass.name, ":", MyClass.count)
