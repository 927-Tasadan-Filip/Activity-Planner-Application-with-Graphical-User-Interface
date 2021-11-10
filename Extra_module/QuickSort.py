def partition(lista, left, right):
    index = left - 1
    pivot = lista[right]

    for small_index in range(left, right):
        if lista[small_index] < pivot:
            index += 1
            lista[index], lista[small_index] = lista[small_index], lista[index]

    lista[index + 1], lista[right] = lista[right], lista[index + 1]
    index += 1
    return index


def sort_lista(lista, left, right):
    if left < right:
        partition_index = partition(lista, left, right)

        sort_lista(lista, left, partition_index - 1)
        sort_lista(lista, partition_index + 1, right)


lista = [4,2,7,3,5,1,9,3,1,4,5]
sort_lista(lista, 0, len(lista) - 1)
print(lista)





