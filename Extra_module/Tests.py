from Extra_module.FilterFunction import *
from Extra_module.GnomeSort import *
from Extra_module.IterableStructure import *
import unittest


class TestExtraModule(unittest.TestCase):

    def setUp(self):
        self.__iter_struct = IterableDataStruct()

    def test_append_iter(self):
        self.__iter_struct.append_iter(1)
        assert self.__iter_struct[0] == 1

        self.__iter_struct.append_iter(2)
        assert self.__iter_struct[1] == 2

    def test_iterable_object(self):
        self.__iter_struct.append_iter(1)
        self.__iter_struct.append_iter(2)
        for index in range(self.__iter_struct.get_length()):
            element = self.__iter_struct.__getitem__(index)
            if index == 0:
                assert element == 1
            elif index == 1:
                assert element == 2

        for element in self.__iter_struct:
            assert (element == 1 or element == 2)

        self.__iter_struct.__delitem__(0)
        assert self.__iter_struct[0] == 2

    def test_gnome_sort(self):
        list_to_sort = [1, 5, 3, 4, 2, 7, 8, 9]

        def comparison_function_test(element_1, element_2):
            if element_1 < element_2:
                return True
            return False
        sorted_list = gnome_sort(list_to_sort, comparison_function_test)
        assert sorted_list == [1, 2, 3, 4, 5, 7, 8, 9]

    def test_filter_function(self):
        list_to_filter = [1, 5, 3, 4, 2, 7, 8, 9]

        def acceptance_function_test(element):
            if element % 2 == 0:
                return True
            return False

        filtered_list = filter_by_given_comparison(list_to_filter, acceptance_function_test)
        assert filtered_list == [1, 5, 3, 7, 9]