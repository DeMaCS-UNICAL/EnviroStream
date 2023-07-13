#!/usr/bin/python3

import math

## Humidex computation
#---
# Compute the humidex from temperature T (in degrees Celsius) and relative humidity H (in %).
def compute_humidex(temperature,humidity):
    temperature = float(temperature)
    humidity= float(humidity)
    dewpoint = (temperature - ((100-humidity)/5)) + 273.15
#    h = (0.5555)*(6.11*math.exp(5417.7530*((1/273.15)-(1/dewpoint)))-10)

    return int(temperature+((0.5555)*(6.11*math.exp(5417.7530*((1/273.15)-(1/dewpoint)))-10)))
    
## Beaufort scale computation
#---
# Return the Beaufort scale number for a given wind speed in m/s.
def beaufort_scale(wind_speed):
    wind_speed = float(wind_speed)
    if wind_speed <0.3:
        return 0
    elif wind_speed <1.6:
        return 1
    elif wind_speed <3.4:
        return 2
    elif wind_speed <5.5:
        return 3
    elif wind_speed <8.0:
        return 4
    elif wind_speed <10.8:
        return 5
    elif wind_speed <13.9:
        return 6
    elif wind_speed <17.2:
        return 7
    elif wind_speed <20.8:
        return 8
    elif wind_speed <24.5:
        return 9
    elif wind_speed <28.5:
        return 10
    elif wind_speed <32.7:
        return 11
    else:
        return 12
    

## Greater equal than
#---
# Greater or equal than comparison between two values.
def geq(a,b):
    return float(a) >= float(b)

## Greater than
#---
# Greater than comparison between two values.
def gt(a,b):
    return float(a) > float(b)

## Less equal than
#---
# Less or equal than comparison between two values.
def leq(a,b):
    return float(a) <= float(b)


## Less than
#---
# Less than comparison between two values.
def lt(a,b):
    return float(a) < float(b)


## Sum between two values
#---
# Sum between two values.
def sum(a,b):
    return str(float(a)+float(b))

## Division between two values
#---
# Division between two values.
def div(a,b):
    return str(float(a)/float(b))


print(compute_humidex(21,45))
