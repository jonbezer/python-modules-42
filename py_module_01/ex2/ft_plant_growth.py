#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float,
                 age: int, growth_rate: float) -> None:
        self.name = name
        self.height = height
        self._age = age
        self.growth_rate = growth_rate

    def grow(self) -> None:
        self.height += self.growth_rate

    def age(self) -> None:
        self._age += 1

    def show(self) -> None:
        print(
            f"{self.name.capitalize()}: "
            f"{self.height:.1f}cm, {self._age} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25.0, 30, 0.8)
    print("=== Garden Plant Growth ===")
    rose.show()
    rose_initial_height = rose.height

    for day_r in range(1, 8):
        rose.grow()
        rose.age()
        print(f"=== Day {day_r} ===")
        rose.show()

    total_growth_r = round(rose.height - rose_initial_height, 1)
    print(f"Growth this week: {total_growth_r}cm of Rose")
