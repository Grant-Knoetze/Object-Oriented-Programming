
class Athlete:
    def __init__ (self, pDiscipline, pName, pExperiencePoints):
        self.discipline = pDiscipline
        self.name = pName
        self.experiencepoints = pExperiencePoints
        print('Creating Athlete object')

    def __str__ (self):
        return "Discipline = %s, Name = %s, ExperiencePoints = %d" %(self.discipline, self.name, self.experiencepoints)

    def calculateExperiencePoints(self):
        prompt = '\nEnter number of hours exercised for %s: ' % (self.name)
        hours = input(prompt)
        prompt = 'Enter the hourly EP for %s: ' %(self.name)
        hourlyPoints = input(prompt)
        self.experiencepoints = int(hours)*int(hourlyPoints)
        return self.experiencepoints
    
