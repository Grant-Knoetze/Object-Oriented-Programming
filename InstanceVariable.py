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
