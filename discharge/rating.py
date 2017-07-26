# -*- coding: utf-8 -*-
""" This module defines stream rating functions.

Station 148: Allerton Trust Farm
--------------------------------
Discharge is calculated using the equation for open channel flow through a 
a 45 degree v-notch weir:

                  Q = Cd * sqrt(g) * tan (theta/2) * (h)^(5/2)

where Cd is the discharge coefficient, g is the gravitational acceleration, h is 
the head drop (m), theta is the notch angle (45 degrees):

                  Cd = (8*sqrt(2))/15

For efficiceny the first three terms are combined into a single coeffecient:

                  K_148 = Cd * sqrt(g) * tan(theta/2)

"""

__version__ = '0.0.1'
__author__  = 'Tim Hodson'

from math import *

g = 9.81 # Acceleration of gravity

def rating_148(depth):
    """Calculate discharge at station 148 from a depth log

    Args:
        depth (array): Water depth used to calculate discharge.

    Returns:
        Q (array): Calculated discharge.
    """

    K_148 = (8*sqrt(2))/15 * sqrt(g) * tan( radians(45/2) )
    bhead = 260 #mm
    h = (depth - bhead)/1000
    h[ h < 0 ] = 0

    Q = K_148 * h**(5/2)
    return Q

def get_rating(station):
    """This function returns the rating curve of station

    Args:
        station (str): Three digit ISWS station number.

    Returns:
        rating (function): Rating function for the given station.
    """

    rating = {
    '148': rating_148
    }[station]

    return rating



