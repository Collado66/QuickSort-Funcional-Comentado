# Implementação funcional de QuickSort em Python
# Programação funcional: evita mutações e usa recursão + funções puras

def quicksort(lista):
    # Caso base: se a lista tiver 0 ou 1 elemento, já está ordenada
    if len(lista) <= 1:
        return lista

    # Escolhemos o primeiro elemento como pivô
    pivot = lista[0]

    # Particionamento funcional:
    # Usamos compreensões de lista para gerar novas listas
    # sem alterar a lista original
    menores = [x for x in lista[1:] if x <= pivot]  # elementos <= pivô
    maiores = [x for x in lista[1:] if x > pivot]   # elementos > pivô

    # Recursão funcional:
    # Ordenamos as sublistas e as concatenamos com o pivô no meio
    return quicksort(menores) + [pivot] + quicksort(maiores)


# Exemplo de uso
valores = [33, 10, 55, 26, 17, 42, 9]
print("Lista original:", valores)
print("Lista ordenada (QuickSort funcional):", quicksort(valores))
