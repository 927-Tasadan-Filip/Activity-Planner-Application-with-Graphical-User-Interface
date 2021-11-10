from Infrastructure.inmemrepo.person_repository import *


class PersonTextRepository(PersonRepo):

    def __init__(self, filename):
        PersonRepo.__init__(self)
        self.__filename = filename

    def read_all_from_file(self):

        file_to_read = open(self.__filename, 'r')
        for line in file_to_read:
            line = line.strip()
            if line != "":
                line = line.split(",")
                try:
                    PersonRepo.add_person(self, line)
                except:
                    pass
        file_to_read.close()
        
    def __write_all_to_file(self):

        file_to_write = open(self.__filename, 'w')
        persons_as_string = PersonRepo.transform_person_list_to_string(self._entities)
        for element in persons_as_string:
            file_to_write.write(element + "\n")
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
