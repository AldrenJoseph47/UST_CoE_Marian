class addsub():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
class muldiv:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b

def main():
    o1=addsub(2,1)
    o2 = addsub(4, 3)
    print(o1.add())
    print(o2.sub())
    print(o1.add())
    print(o2.add())