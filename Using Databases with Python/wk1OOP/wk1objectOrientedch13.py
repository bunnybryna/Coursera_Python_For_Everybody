#eg1 object oriented
class PartyAnimal:
    x = 0
    # first parameter is by convention is always self
    # moment of creation
    def __init__(self):
        print "I am constructed"
    
    def party(self):
        self.x = self.x + 1
        print "So far",self.x
    # moment of destruction
    def __del__(self):
        print "I am destructed", self.x
an = PartyAnimal()
an.party()
an.party()
an.party()
# <type 'instance'>
print "Type", type(an)
# Dir ['__doc__','__module__','party','x']
print "Dir", dir(an)

#eg2 obejct life cycle
class PartyAnimal:
    x = 0
    name = ""
    def __init__(self,nam):
        self.name = nam
        print self.name, "constructed"
     
    def party(self):
        self.x = self.x + 1
        print self.name, "party count", self.x
        
s = PartyAnimal("Sally")
s.party()

#j = PartyAnimal("Jim")
#j.party()
#s.party()        

#eg 3 inheritance
class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print self.name, "points", self.points
        
j = FootballFan("Jim")
j.party()
j.touchdown()
