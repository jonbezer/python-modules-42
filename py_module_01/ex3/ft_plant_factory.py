#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"Created: {self.name.capitalize()}: {self.height:.1f}cm, "
              f"{self.age} days old")


if __name__ == "__main__":
    rose = Plant("rose", 25.0, 30)
    oak = Plant("oak", 200.0, 365)
    cactus = Plant("cactus", 5.0, 90)
    sunflower = Plant("sunflower", 80.0, 45)
    fern = Plant("fern", 15.0, 120)

    print("=== Plant Factory Output  ===")
    rose.show()
    oak.show()
    cactus.show()
    sunflower.show()
    fern.show()
