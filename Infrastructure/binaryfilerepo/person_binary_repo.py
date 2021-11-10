from Infrastructure.inmemrepo.person_repository import *
import pickle


class PersonBinaryRepository(PersonRepo):

    def __init__(self, filename):
        PersonRepo.__init__(self)
        self.__filename = filename

    def read_all_from_file(self):

        with open(self.__filename, "rb") as file:
            while True:
                try:
                    person = pickle.load(file)
                except EOFError:
                    person = None
                if person is not None:
                    person = person.split(",")
                    PersonRepo.add_person(self, person)
                else:
                    break
            file.close()

    def __write_all_to_file(self):

        file_to_write = open(self.__filename, 'wb')
        persons_as_string = PersonRepo.transform_person_list_to_string(self._entities)
        for element in persons_as_string:
            pickle.dump(element + "\n", file_to_write)
        file_to_write.close()

    def add_person(self, person):
        PersonRepo.add_person(self, person)
        self.__write_all_to_file()

    def remove_by_id_person(self, person_id):
        removed_person = PersonRepo.remove_by_id_person(self, person_id)
        self.__write_all_to_file()
        return removed_person

    def update_phone_number(self, given_id, new_phone_number):
        changed_phone = PersonRepo.update_phone_number(self, given_id, new_phone_number)
        self.__write_all_to_file()
        return changed_phone

    def replace_old_person_with_new_person_by_id(self, old_id, new_person):
        old_person = PersonRepo.replace_old_person_with_new_person_by_id(self, old_id, new_person)
        self.__write_all_to_file()
        return old_person

    def get_all(self):
        return PersonRepo.get_all(self)
