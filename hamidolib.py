def greeting(name):
    print("Hey & Welcome {}".format(name))
greeting("medo")

class fruits():
    def __init__(self,color,flavor):
        self.color = color
        self.flavor = flavor
class apple(fruits):
    pass
american_apple = apple("green","tasty")

print(american_apple.color.upper())
        