class Pakuri:

    def __init__(self, species):
        self.species = species
        self.attack = (len(self.species) * 7) + 9
        self.defense = (len(self.species) * 5) + 17
        self.speed = (len(self.species) * 6) + 13

    def get_species(self):
        return self.species

    def get_attack(self):
        return self.attack

    def get_defense(self):
        return self.defense

    def get_speed(self):
        return self.speed

    def set_attack(self, new_attack):
        self.attack = new_attack

    def evolve(self):
        self.attack *= 2
        self.defense *= 4
        self.speed *= 3


