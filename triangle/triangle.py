def validar(lados):
    a, b, c = sorted(lados)
    return c <= a + b and a > 0


def equilateral(lados):
    a, b, c = lados
    return validar(lados) and a == b and a == c


def isosceles(lados):
    a, b, c = lados
    return validar(lados) and (a == b or a == c or b == c)


def scalene(lados):
    a, b, c = lados
    return validar(lados) and a != b and a != c and b != c
