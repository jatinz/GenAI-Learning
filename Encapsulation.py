class Person:
    def __init__(self,name,age,gender):
        self.__name = name ## PRIVATE VARIABLE
        self._age = age ## PROTECTED VARIABLE
        self.gender = gender ## PUBLIC VARIABLE
    
    def get_age(self):
        return self._age+1

class Emp(Person):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)

    def print_age(self):
        return self.get_age()

def get_person_name(person):
    return person.name

def get_person_gender(person):
    return person.gender


jatin = Person("Jatin",32,"M")
jatin2 = Emp("Jatin",32,"M")
## print(f" :: {get_person_name(jatin)}") ## WILL GIVE ERROR AS NAME IS NOT PUBLIC
print(f" :: {get_person_gender(jatin)}")

print(f" :: {Emp.print_age(jatin2)}")