def ft_plant_age() -> None:
    age_plant: int = int(input("Enter age in days: "))
    if age_plant > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
