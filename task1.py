class Person:
    def __init__(self, name, surname, phone):
        self.name = name
        self.surname = surname
        self.phone = phone

    def get_info(self):
        return f"Name: {self.name}, Surname: {self.surname}, Phone: {self.phone}"

class Student(Person):
    def __init__(self, name, surname, phone, fakultet, rating):
        super().__init__(name, surname, phone)
        self.fakultet = fakultet
        self.rating = rating

    def get_info(self):
        return (super().get_info() + 
                f", Fakultet: {self.fakultet}, Rating: {self.rating}")

student = Student("Saidahmad", "Murodullayev", "+998901234567", "Informatika", 90)
print(student.get_info())
