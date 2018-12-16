from random import random, gauss

def weather():
    '''Update weather state in the shared memory'''
    current_weather = weather_in_shared_memory
    return fonction_meteo_selon_gauss(current_weather)

def fonction_meteo_selon_gauss(degre):
    variation = degre - 10
    if variation > 0:
        return degre + gauss(-1, variation)
    else:
        return degre + gauss(1, variation)


def fonction_meteo_selon_data(t):
    pass
