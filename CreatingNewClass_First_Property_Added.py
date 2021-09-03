
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


            
            
        
    
