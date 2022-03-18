from Utils.testUtils import class_test
from abc import ABC, abstractmethod

class Human(ABC):
   
    @abstractmethod
    def __init__(self, name, age):
        """
        Create a human basis as part of a child instance.
        """
       
        self._name = name
        self._age = age
   
    @property
    def name(self):
        return self._name
   
    @name.setter
    def name(self, name):
        self._name = name
       
    @property
    def age(self):
        return self._age
   
    @age.setter
    def age(self, age):
        self._age = age
   
class Student(Human):
    def __init__(self, name, age, grades):
        """
        Create a student instance.
        """
        super().__init__(name, age)
        self._grades = grades
       
    def get_avg(self):
        """
        >>> test_obj.get_avg()
        98
        """
        return sum(self.grades)//len(self.grades)
   
    @property
    def grades(self):
        return self._grades
   
    @grades.setter
    def grades(self, grades):
        self._grades = grades
   
    @property
    def age(self):
        return self._age
   
    @classmethod
    def get_example_obj(cls): return cls("moshe" , 6, [92, 98]) # Return example Student instance
       
       
    @classmethod
    def overall_test(cls):
        """
        Test the whole class, based on one global object.
       
        test_obj - object to test the class with, initialize using get_example_object.
        """
       
        test_obj = cls.get_example_obj()
        class_test(test_obj)
       


if __name__ == '__main__':
    Student.overall_test()
    