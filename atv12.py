listas = [["a", "b", "c"], ["d", "e"], ["f", "g", "h"]]

resultado = [item for sublista in listas for item in sublista]

print(resultado)
