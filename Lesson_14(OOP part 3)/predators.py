# from mammals import mammals
# from my_animals import my_animals


class Predators:
    def __init__(self, name: str, prey: str):
        super().__init__(name)
        self.name = None
        self.prey = prey

    def hunt(self):
        print(f"{self.name} can hunting on {self.prey}.")

    def __str__(self):
        return f"Predator: {self.name} (prey: {self.prey})"

    def print_info(self):
        pass


# print(Predators)
