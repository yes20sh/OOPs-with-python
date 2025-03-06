class User:
    def __init__(self,name,password):
        self.name = name
        self.password = password
    
    def display(self):
        print(f"name : {self.name} & password : {self.password}")

class Student(User):
    def __init__(self, subject, subject_code, name, password):
        super().__init__(name,password)
        self.subject = subject
        self.subject_code = subject_code
    
    def display(self):
        print(f"subject : {self.subject} & subject code : {self.subject_code}")
        super().display()

std1 = Student('Python', 345, 'Yashraj','2001')

std1.display()
