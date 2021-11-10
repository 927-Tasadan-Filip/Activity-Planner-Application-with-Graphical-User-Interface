from Infrastructure.inmemrepo.person_repository import *
import json


class PersonJsonRepository(PersonRepo):

    def __init__(self, filename):
        PersonRepo.__init__(self)
        self.__filename = filename

    def read_all_from_file(self):

        with open(self.__filename, "r") as file:
            try:
                data = json.load(file)
                for person in data["persons"]:
                    person = PersonRepo.transform_json_dict_to_list(person)
                    PersonRepo.add_person(self, person)
            except json.decoder.JSONDecodeError:
                pass
        file.close()

    def __write_all_to_file(self):
        data = {"persons": []}
        persons_as_object = PersonRepo.get_all(self)
        for element in persons_as_object:
            persons_as_json_dict = PersonRepo.transform_person_to_json_dict(element)
            data["persons"].append(persons_as_json_dict)
        with open(self.__filename, "w") as file:
            json.dump(data, file)
            file.close()

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

