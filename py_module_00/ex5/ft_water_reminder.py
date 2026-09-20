# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_water_reminder.py                              :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: jonbezer <jonbezer@student.42sp.org.br>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/09/20 18:58:22 by jonbezer         #+#    #+#              #
#    Updated: 2026/09/20 18:58:23 by jonbezer        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def ft_water_reminder() -> None:
    last_watering: int = int(input("Days since last watering: "))
    if last_watering > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
