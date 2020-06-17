from math import sqrt


def score(x, y):
    distancia = sqrt(x**2 + y**2)
    if distancia <= 1:
        return 10
    elif distancia <= 5:
        return 5
    elif distancia <= 10:
        return 1
    return 0
