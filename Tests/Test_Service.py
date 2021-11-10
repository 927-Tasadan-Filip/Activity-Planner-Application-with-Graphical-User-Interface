from Business.Service import MainService, ServiceException, ServiceValueException
from Validators.Entity_validators import ValidatePerson, PersonValidateException, ActivityValidateException, ValidateActivityAtributes
from Infrastructure.inmemrepo import *
import unittest

class ServiceTesting(unittest.TestCase):

    def setUp(self):
        repo_persons = PersonRepo()
        repo_persons.generate_default_persons_list()
        repo_activities = ActivityRepo([])
        repo_activities.update_available_person_id_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        repo_activities.create_default_activities()
        self._test_service = MainService(repo_persons, repo_activities)

    def test_get_persons(self):
        persons_List = self._test_service.service_get_persons()
        assert len(persons_List) == 10

    def test_service_add_person(self):
        self._test_service.service_add_person(['121', 'sdadas', '1234567890'], 1)
        persons_List = self._test_service.service_get_persons()
        assert len(persons_List) == 11

    def test_service_remove_by_id(self):
        self._test_service.service_remove_by_id('10', 1)
        persons_List = self._test_service.service_get_persons()
        assert len(persons_List) == 9

    def test_service_update_phone_number(self):
        id = '1'
        new_phone_number = '0987654321'
        self._test_service.service_update_phone_number([id, new_phone_number], 1)
        persons_List = self._test_service.service_get_persons()
        assert persons_List[0].person_id == 1
        assert persons_List[0].phone_number == '0987654321'

    def test_service_replace_by_id(self):
        old_id = '1'
        new_person = ['101', 'Winston Smith', '0987654321']
        self._test_service.service_replace_by_id([old_id, new_person], 1)
        persons_List = self._test_service.service_get_persons()
        assert persons_List[9].person_id == 101
        assert persons_List[9].name == 'Winston Smith'
        assert persons_List[9].phone_number == '0987654321'

    def test_service_reversed_replace_by_id(self):

        try:
            old_person = ['101', 'Winston Smith', '0987654321']
            new_id = 10
            self._test_service.service_reversed_replace_by_id(old_person, new_id)
        except PersonValidateException:
            assert True

    def test_service_search_person_name(self):
        person_name = 'B'
        person_search_result = self._test_service.service_search_person_name(person_name)
        assert len(person_search_result) >= 1

        try:
            person_name = '213'
            person_search_result = self._test_service.service_search_person_name(person_name)
        except ServiceException:
            assert True

    def test_service_search_person_phone(self):
        person_phone = '07'
        person_search_result = self._test_service.service_search_person_phone(person_phone)
        assert len(person_search_result) >= 1

        try:
            person_phone = 'asdadsd'
            person_search_result = self._test_service.service_search_person_phone(person_phone)
        except ServiceException:
            assert True

    def test_service_add_activity(self):

        persons_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        new_activity = ['12', ['1', ' 3', ' 5'], '12/05/2022', '12:05', 'Folsom Prison Blues']
        self._test_service.service_add_activity([persons_list, new_activity], 1)
        activities_list = self._test_service.service_get_activities()
        assert activities_list[-1].activity_id == 12
        assert activities_list[-1].time == [12, 5]

    def test_service_remove_activity_by_id(self):
        activity_id = '1'
        self._test_service.service_remove_activity_by_id(activity_id, 1)
        activities_list = self._test_service.service_get_activities()
        assert activities_list[0].activity_id == 2

        activity_id = '6'
        self._test_service.service_remove_activity_by_id(activity_id, 1)
        activities_list = self._test_service.service_get_activities()
        assert activities_list[-1].activity_id == 5

        activity_id = '3'
        self._test_service.service_remove_activity_by_id(activity_id, 1)
        activities_list = self._test_service.service_get_activities()
        assert activities_list[2].activity_id == 5

    def test_service_search_activity_date(self):
        activity_date = [12, 5, 2020]
        activity_search = self._test_service.service_search_activity_date(activity_date)
        assert activity_search[0].activity_id == 4

        try:
            activity_date = [12, 5, 2025]
            activity_search = self._test_service.service_search_activity_date(activity_date)
        except ServiceException:
            assert True

    def test_service_search_activity_time(self):
        activity_time = [12, 5]
        activity_search = self._test_service.service_search_activity_time(activity_time)
        assert activity_search[0].activity_id == 1

        try:
            activity_time = [24, 0]
            activity_search = self._test_service.service_search_activity_time(activity_time)
        except ServiceException:
            assert True

    def test_service_search_activity_description(self):
        activity_description = 'blues'
        activity_search = self._test_service.service_search_activity_description(activity_description)
        assert activity_search[0].activity_id == 3

        try:
            activity_description = 'Gothic Concert'
            activity_search = self._test_service.service_search_activity_description(activity_description)
        except ServiceException:
            assert True

    def test_service_create_default_activities(self):
        try:
            self._test_service.service_create_default_activities([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        except:
            assert True

    def test_service_search_person_in_activity(self):
        id_of_person = '1'
        activity_search = self._test_service.service_search_person_in_activity(id_of_person)
        assert activity_search[0].activity_id == 1

        try:
            id_of_person = '12'
            activity_search = self._test_service.service_search_person_in_activity(id_of_person)
        except ServiceException:
            assert True

        try:
            id_of_person = 'dsa'
            activity_search = self._test_service.service_search_person_in_activity(id_of_person)
        except ServiceException:
            assert True

        try:
            id_of_person = '-5'
            activity_search = self._test_service.service_search_person_in_activity(id_of_person)
        except ServiceException:
            assert True

    def test_service_busiest_days(self):
        activity_search = self._test_service.service_busiest_days()
        assert activity_search[0].activity_id == 1

    def test_serivce_undo(self):
        try:
            self._test_service.service_undo()
        except ServiceException:
            assert True

    def test_service_redo(self):
        try:
            self._test_service.service_redo()
        except ServiceException:
            assert True
