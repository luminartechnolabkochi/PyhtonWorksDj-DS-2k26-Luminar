

class SuperHero:

    name:str

    power:str

    universe:str


    def __init__(self,name,power,universe):

        self.name = name

        self.power = power

        self.universe = universe

    
    def display(self):

        print(f"Name:{self.name} Power:{self.power} Universe:{self.universe}")


bat_man_instance=SuperHero("bat_man","fly","bc") #bat_man

hea_man=SuperHero("heman","jump","bc") #heman

bat_man_instance.display()

hea_man.display()



