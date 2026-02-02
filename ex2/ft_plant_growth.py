class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.old = age

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self.old += 1

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.old} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    inital_height = rose.height
    print("=== Day 1 ===")
    rose.get_info()
    for day in range(6):
        rose.grow()
        rose.age()
    print("=== Day 7 ===")
    rose.get_info()
    print(f"Growth this week: +{rose.height - inital_height}cm")
