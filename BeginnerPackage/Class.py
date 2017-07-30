import random
import os
import sys

class Animal:

    __name = ""
    __height = 0
    __weight = 0

    def __init__(self, name, height, weight):
        self.__name = name
        self.__height = height
        self.__weight = weight

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

    def set_weight(self, weight):
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def get_type(self):
        print("Animal")

    def to_string(self):
        return "{} is {} in weight and {} in height".format(self.__name,
                                                            self.__weight,
                                                            self.__height)

cat = Animal("Tom", 33, 10)

print(cat.to_string())
print(cat.get_name(), cat.get_height(), cat.get_weight())

class Dog(Animal):
    __owner = ""

    def __init__(self, name, height, weight, owner):
        self.__owner = owner
        super(Dog, self).__init__(name, height, weight)

    def set_owner (self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type (self):
        print ("Dog")

    def to_string(self):
        return "{} is {} in weight and {} in height. His owner is {}".format(self.__name,
                                                                             self.__weight,
                                                                             self.__height,
                                                                             self.__owner)