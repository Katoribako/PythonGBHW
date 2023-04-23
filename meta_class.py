# реализовать метакласс. позволяющий создавать всегда один и тот же
# объект класса (см. урок)


class NewMeta(type):

    def __init__(cls, *args, **kwargs):
        cls.arguments = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.arguments == None:
            cls.arguments = super().__call__(*args, **kwargs)
            cls.arguments = cls.arguments = super().__call__(*args, **kwargs)
            return cls.arguments
        else:
            return cls.arguments


class MyClass(metaclass=NewMeta):

    def method_1(self):
        pass


My_class_1 = MyClass()
My_class_2 = MyClass()
My_class_3 = MyClass()

print(type(My_class_1))
print(type(My_class_2))
print(type(My_class_3))
print(My_class_1 == My_class_2)
print(My_class_1 is My_class_2)
print(My_class_1 == My_class_3)
print(My_class_3 is My_class_2)