class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.old = age

    def grow(self):
        self.height += 1

    def age(self):
        self.old += 1

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.old} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    day = 1
    print("=== Day 1 ===")
    rose.get_info()
    for day in range(6):
        rose.grow()
        rose.age()
    print("=== Day 7 ===")
    rose.get_info()
    print("Growth this week: +6cm")
