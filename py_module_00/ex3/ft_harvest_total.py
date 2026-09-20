# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_harvest_total.py                               :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: jonbezer <jonbezer@student.42sp.org.br>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/09/20 18:57:38 by jonbezer         #+#    #+#              #
#    Updated: 2026/09/20 18:57:47 by jonbezer        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def ft_harvest_total() -> None:
    day_1: int = int(input("Day 1 harvest: "))
    day_2: int = int(input("Day 2 harvest: "))
    day_3: int = int(input("Day 3 harvest: "))
    total: int = day_1 + day_2 + day_3

    print(f"Total harvest: {total}")
