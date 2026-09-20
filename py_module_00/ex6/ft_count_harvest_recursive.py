def ft_count_harvest_recursive() -> None:
    days: int = int(input("Days until harvest: "))

    def counter(current: int) -> None:
        if current > days:
            print("Harvest time!")
            return
        print(f"Day {current}")
        counter(current + 1)

    counter(1)
