# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_seed_inventory.py                              :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: jonbezer <jonbezer@student.42sp.org.br>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/09/20 18:54:21 by jonbezer         #+#    #+#              #
#    Updated: 2026/09/20 18:54:40 by jonbezer        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    formated_seed: str = seed_type.capitalize()

    if unit == "packets":
        print(f"{formated_seed} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{formated_seed} seeds: {quantity} grams total0")
    elif unit == "area":
        print(f"{formated_seed} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
