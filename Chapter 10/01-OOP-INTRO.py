# Class defines a blueprint for an object
class Student:

    # Constructor (__init__) to initialize object properties
    def __init__(self, name, roll_no, marks):
        self.name = name                # public attribute
        self.roll_no = roll_no
        self.__marks = marks            # private attribute (encapsulation)

    # Method to display student info
    def display_info(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}")

    # Getter method to access private data
    def get_marks(self):
        return self.__marks

    # Setter method to change marks
    def set_marks(self, new_marks):
        self.__marks = new_marks

# Inheritance: GraduateStudent class inherits from Student
class GraduateStudent(Student):

    # Constructor with extra field
    def __init__(self, name, roll_no, marks, thesis_title):
        super().__init__(name, roll_no, marks)     # Call parent constructor
        self.thesis_title = thesis_title

    # Method overriding (Polymorphism)
    def display_info(self):
        super().display_info()
        print(f"Thesis Title: {self.thesis_title}")

# Create object of GraduateStudent
s1 = GraduateStudent("Hassan", 101, 89, "AI in Education")

# Call methods
s1.display_info()
print("Marks:", s1.get_marks())

# Update marks using setter
s1.set_marks(95)
print("Updated Marks:", s1.get_marks())
