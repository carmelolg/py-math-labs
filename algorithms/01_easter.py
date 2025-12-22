#!/usr/bin/env python3

import argparse
from datetime import datetime

parser = argparse.ArgumentParser(description='Year to calculate')
parser.add_argument("-Y", default=datetime.now().year, type=int, help="Year to calculate")

args = parser.parse_args()
year = args.Y

def get_gregorian_map_value_by_year(_year: int):
    min_year = 1583
    max_year = 2499

    # Gregorian map for years 1699 to 2499
    _map = {
        1699: {'M': 22, 'N': 2},
        1799: {'M': 23, 'N': 3},
        1899: {'M': 23, 'N': 4},
        2099: {'M': 24, 'N': 5},
        2199: {'M': 24, 'N': 6},
        2299: {'M': 25, 'N': 0},
        2399: {'M': 26, 'N': 1},
        2499: {'M': 25, 'N': 1}
    }

    if _year < min_year or _year > max_year:
        raise ValueError(f"Year must be between {min_year} and {max_year}")

    for key in _map.keys():
        if _year <= key:
            return _map[key]
    return None



# Calculate the month and day of Easter Sunday for the given year
alpha = year % 19
beta = year % 4
gamma = year % 7

gregorian_map = get_gregorian_map_value_by_year(year)
delta = (19 * alpha + gregorian_map['M']) % 30
epsilon = (2 * beta + 4 * gamma + 6 * delta + gregorian_map['N']) % 7

if delta + epsilon < 10:
    month = 3
    day = delta + epsilon + 22
else:
    month = 4
    day = delta + epsilon - 9

print(f"Easter Sunday in {year} falls on {day:02d}/{month:02d}/{year}")