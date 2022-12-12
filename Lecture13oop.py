class Employee:
    
    counter=0
    def __init__(self , name, age) :
        self.name= name
        self.age= age
        Employee.counter +=1
        
    def display(self):
        print("name=",self.name)
        print("age=",self.age)

    def counters(self):
        print("Number of students", Employee.counter)




obj1=Employee("maryam","50")
obj1.display()
obj1.counters()

obj2=Employee("daniyal","80")
obj2.display()
obj2.counters()