# Module 9 - Skill Building Exercise No. 2 Solution
# Author: Bruce Elgort
# Date: July 22, 2017
# Update: February 25, 2019

class Student:

    def __init__(self,first,last,gender,gpa,degree,birthday,courses):
        self.__first_name = first
        self.__last_name = last
        self.__gender = gender
        self.__gpa = gpa
        self.__degree = degree
        self.__birthday = birthday
        self.__courses = courses

    def setGPA(self,gpa):
        self.__gpa = gpa

    def getGPA(self):
        return self.__gpa

    def setCourse(self,course):
        self.__courses.append(course)

    def getCourses(self):
        return self.__courses

def main():    
    bruce = Student("Bruce","Elgort","Male","4.0","Web Development","7/2/1963",['CTEC121','CTEC122'])
    shawn = Student("Shawn","Chandra","Male","3.0","AAT Transfer","8/1/2000",['CTEC121','CTEC126','CTEC227'])

    bruce.setGPA(2.0)
    print(bruce.getGPA())
    bruce.setCourse('Basket Weaving')
    print(bruce.getCourses())


main()