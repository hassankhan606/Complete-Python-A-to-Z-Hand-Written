# Instance attributes take precedence over class attributes during retrieval and assignment
#^ When looking for an attribute using object.attribute, Python checks:
#* 1) Is the attribute present in the object instance?
#* 2) If not, is it present in the class?

class NewEmployee:
    language = "Python"   # Class attribute
    name = "Shan"         # Class attribute

    def get_info(self):
        print(f"The name is: {self.name}")
        print(f"The language is: {self.language}")

    def greet(self):
        print("Good Morning")

# Creating an instance of NewEmployee
haman = NewEmployee()
haman.name = "Hassan"  # Setting instance attribute (overrides class attribute for this instance)

# Calling methods
haman.greet()
haman.get_info()
