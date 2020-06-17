def slices(serie, longitud):

    if longitud > len(serie):
        raise ValueError('La longitud no puede ser mayor que la serie')

    resultado = []
    i = 0
    while i + longitud <= len(serie):
        resultado.append(serie[i: i + longitud])
        i += 1
    return resultado
