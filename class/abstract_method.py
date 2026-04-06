class AbstractClass:
    def abstract_method(self):
        raise NotImplementedError("This method must be implemented by the subclass")
    

class ConcreteClass(AbstractClass):
    def abstract_method(self):
        return "This is the implementation of the abstract method"
    
class AnotherConcreteClass(AbstractClass):
    pass

concrete = ConcreteClass()
print(concrete.abstract_method())

another_concrete = AnotherConcreteClass() # ye class abstract method ko implement nahi kar rahi hai, isliye ye error dega
print(another_concrete.abstract_method())