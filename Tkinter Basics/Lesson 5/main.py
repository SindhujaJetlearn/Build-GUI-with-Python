#class is the blueprint of the object.
class Student:
    #Properties/Attributes
    #inbuilt function
    def __init__(self,name,age,grade,hobby):
        self.name = name
        self.age = age
        self.grade = grade
        self.hobby = hobby
        self.intro = " "
    
    #Functions/Methods
    def displayDetails(self):
        print("The details of the student : ")
        print("Name :",self.name)
        print("Age :",self.age)
        print("Grade :",self.grade)
        print("Hobby :",self.hobby)
    
    def introduction(self):
        self.intro=input("Tell me about yourself : ")
        print(self.intro)

#Creating Object - instance of a class
#once the class is created, it will call the init function automatically
s1=Student("Remi",12,"6th Grade","Coding")
#objectName.functionName()
s1.displayDetails()
print(s1.age)

    


