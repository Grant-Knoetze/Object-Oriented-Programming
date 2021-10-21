# We define a class called Staff
# A method is a function that exhists inside of a class and has a method
# self as a parameter.


class Staff:

    """We define a special method called __inint__ for the class
    this __inint__ method is known as the initializer of the class
    it is always named init with two underscores in the front and back
    Initializer is called whenever an object of the class is created
    Used to inilialize the variables (i.e. give them initial values) in the class
    the class
    Writing an initializer is optional if you do not want to
    initialize the instance variables when you create the object
    You can initialize them later."""

    def __init__(self, pPosition, pName, pPay):
        self.position = pPosition
        self.name = pName
        self.pay = pPay
        print("Creating Staff object")

    """__str__ is another special method commonly included 
    when coding a class. We use it to return a human readable 
    string that represents the class"""

    def __str__(self):
        return "Position = %s, Name = %s, Pay = %d" % (
            self.position,
            self.name,
            self.pay,
        )

    def calculatePay(self):
        prompt = "\nEnter number of hours worked for %s: " % (self.name)
        hours = input(prompt)
        prompt = "Enter the hourly rate for %s: " % (self.name)
        hourlyRate = input(prompt)
        self.pay = int(hours) * int(hourlyRate)
        return self.pay
