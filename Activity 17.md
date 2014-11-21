### Create a social security number module
##### Create a social security number class:
```python
class SS:
    class InvalidSocial(ValueError):
        pass
    def __init(self):
        self.social = self.getss
    
    def validatess(self):
        check that self.ss is valid
        Anywhere that you find the ss is invalid raise self.InvalidSocial
    
    def getsocial(self):
        self.ss = input("Social: ")
        try
            self.validatess()
        except InvalidSocial:
            print("Invalid SS, please try again\n")
            self.getsocial()        
        
        
```
- validate should check that a valid ss number has been put in. If not it should raise the InvalidSocial exception. Since InvaldSocial is inside the class you will have to call it with self.InvalidSocial.

#### Create the module
- put the code for this module in a file ss.py

### Create an employee module
#### Create an employee class
1. Your first line of code should be 
```python
from ss import *
```
2. Your class should have an __init__ method with an optional dictionary parameter: {social:[last,first,start,pay_rate]}. 
```python
    def __init__(self,{social:[last,first,start,pay_rate]})
```
Where social is SS class, first, last, and start are strings, and pay_rate is a float. 
- check to see if first is None, if so then input the employee.
- if first is not None, then
```python
    self.first = first
    self.last = last
    self.start = start
    self.payrate = rate
    self.ss = social
```

3. Create a __str__ method that returns a string with all the employee information in a nicely formatted string.

#### Create the module
- put the code from this module in a file employee.py

### Create an employee database

#### Import the employee module
from employee import *

#### Create an empty employee list
empl = 
