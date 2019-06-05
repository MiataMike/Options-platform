import math
#from .black_scholes import bsPut

def vol(current_price, target_price, percent_year):
    return math.log(target_price/current_price)/percent_year

def day2yr(days):
   return days/250
