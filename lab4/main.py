class Farm:

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