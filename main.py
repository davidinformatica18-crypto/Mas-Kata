def string_calculator(numeros):
    if numeros == "":
        return 0

    numeros = numeros.replace("\n", ",")

    lista = numeros.split(",")

    total = 0

    for n in lista:
        total += int(n)

    return total
