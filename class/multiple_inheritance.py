class A:
    def method_a(self):
        return "Method A"
    
    def method_common(self):
        return "Method Common from A"
    
class B:
    def method_b(self):
        return "Method B"
    
    def method_common(self):
        return "Method Common from B"
    
class C(A, B): # ye multiple inheritance hai, jisme hum ek class ke properties aur methods ko dusre class me use kar sakte hai
    def method_c(self):
        return "Method C"
    
c = C()
print(c.method_a())
print(c.method_b())
print(c.method_c())
print(c.method_common()) # ye method common hai, lekin C class me A class ko pehle inherit kiya gaya hai, isliye method_common() A class ka method call karega. Agar B class ko pehle inherit kiya jata to B class ka method call hota.

# isko kahte hai method resolution order (MRO), jisme Python pehle C class me method_common() ko search karega, agar nahi mila to A class me search karega, agar wahan bhi nahi mila to B class me search karega.
print(C.mro()) # ye method resolution order ko print karta hai, jisme C class pehle aata hai, uske baad A class aata hai, uske baad B class aata hai, aur sabse last me object class aata hai, jisme sabhi classes inherit karti hai.