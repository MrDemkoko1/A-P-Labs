class Farm:

    pub_number = 100
    pub_string = 'Info'

    def __init__(self, location, animals_qty, vent_power, milk):
        self.__location = location
        self.__animals_qty = animals_qty
        self.__vent_power = vent_power
        self.__amount_of_milk = milk
        print('Farm has been created')

    def __del__(self):
        print('Farm has been deleted')

    def get_location(self):
        return self.__location
    
    def get_animals_qty(self):
        return self.__animals_qty
    
    def get_vent_power(self): 
        return self.__vent_power

    def get_amount_of_milk(self):
        return self.__amount_of_milk

    def add_milk(self, additional_milk):
        if additional_milk >= 0:
            self.__amount_of_milk += additional_milk

    def efficiency(self):
        if self.__animals_qty > 0:
            return self.__amount_of_milk / self.__animals_qty
        return 0

    def __str__(self):
        return f"Location: {self.__location}, Animals: {self.__animals_qty}, Fan Power: {self.__vent_power}W"

    def __repr__(self):
        return f"Farm(location='{self.__location}', num_animals={self.__animals_qty}, fan_power={self.__vent_power}"


def main():
    farm1 = Farm('Lviv', 30, 300, 28)
    farm2 = Farm('Drogobych', 50, 350, 38)
    farm3 = Farm('Ternopil', 123, 430, 125)

    farm1.add_milk(35)
    farm2.add_milk(44)
    farm3.add_milk(56)

    farms = [farm1, farm2, farm3]

    highest_efficiency = 0
    most_efficient_farm = farms[0]

    for farm in farms:
        if farm.efficiency() > highest_efficiency:
            highest_efficiency = farm.efficiency()
            most_efficient_farm = farm

    print(f'Farm 1:\n {farm1}')
    print(f'Farm 2:\n {farm2}')
    print(f'Farm 3:\n {farm3}')
    print(f'The most efficient farm is:\n {most_efficient_farm}\n with efficiency {highest_efficiency}')

main()