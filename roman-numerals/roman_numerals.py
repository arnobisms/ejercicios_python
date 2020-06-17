def roman(numero):
    if numero >= 1000:
        return "{}{}".format("M", roman(numero - 1000))
    elif numero >= 900:
        return "{}{}".format("C", roman(numero + 100))
    elif numero >= 500:
        return "{}{}".format("D", roman(numero - 500))
    elif numero >= 400:
        return "{}{}".format("C", roman(numero + 100))
    elif numero >= 100:
        return "{}{}".format("C", roman(numero - 100))
    elif numero >= 90:
        return "{}{}".format("X", roman(numero + 10))
    elif numero >= 50:
        return "{}{}".format("L", roman(numero - 50))
    elif numero >= 40:
        return "{}{}".format("X", roman(numero + 10))
    elif numero >= 10:
        return "{}{}".format("X", roman(numero - 10))
    elif numero >= 9:
        return "{}{}".format("I", roman(numero + 1))
    elif numero >= 5:
        return "{}{}".format("V", roman(numero - 5))
    elif numero >= 4:
        return "{}{}".format("I", roman(numero + 1))
    elif numero > 0:
        return "{}{}".format("I", roman(numero - 1))
    else:
        return ""
