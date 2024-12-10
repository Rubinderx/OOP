class Person():
    def __init__(self, person_name, person_age, person_height):
        self.name = person_name
        self.age = person_age
        self.height = person_height
    
    def introduce(self):
        print(f"Hi, I'm {self.name}, I'm {self.age} years old and I'm a {self.height} build.")

robin = Person("Robin", 25, "Medium")

robin.introduce()
