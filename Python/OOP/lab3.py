#!/usr/bin/env python3

'''
create class
    person
        hass attribute age
        check if value of age small than 18 raise error 
        "Sorry you age is below eligibility criteria"
        use->     @property,  @age.setter and make age private prop

'''
class Person:
    def __init__(self,age):

         self.age=age

    @property
    def __age(self):
        return self.__age

    @age.setter
    def age(self, age):
        
        if age < 18 : 
            self.__age=0
            raise ValueError("Sorry you age is below eligibility criteria")
        else:
            self.__age=age

p=Person(int(input("enter your age: ")))
print(p.age)
