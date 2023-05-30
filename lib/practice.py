class User:
    def log_in(self):
        print('User logged in() called.')
        self.logged_in = True

class Student(User):
    def log_in(self):
        print("Student.log_in() called.")
        super().log_in()
        self.in_class = True



class User:
    def log_in(self, name):
        self.name = name
    
    def log_in(self):
        self.logged_in = True

class Student(User):
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def log_in(self):
         super().log_in()
         self.in_class =True

oneil = Student()
oneil.log_in()
# "Student.log_in() called."
# "User.log_in() called."
# True





class User:
    def __init__(self, name):
        print("User.__init__ called.")
        self.name = name

    def log_in(self):
        self.logged_in = True

class Student(User):
    def __init__(self, name, grade):
        print("Student.__init__ called.")
        super().__init__(name)
        self.grade = grade

    def log_in(self):
        super().log_in()
        self.in_class = True


oneil = Student("O'neil", 10)
# Student.__init__ called.
# User.__init__ called.
oneil.__dict__
# {'name': "O'neil", 'grade': 10}
