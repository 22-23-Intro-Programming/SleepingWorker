class Zoo:
    def __init__(self):
        self.animals = ["tiger" , "shark", "turtle"]
        self.habitats = ["jungle", "fish_tank", "small_fish_tank"]
        self.ticketPrice = 100
        self.maxCapacity = 1000

    def getAnimals(self):
        final = ""
        for i in self.animals:
            final += i + " "
        print(final)

    def getHabitats(self):
        final = ""
        for i in self.habitats:
            final += i + " "
        print(final)

    def whereLive(self, animal):
        print(self.habitats[self.animals.index(animal)])

    def whatLive(self, habitat):
        print(self.animals[self.habitats.index(habitat)])
    
    def addAnimal(self, newAnimal, newHabitat):
        self.animals.append(newAnimal)
        self.habitats.append(newHabitat)
        
    

def main():
    zoo = Zoo()
    zoo.getAnimals()
    zoo.getHabitats()
    zoo.whereLive("shark")
    zoo.whatLive("fish_tank")
    zoo.addAnimal("monkey", "trees")
    zoo.whereLive("monkey")


main()


        
        
