class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")

    def create_all(plant_templates):
        plants = []
        for name, height, age in plant_templates:
            plants.append(Plant(name, height, age))
        return plants

    def get_info(self):
        print(f"{self.name} ({self.height}cm, {self.age} days)")


if __name__ == "__main__":
    plant_templates = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    print("=== Plant Factory Output ===")
    plants = Plant.create_all(plant_templates)
    i = 0
    for p in plants:
        i += 1
    print(f"\nTotal plants created: {i}")
