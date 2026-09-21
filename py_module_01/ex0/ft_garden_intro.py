#!/usr/bin/env python3

def ft_garden_intro() -> None:
    name_plant: str = "Rose"
    height: int = 25
    age: int = 30

    print("=== Welcome to My garden ===")
    print(f"Plant: {name_plant}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print("\n=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro()
