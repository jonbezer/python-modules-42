# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_plant_age.py                                   :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: jonbezer <jonbezer@student.42sp.org.br>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/09/20 18:58:12 by jonbezer         #+#    #+#              #
#    Updated: 2026/09/20 18:58:13 by jonbezer        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def ft_plant_age() -> None:
    age_plant: int = int(input("Enter age in days: "))
    if age_plant > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
