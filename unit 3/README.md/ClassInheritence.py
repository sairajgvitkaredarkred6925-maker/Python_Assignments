#Manager class inherits from Person and Employee class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print('Name :',self.name)
        print('Age :',self.age)           

class Employee:
      def __init__(self, employee_id, salary):
           self.employee_id = employee_id
           self.salary = salary

      def display_info(self):
            print('Employee ID :',self.employee_id)
            print('Salary :',self.salary)   


class Manager(Person, Employee):
     def __init__ (self, name , age , employee_id, salary, department):
          Person.__init__(self, name, age)
          Employee.__init__(self, employee_id, salary)

          self.department = department

     def display_info(self):
          Person.display_info(self)
          Employee.display_info(self)
          print('Department :',self.department)
         
manage = Manager('Sanskar', 19, 'ADT1103', 696769676967, 'AI-DA') 
manage.display_info()