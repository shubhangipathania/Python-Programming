class ExampleClass:
    def __init__(self,argument1,argument2):
        self.args1=argument1
        self.args2=argument2

    @classmethod
    def factory_method(cls,argument1,argument2):
        return cls(argument1,argument2)
    
obj=ExampleClass.factory_method(10,20)
print(obj.args1,obj.args2)
