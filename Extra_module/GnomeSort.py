def gnome_sort(list_to_sort, comparison_function):
    position = 0
    while position < len(list_to_sort):
        if position == 0 or (comparison_function(list_to_sort[position - 1], list_to_sort[position]) is True):
            position += 1

        else:
            list_to_sort[position - 1], list_to_sort[position] = list_to_sort[position], list_to_sort[position - 1]
            position -= 1

    return list_to_sort
