class Mammals:
    pass


class Mammals:
    def __init__(self, name: str, diet: str = "plants"):
        super().__init__(name)
        self.name = None
        self.prey = None
        self.diet = diet

    def eat_plants(self):
        print(f"{self.name} eats {self.diet}."), str

    def print_info(self):
        print(f"Prey: {self.prey}")

    # print(Mammals)
