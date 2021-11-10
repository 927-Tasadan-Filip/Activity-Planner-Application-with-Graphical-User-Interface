from Infrastructure.inmemrepo import PersonRepo, PersonValidateException, ActivityValidateException, ActivityRepo
import unittest


class TestPersonRepository(unittest.TestCase):
    def setUp(self):
        self._person_repo = PersonRepo()

    def test_get_all(self):
        assert len(self._person_repo.get_all()) == 0

    def test_create_person_object_from_string(self):
        try:
            new_person = 'SDA, John, 0770190937'
            self._person_repo.create_person_object_from_string(new_person)
        except PersonValidateException:
            assert True

    def test_generate_default_persons_list(self):

        self._person_repo.generate_default_persons_list()
        person_list = self._person_repo.get_all()

        assert len(person_list) == 10
        assert person_list[9].person_id == 10
        assert person_list[0].person_id == 1
        assert len(person_list[5].phone_number) == 10

    def test_add_person(self):

        new_person = ['11', 'Johnny Cash', '0770192937']
        self._person_repo.add_person(new_person)
        assert self._person_repo._entities[0].person_id == 11
        assert self._person_repo._entities[0].name == 'Johnny Cash'
        assert self._person_repo._entities[0].phone_number == '0770192937'

        new_person = ['12', 'Bon Jovi', '0770195937']
        self._person_repo.add_person(new_person)
        assert self._person_repo._entities[1].person_id == 12
        assert self._person_repo._entities[1].name == 'Bon Jovi'
        assert self._person_repo._entities[1].phone_number == '0770195937'

        # ID already used
        try:
            new_person = ['11', 'Bon Jovi', '0770195937']
            self._person_repo.add_person(new_person)
        except PersonValidateException:
            assert True

        # ID already used
        try:
            new_person = ['asddsa', 'Bon Jovi', '0770195937']
            self._person_repo.add_person(new_person)

        except PersonValidateException:
            assert True

    def test_remove_by_id_person(self):
        new_person = ['11', 'Johnny Cash', '0770192937']
        self._person_repo.add_person(new_person)
        new_person = ['12', 'Bon Jovi', '0770195937']
        self._person_repo.add_person(new_person)
        given_id = 11
        self._person_repo.remove_by_id_person(given_id)
        assert self._person_repo._entities[0].person_id == 12

        # This person's ID doesn't exist in the list
        try:
            given_id = 5
            self._person_repo.remove_by_id_person(given_id)
        except PersonValidateException:
            assert True

    def test_update_phone_number(self):
        new_person = ['10', 'Johnny Cash', '0770192937']
        self._person_repo.add_person(new_person)
        given_id = 10
        new_phone_number = '0745132627'
        self._person_repo.update_phone_number(given_id, new_phone_number)
        assert self._person_repo._entities[0].phone_number == '0745132627'

        try:
            given_id = 5
            new_phone_number = '0745132627'
            self._person_repo.update_phone_number(given_id, new_phone_number)
        except PersonValidateException:
            assert True

    def test_replace_old_person_with_new_person_by_id(self):
        new_person = ['10', 'Johnny Cash', '0770192937']
        self._person_repo.add_person(new_person)
        old_id = 10
        new_person = ['101', 'Winston Smith', '0771256432']
        self._person_repo.replace_old_person_with_new_person_by_id(old_id, new_person)
        assert self._person_repo._entities[0].person_id == 101
        assert self._person_repo._entities[0].name == 'Winston Smith'
        assert self._person_repo._entities[0].phone_number == '0771256432'

        # The person with the ID = 10 doesn't exist anymore
        try:
            old_id = 10
            new_person = ['101', 'Winston Smith', '0771256432']
            self._person_repo.replace_old_person_with_new_person_by_id(old_id, new_person)
        except PersonValidateException:
            assert True

    def test_reversed_replace_by_id(self):
        new_person = ['10', 'Johnny Cash', '0770192937']
        self._person_repo.add_person(new_person)
        self._person_repo.reversed_replace_by_id(['12', 'June Carter', '0770192937'], 10)
        assert self._person_repo._entities[0].person_id == 12


class TestAcitvityRepository(unittest.TestCase):
    def setUp(self):
        self._activity_repo = ActivityRepo([])
        self._activity_repo.update_available_person_id_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_add_activity(self):
        new_activity = [1, [1, 3, 5], "15/05/2020", "15:05", "Rock concert"]
        self._activity_repo.add_activity(new_activity)
        assert self._activity_repo._activity_entity[0].activity_id == 1
        assert self._activity_repo._activity_entity[0].person_id == [1, 3, 5]
        assert self._activity_repo._activity_entity[0].date == [15, 5, 2020]
        assert self._activity_repo._activity_entity[0].time == [15, 5]
        assert self._activity_repo._activity_entity[0].description == "Rock concert"

        try:

            new_activity = [1, [1, 3, 5], "15/05/2020", "15:05", "Rock concert"]
            self._activity_repo.add_activity(new_activity)
        except:
            assert True

        try:

            new_activity = [1, 'asd, sad', "15/05/2020", "15:05", "Rock concert"]
            self._activity_repo.add_activity(new_activity)
        except:
            assert True

    def test_remove_activity_by_id(self):

        # We are going to delete the activity that we added previously so the activities list will be empty now
        self._activity_repo.create_default_activities()
        self._activity_repo.remove_activity_by_id(1)

        # Remove an activity that does not exists
        try:
            self._activity_repo.remove_activity_by_id(1)
        except ActivityValidateException:
            assert True


    def test_get_all(self):
        assert self._activity_repo.get_all() == []

    def test_create_activity_from_string(self):
        self._activity_repo.create_activity_from_string(['1', ['1', ' 3', ' 5'], '12/05/2020', '12:05', 'Rock concert'])

    def test_create_default_activities(self):
        self._activity_repo.create_default_activities()
        assert len(self._activity_repo.activity_entity) == 6

    def test_available_person_id_list_getter(self):
        assert self._activity_repo.available_person_id_list == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_available_person_id_list_setter(self):
        self._activity_repo.available_person_id_list = [1, 2, 3]
        assert self._activity_repo.available_person_id_list == [1, 2, 3]

    def test_activity_entity(self):
        assert self._activity_repo.activity_entity == []