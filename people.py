#myra ribeiro
#2023/01/03
#purpose is to store and print out different job roles for people,their salary and their name

#construct the employee class
class employee:
    #construct and employee with a name and salary
    #@param name - name of employee
    #@param salary - the salary of the employee
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
    
    #construct a string representation of the employee
    #return the string with datails of the employee
    def __repr__(self):
        return f"{self._name}, has a salary of {self._salary}"

#construct the manager class
class Manager (employee) :
    ## Construct a new manager with a name, salary and department
    #  @ param name - the name of the manager
    #  @ param salary - the salary of the manager
    #  @ param department - the manager's department
    #
    
    def __init__ (self, name, salary, department) :
        super().__init__ (name, salary)
        self._department = department
        
    ## Construct a string representation of the manager
    #  @return a string containing the details of the manager
    #
    
    def __repr__ (self) :
        return self._name + " has a salary of %.2f" % self._salary + " and manages the " + self._department + " department"
#construct the executive class
class executive(Manager):
    #print out the previous result of the executive employee
    #return a string containing details of the executive
    def __repr__(self):
        return f"{self._name}, who is an executive, has a salary of {self._salary} and manages the {self._department} department"


  