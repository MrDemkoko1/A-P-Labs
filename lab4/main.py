class Farm:

    pub_number = 100
    pub_string = 'Info'

    def __init__(self, location, animals_qty, vent_power):
        self.__location = location
        self.__animals_qty = animals_qty
        self.__vent_power = vent_power
        print('Farm has been created')

    def __del__(self):
        print('Farm has been deleted')

    def get_location(self):
        return self.__location
    
    def get_animals_qty(self):
        return self.__animals_qty
    
    def get_vent_power(self): 
        return self.__vent_power

    def __str__(self):
        return f"Location: {self.__location}, Animals: {self.__animals_qty}, Fan Power: {self.__vent_power}W"

    def __repr__(self):
        return f"Farm(location='{self.__location}', num_animals={self.__animals_qty}, fan_power={self.__vent_power}"


def main():
    farm1 = Farm('Lviv', 30, 300)
    farm2 = Farm('Drogobych', 50, 350)
    farm3 = Farm('Ternopil', 123, 430)

    print(farm1)
    print(farm2)
    print(farm3)

main()