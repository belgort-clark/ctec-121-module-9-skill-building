# Module 8 - Skill Building Exercise No. 2 Solution
# Author: Bruce Elgort
# Date: July 22, 2017

class Student:
    def __init__(self,first,last,gender,gpa,degree,birthday,courses):
        self.first_name = first
        self.last_name = last
        self.gender = gender
        self.gpa = gpa
        self.degree = degree
        self.birthday = birthday
        self.courses = courses


    def setGPA(self,gpa):
        self.gpa = gpa


    def getGPA(self):
        return self.gpa


    def setCourse(self,course):
        self.courses.append(course)


    def getCourses(self):
        return self.courses

def main():    
    bruce = Student("Bruce","Elgort","Male","4.0","Web Development","7/2/1963",['CTEC121','CTEC122'])
    shawn = Student("Shawn","Chandra","Male","3.0","AAT Transfer","8/1/2000",['CTEC121','CTEC126','CTEC227'])

    bruce.setGPA(2.0)
    print(bruce.getGPA())
    bruce.setCourse('Basket Weaving')
    print(bruce.getCourses())


main()