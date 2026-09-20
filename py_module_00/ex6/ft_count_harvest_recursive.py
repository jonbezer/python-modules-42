# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_count_harvest_recursive.py                     :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: jonbezer <jonbezer@student.42sp.org.br>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/09/20 18:59:30 by jonbezer         #+#    #+#              #
#    Updated: 2026/09/20 18:59:34 by jonbezer        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def ft_count_harvest_recursive() -> None:
    days: int = int(input("Days until harvest: "))

    def counter(current: int) -> None:
        if current > days:
            print("Harvest time!")
            return
        print(f"Day {current}")
        counter(current + 1)

    counter(1)
