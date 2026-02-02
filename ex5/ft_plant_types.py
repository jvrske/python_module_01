class Plant:
    def __init__(self, name, height, age) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, color) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!\n")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        shade = self.trunk_diameter * 1.56
        print(f"{self.name} provides {shade} square meters of shade\n")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season,
                 nutritional_value) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def nutri_value(self):
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 25, 30, "red color")
    print(f"{rose.name} ({rose.__class__.__name__}): {rose.height}cm, \
{rose.age} days, {rose.color}")
    rose.bloom()

    oak = Tree("Oak", 500, 1825, 50)
    print(f"{oak.name} ({oak.__class__.__name__}): {oak.height}cm, \
{oak.age} days, {oak.trunk_diameter}cm diameter")
    oak.produce_shade()

    veg = Vegetable("Tomato", 80, 90, "summer harvest", "vitamin C")
    print(f"{veg.name} ({veg.__class__.__name__}): {veg.height}cm, \
{veg.age} days, {veg.harvest_season}")
    veg.nutri_value()
