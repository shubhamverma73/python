class staticmethod:
    @staticmethod
    def static_method():
        print("This is a static method")

instance = staticmethod()
instance.static_method() # just for showing that we can call static method using instance but it is not recommended way to call static method
staticmethod.static_method() # real way to call static method without creating instance of class