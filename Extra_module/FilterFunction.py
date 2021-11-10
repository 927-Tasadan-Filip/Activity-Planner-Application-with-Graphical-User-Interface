def filter_by_given_comparison(list_to_filter, comparison_function):
    """
    #TODO: SPECS
    """
    filtered_list = []
    for element in list_to_filter:
        if comparison_function(element) is False:
            filtered_list.append(element)
    return filtered_list
