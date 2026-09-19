def ft_count_harvest_iterative() -> None:
    days: int = int(input("Days until harvest: "))

    for day in range(0, days):
        print(f"Day {day}")

    print("Harvest time!")
