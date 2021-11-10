from Domain.Entities import *
from Validators.Entity_validators import ValidatePerson, PersonValidateException, ActivityValidateException
from Validators.Entity_validators import ValidateActivityAtributes

import unittest


class TestPerson(unittest.TestCase):

    def setUp(self):
        self.__person = []
        self.person_validator = ValidatePerson()

    def test_person_creation(self):

        self.__person = Person()

        self.__person.person_id = 1
        self.__person.name = 'Bon Scott'
        self.__person.phone_number = '0770145234'

        assert self.__person.person_id == 1
        assert self.__person.name == 'Bon Scott'
        assert self.__person.phone_number == '0770145234'

        self.__person.person_id = 2
        self.__person.name = 'Brian Johnson'
        self.__person.phone_number = '0745233421'

        assert self.__person.person_id == 2
        assert self.__person.name == 'Brian Johnson'
        assert self.__person.phone_number == '0745233421'

    def test_validate_person(self):
        try:
            given_id = '12'
            given_phone_number = '0764232'
            self.person_validator.validate_from_list(given_id, given_phone_number)
        except PersonValidateException:
            assert True
    def test_validate_person_id(self):

        # Gibberish ID
        try:
            given_id = 'sada'
            self.person_validator.validate_person_id(given_id)
        except PersonValidateException as ve:
            assert str(ve.msg) == "Person ID should be a positive INTEGER number"

        # Negative ID
        try:
            given_id = '-12'
            self.person_validator.validate_person_id(given_id)
        except PersonValidateException as ve:
            assert str(ve.msg) == "Person ID should be a POSITIVE integer number"

    def test_validate_phone_number(self):

        # Phone number with different digit number than 10

        try:
            given_phone_number = '0764232'
            self.person_validator.validate_phone_number(given_phone_number)
        except PersonValidateException as ve:
            assert str(ve.msg) == "The phone number should contain exactly 10 digits"

        # Phone number containing not only digits

        try:
            given_phone_number = '0745sab965'
            self.person_validator.validate_phone_number(given_phone_number)
        except PersonValidateException as ve:
            assert str(ve.msg) == "Phone number should contain only digits"


class TestActivity(unittest.TestCase):

    def setUp(self):
        self.__activity = []
        self.activity_validator = ValidateActivityAtributes()

    def test_activity_creation(self):

        self.__activity = Acitvity()

        self.__activity.activity_id = 1
        self.__activity.person_id = [1, 2, 4, 5]
        self.__activity.date = '12/05/2020'
        self.__activity.time = '12:05'
        self.__activity.description = 'This is a rock concert'

        assert self.__activity.activity_id == 1
        assert self.__activity.person_id == [1, 2, 4, 5]
        assert self.__activity.date == [12, 5, 2020]
        assert self.__activity.time == [12, 5]
        assert self.__activity.description == 'This is a rock concert'

        self.__activity.activity_id = 3
        self.__activity.person_id = [1, 23, 43, 521]
        self.__activity.date = '01/09/2020'
        self.__activity.time = '15:05'
        self.__activity.description = 'This is a jazz concert'

        assert self.__activity.activity_id == 3
        assert self.__activity.person_id == [1, 23, 43, 521]
        assert self.__activity.date == [1, 9, 2020]
        assert self.__activity.time == [15, 5]
        assert self.__activity.description == 'This is a jazz concert'

    def test_validate_acitvity(self):
        self.activity_validator.validate_activity(3, [1, 23, 43, 521], '1/9/2020', '15:05', 'This is a jazz concert')

    def test_validate_activity_id(self):
        try:
            given_id = "sda"
            self.activity_validator.validate_activity_id(given_id)
        except:
            assert True

        try:
            given_id = "-12"
            self.activity_validator.validate_activity_id(given_id)
        except:
            assert True

    @staticmethod
    def test_msg():
        activ_except = ActivityValidateException('hei')
        assert activ_except.msg == 'hei'

    def test_validate_date(self):
        try:
            given_date = '12/12/as'
            self.activity_validator.validate_date(given_date)
        except:
            assert True

        try:
            given_date = '12/sds/2020'
            self.activity_validator.validate_date(given_date)
        except:
            assert True

    def test_validate_time(self):
        try:
            given_time = 'sad:12'
            self.activity_validator.validate_time(given_time)
        except:
            assert True

        try:
            given_time = '-12:12'
            self.activity_validator.validate_time(given_time)
        except:
            assert True

        try:
            given_time = '12:78'
            self.activity_validator.validate_time(given_time)
        except:
            assert True

    def test_validate_person_id_list(self):
        try:
            given_person_id = [1, 5, 7]
            persons_list = [2, 5, 7]
            self.activity_validator.validate_person_id_list(given_person_id, persons_list)
        except:
            assert True
    def test_validate_period_of_activity_by_means_of_schedule(self):
        # [1, 9, 2020]
        # [15, 5]
        self.activity_validator.validate_period_of_activity_by_means_of_schedule([[1, 9, 2020], [15, 5]], [[1, 9, 2020], [15, 5]])
