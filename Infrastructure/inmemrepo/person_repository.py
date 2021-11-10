from Domain.Entities import *
import random
from Validators.Entity_validators import *
from Extra_module.IterableStructure import *


class PersonRepo:
    """
    This class will create the repository of a 'Person' object
    """
    def __init__(self):
        """
        This method is the instantiation of the 'Repo_person class'
        :_entities: is a list which will keep all the given persons
        """
        self._entities = IterableDataStruct()
        self.valid_person = ValidatePerson()

    def get_all(self):
        return self._entities[:]

    def create_person_object_from_string(self, person_attributes_list):
        """
        This method will transform the attributes of a person given as a string into a 'Person' object
        :param person_attributes_string: attributes of a person (type: string)
        :return: a 'Person' object with the given attributes
        """
        person_attributes_list[0] = str(person_attributes_list[0])
        person_id = person_attributes_list[0].strip()
        name = person_attributes_list[1].strip()
        phone_number = person_attributes_list[2].strip()
        self.valid_person.validate_from_list(person_id, phone_number)
        return Person(person_id, name, phone_number)

    def add_person(self, person_attributes_string):
        """
        This method will add a new person to the entities list with the given attributes after
        those were converted into a 'Person' object
        :param person_attributes_string: attributes of a person (type: string)
        :return: append a new person object to the entities list
        """
        person = self.create_person_object_from_string(person_attributes_string)

        for element in self._entities:
            if element.person_id == person.person_id:
                raise PersonValidateException("Person ID is already used!")
        self._entities.append_iter(person)

    def generate_default_persons_list(self):
        """
        This method will generate a random list and will append to '_entity' which will be the default persons list
        :return: append to '_entities' the random generated list of person object
        """
        name_list = ['Bon Scott', 'Angus Young', 'Brian Johnson', 'Malcom Young', 'Phil Rudd', 'Curt Kobain', 'Gerard Way', 'Frank Lero', 'Mikey Way', 'Chester Bennington', 'Mike Shinoda']
        phone_number_list = ['0745233245', '0745253245', '0745233380', '0745233421', '0770123323', '0770135342', '0359323256', '0356123074', '0356154074', '0770123518']
        frequency_name_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        frequency_phone_number_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(1, 11):
            ok1 = 0
            while ok1 == 0:
                local_name = random.choice(name_list)
                for j in range(11):
                    if local_name == name_list[j]:
                        if frequency_name_list[j] == 0:
                            name = local_name
                            frequency_name_list[j] = 1
                            ok1 = 1
                            break
            ok2 = 0
            while ok2 == 0:
                local_phone_number = random.choice(phone_number_list)
                for j in range(10):
                    if local_phone_number == phone_number_list[j]:
                        if frequency_phone_number_list[j] == 0:
                            phone_number = local_phone_number
                            frequency_phone_number_list[j] = 1
                            ok2 = 1
                            break
                if 0 not in frequency_phone_number_list:
                    break
            person_attributes_as_string = [str(i), name, phone_number]
            person = self.create_person_object_from_string(person_attributes_as_string)
            self._entities.append_iter(person)

    def remove_by_id_person(self, given_id):
        """
        This method will remove a person with the given id from our person list
        :param given_id: person's ID to be removed from person list (type: positive integer)
        :return: remove from '_entities' the person which had that given ID
        """
        self.valid_person.validate_person_id(given_id)
        given_id = int(given_id)
        ok = 0
        for index in range(self._entities.get_length()):
            element = self._entities.__getitem__(index)
            if element.person_id == given_id:
                removed_person = element
                self._entities.__delitem__(index)
                ok = 1
                break

        if ok == 0:
            raise PersonValidateException("The person with the given ID does not exit in persons list")

        return removed_person

    def update_phone_number(self, given_id, new_phone_number):
        """
        This method will change the phone number of a person (given by it's id) with 'new_phone_number'
        :param given_id: person's ID to be updated from person list (type: integer)
        :param new_phone_number: the new phone number to change the old one of this person's ID (type: string of 10 digits)
        :return: change the oldphone number
        """
        changed_phone = ''
        self.valid_person.validate_person_id(given_id)
        given_id = int(given_id)
        self.valid_person.validate_phone_number(new_phone_number)
        ok = 0
        for index in range(self._entities.get_length()):
            element = self._entities.__getitem__(index)
            if element.person_id == given_id:
                ok = 1
                changed_phone = element.phone_number
                element.phone_number = new_phone_number
        if ok == 0:
            raise PersonValidateException("The person with the given ID does not exit in persons list")
        return changed_phone

    def replace_old_person_with_new_person_by_id(self, old_id, new_person):
        """
        This function will replace the person with 'old_id' value in '_entities' with 'new_person' value
        @param old_id: the value to be replaced (type: positive integer)
        @param new_person: the value to replace the old_number value (type: string)
        @return: update '_entities' replacing person with the 'old_id' value with 'new_person' value
        """
        self.valid_person.validate_person_id(old_id)
        old_id = int(old_id)
        old_person = self.remove_by_id_person(old_id)
        self.add_person(new_person)
        return old_person

    def reversed_replace_by_id(self, old_person, new_id):
        self.remove_by_id_person(new_id)
        self.add_person(old_person)

    @staticmethod
    def transform_person_list_to_string(given_list):
        persons_string_list = []
        for element in given_list:
            persons_string_list .append((str(element.person_id) + ', ' + str(element.name) + ', ' + str(element.phone_number)))

        return persons_string_list

    def get_persons_id(self):
        persons_id_list = []
        for element in self._entities:
            persons_id_list.append(element.person_id)
        return persons_id_list

    @staticmethod
    def transform_json_dict_to_list(given_dict):
        return [given_dict["id"], given_dict["name"], given_dict["phone"]]

    @staticmethod
    def transform_person_to_json_dict(given_person):
        json_dict = {
            "id": str(given_person.person_id),
            "name": given_person.name,
            "phone": given_person.phone_number
        }
        return json_dict

    @staticmethod
    def person_name_acceptance(given_name):
        given_name = given_name.lower()

        def check_acceptance_name(person_object):

            if given_name not in person_object.name.lower():
                return True
            else:
                return False
        return check_acceptance_name

    @staticmethod
    def person_phone_acceptance(given_phone):

        def check_acceptance_phone(person_object):
            if given_phone not in person_object.phone_number:
                return True
            else:
                return False

        return check_acceptance_phone