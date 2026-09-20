# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_count_harvest_iterative.py                     :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: jonbezer <jonbezer@student.42sp.org.br>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/09/20 18:59:22 by jonbezer         #+#    #+#              #
#    Updated: 2026/09/20 18:59:25 by jonbezer        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def ft_count_harvest_iterative() -> None:
    days: int = int(input("Days until harvest: "))

    for day in range(0, days):
        print(f"Day {day}")

    print("Harvest time!")
