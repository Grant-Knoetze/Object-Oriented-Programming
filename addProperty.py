# To demonstrate how properties work we add one to the variable position
# to ensure that it can only be set to 'Basic' or 'Manager'

class Staff:

    def __init__(self, pPosition, pName, pPay):
        self._position = pPosition  # Change to _position to signal other programmers not to touch variable
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
