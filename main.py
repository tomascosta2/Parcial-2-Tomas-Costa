def test(adn):
    def esMutante(secuencia):
        # secuencia[i:i+4] es como un "slice"
        # A * 4 = AAAA
        return any(secuencia[i:i+4] == secuencia[i]*4 for i in range(len(secuencia)-3))

    # Filas
    if any(esMutante(fila) for fila in adn):
        return True

    # Columnas
    if any(esMutante(''.join(adn[i][j] for i in range(len(adn)))) for j in range(len(adn[0]))):
        return True

    # Diagonales
    if any(esMutante(''.join(adn[i+k][j+k] for k in range(4))) for i in range(len(adn)-3) for j in range(len(adn[0])-3)):
        return True

    if any(esMutante(''.join(adn[i-k][j+k] for k in range(4))) for i in range(3, len(adn)) for j in range(len(adn[0])-3)):
        return True

    return False


# adn = ["ATGCGA", "CDGTGC", "TTATST", "AGAAGG", "CCCDTA", "TCACTG"]

adn = []
letras = 'ACGT'

while(len(adn) < 6) :
    print('Ingrese el subadn')
    aux = input()
    if len(aux) == 6 and any(aux[j] in letras for j in range(1,len(aux))) :
        adn.append(aux)
    else :
        print('El subadn debe tener 6 caracteres y solo puede contener las letras A,C,G y T por favor ingreselo de nuevo')
        


if test(adn):
    print("La persona es mutante.")
else:
    print("La persona no es mutante.")