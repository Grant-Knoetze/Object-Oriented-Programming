class DevAsset:
    companyName = "Developer Laboratory"  # Class variable is available to every instance of this class

    def __init__(self, Psalary):
        self.salary = Psalary  # Instance variable is available only to this method

    def printInfo(self):  # this method prints the value of companyName and salary
        print("Company name is", DevAsset.companyName)
        print("Salary is", self.salary)


# After defining the DevAsset class, we create two instances of said class

Jake = DevAsset(3000)
Smith = DevAsset(4000)

# We change the name of the company effectively changing the class variable which affects instances in the DevAsset class.

DevAsset.companyName = "Developer School"
print(Jake.companyName)
print(Smith.companyName)

# Here we change the DevAsset Jake instance salary which only affects the Jake instance in the DevAsset class.

Jake.salary = 5000
print(Jake.salary)
print(Smith.salary)


