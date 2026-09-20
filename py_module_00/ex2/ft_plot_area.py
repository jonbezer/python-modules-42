# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_plot_area.py                                   :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: jonbezer <jonbezer@student.42sp.org.br>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/09/20 18:55:53 by jonbezer         #+#    #+#              #
#    Updated: 2026/09/20 18:55:55 by jonbezer        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def ft_plot_area() -> None:
    length: int = int(input("Enter length: "))
    width: int = int(input("Enter width: "))
    area: int = length * width

    print(f"Plot area: {area}")
