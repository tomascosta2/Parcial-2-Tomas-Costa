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


adn = ["ATGCGA", "CDGTGC", "TTATST", "AGAAGG", "CCCDTA", "TCACTG"]

if test(adn):
    print("La persona es mutante.")
else:
    print("La persona no es mutante.")