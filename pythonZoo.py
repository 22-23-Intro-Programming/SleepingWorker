#'class' starts definition of a class
#this class holds habitats and animals
class Zoo:

    #constructor function
    def __init__(self):
        self.animals = ["tiger" , "shark", "turtle"]
        self.habitats = ["jungle", "fish_tank", "small_fish_tank"]
        self.ticketPrice = 100
        self.maxCapacity = 1000

    #returns string with all animals
    def getAnimals(self):
        final = ""
        for i in self.animals:
            final += i + " "
        print(final)

    #returns string with all habitats
    def getHabitats(self):
        final = ""
        for i in self.habitats:
            final += i + " "
        print(final)

    #input animals and returns where it lives
    def whereLive(self, animal):
        print(self.habitats[self.animals.index(animal)])

    #input habitat and returns what lives there
    def whatLive(self, habitat):
        print(self.animals[self.habitats.index(habitat)])

    #input new animal and new habitat and it adds it to the zoo
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


        
        
