class Parent1:
    def info(self):
        print('Class name: %s' % (str(Parent1.__name__)))


class Parent2:
    def info(self):
        print('Class name: %s' % (str(Parent2.__name__)))


class Child(Parent2, Parent1):

    def info(self):
        Parent1.info(self)


obj = Child()
obj.info()
