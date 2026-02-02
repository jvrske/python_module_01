class Plant:
    def __init__(self, name, height) -> None:
        self.name = name
        self.height = height

    def grow(self) -> None:
        self.height += 1
        print(f"{self.name} grew 1cm")

    def info(self) -> str:
        return f"- {self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name, height, color) -> None:
        super().__init__(name, height)
        self.color = color

    def bloom(self):
        if self.height > 20:
            return True

    def info(self):
        if self.bloom():
            return super().info() + f", {self.color} (blooming)"
        return super().info() + f", {self.color}"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize_points) -> None:
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def info(self):
        return super().info() + f", Prize points: {self.prize_points}"


class Garden():
    def __init__(self, owner) -> None:
        self.plants = []
        self.owner = owner

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")


class GardenManager:
    def __init__(self):
        ...

    class GardenStats():
        def __init__(self, plants, gardens, numbers) -> None:
            self.plants = plants
            self.gardens = gardens
            self.numbers = numbers

        def calculate():
            ...
            return


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")

    plants = [
        Plant("Oak Tree", 100),
        FloweringPlant("Rose", 25, "red flowers"),
        PrizeFlower("Sunflower", 50, "yellow flowers", 10)
    ]
    garden = Garden("Alice")
    for index in plants:
        garden.add_plant(index)

    print("\nAlice is helping all plants grow...")
    for plant in garden.plants:
        plant.grow()

    print("\n=== Alice's Garden Report ===")
    print("Plants in garden:")
    for plant in garden.plants:
        print(plant.info())
