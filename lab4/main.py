class Farm:
    def __init__(self,loc, anim, vent_pow):
        self.location = loc
        self.animals_count = anim
        self.vent_power = vent_pow


pigfarm = Farm('Basiwka', 30, 50)

print(pigfarm.location)