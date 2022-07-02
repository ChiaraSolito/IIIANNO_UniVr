from typing import List, Tuple

def estremi(lista : List[int]) -> Tuple[int, int]:
    return (lista.index(min(num for num in lista)),lista.index(max(num for num in lista)))

def somma_estremi(lista : List[int]) -> int:
    sum = 0
    for i in range(min(estremi(lista)), max(estremi(lista)) + 1):
        sum = sum + lista[i]
    return sum

lista = [ 1, 2, 3, 4, 5 ]   
print(somma_estremi(lista))