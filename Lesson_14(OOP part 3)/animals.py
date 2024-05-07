from mammals import Mammals
from predators import Predators


class Animals:

    def __init__(self, name: str):
        self.name = name

    def live_in_jungle(self):
        print(f"{self.name} they can live in a jungle.")

    def __str__(self):
        return f"Animals: {self.name}"

    def print_info(self):
        """Prints basic info about the animals"""
        print(self)


class Mammals(Animals):

    def __init__(self, name: str, diet: str = "plants"):
        super().__init__(name)
        self.diet = diet

    def eat_plants(self):
        """Simulates a mammal eating plants."""
        print(f"{self.name} eats {self.diet}.")

    def print_info(self):
        super().print_info()  # Call parent class print_info
        print(f"Diet: {self.diet}")


class Predators(Animals):

    def __init__(self, name: str, prey: str):
        super().__init__(name)
        self.prey = prey

    def hunt(self):
        """Simulates a predator hunting."""
        print(f"{self.name} hunts {self.prey} but not always catch.")

    def print_info(self):  # Overridden print_info for even more details
        super().print_info()  # Call parent class print_info
        print(f"Prey: {self.prey}")


# Create instances
Animals = Animals("General Animals class found")
mammal = Mammals("Zebra")
predator = Predators("Lion", "Zebra")

# Print object information and func
Animals.print_info()
mammal.print_info()
predator.print_info()

print('method to each classes:')
Animals.live_in_jungle()
mammal.eat_plants()
predator.hunt()
