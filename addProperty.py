<<<<<<< HEAD
# To demonstrate how properties work we add one to the variable position
# to ensure that it can only be set to 'Basic' or 'Manager'

class Staff:

    def __init__(self, pPosition, pName, pPay):
        self._position = pPosition # Change to _position to signal other programmers not to touch variable
        self.name = pName
        self.pay = pPay
        print("Creating Staff object")


    """__str__ is another special method commonly included 
    when coding a class. We use it to return a human readable 
    string that represents the class"""

    def __str__(self):
        return "Position = %s, Name = %s, Pay = %d" % (
            self._position,
            self.name,
            self.pay,
        )

    @property
    def position(self):
        print("Getter Method")
        return self._position

    @position.setter
    def position(self, value):
        if value == 'Manager' or value == 'Basic':
            self._position = value
        else:
            print('Position is invalid. No changes made')

    def calculatePay(self):
        prompt = "\nEnter number of hours worked for %s: " % (self.name)
        hours = input(prompt)
        prompt = "Enter the hourly rate for %s: " % (self.name)
        hourlyRate = input(prompt)
        self.pay = int(hours) * int(hourlyRate)
        return self.pay
=======

class Athlete:
    def __init__ (self, pDiscipline, pName, pExperiencePoints):
        self._discipline = pDiscipline
        self.name = pName
        self.experiencepoints = pExperiencePoints
        print('Creating Athlete object')

    def __str__ (self):
        return "Discipline = %s, Name = %s, ExperiencePoints = %d" %(self._discipline, self.name, self.experiencepoints)

    def calculateExperiencePoints(self):
        prompt = '\nEnter number of hours exercised for %s: ' % (self.name)
        hours = input(prompt)
        prompt = 'Enter the hourly EP for %s: ' %(self.name)
        hourlyPoints = input(prompt)
        self.experiencepoints = int(hours)*int(hourlyPoints)
        return self.experiencepoints
    
#Next we add a property for the 'discipline' variable. Illustrating how a property is used to check the value of a change made before it is allowed to occur.
      
    @property
    def discipline(self):
        print("Getter Method")
        return self._discipline

    @discipline.setter
    def discipline(self, value):
        if value == 'Archer' or value == 'Shot Put':
            self._discipline == value
        else:
            print('Discipline is invalid. No changes made.')


            
            
        
    
>>>>>>> 137ac9dcd98a7653d8a888a471a584df5d29db17
