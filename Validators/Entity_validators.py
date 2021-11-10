
import datetime


class StoreException(Exception):
    pass


class PersonValidateException(StoreException):
    def __init__(self, msg):
        super().__init__(self, msg)
        self._msg = msg

    @property
    def msg(self):
        return self._msg


class ActivityValidateException(StoreException):
    def __init__(self, msg):
        super().__init__(self, msg)
        self._msg = msg

    @property
    def msg(self):
        return self._msg

class ValidatePerson:
    def __init__(self):
        pass

    def validate_from_list(self, person_id, phone_number):
        self.validate_person_id(person_id)
        self.validate_phone_number(phone_number)

    def validate_person_id(self, value):
        try:
            value = int(value)
        except:
            raise PersonValidateException("Person ID should be a positive INTEGER number")

        if value <= 0:
            raise PersonValidateException("Person ID should be a POSITIVE integer number")


    @staticmethod
    def validate_phone_number(value):
        if len(value) != 10:
            raise PersonValidateException("The phone number should contain exactly 10 digits")

        for digit in value:
            try:
                is_digit = int(digit)
            except:
                raise PersonValidateException("Phone number should contain only digits")


class ValidateActivityAtributes:

    def __init__(self):
        pass

    def validate_activity(self, activity_id, person_id, date, time, description):

        self.validate_activity_id(activity_id)
        self. validate_date(date)
        self.validate_time(time)

    @staticmethod
    def validate_activity_id(value):

        try:
            value = int(value)
        except:
            raise ActivityValidateException("Activity ID should be a positive INTEGER number")

        if value <= 0:
            raise ActivityValidateException("Activity ID should be a POSITIVE integer number")

    @staticmethod
    def validate_date(value):

        try:
            dd, mm, yy = value.split('/')
            dd = int(dd)
            mm = int(mm)
            yy = int(yy)
            data_check = datetime.datetime(yy, mm, dd)
        except:
            raise ActivityValidateException("The given activity's date is not valid")

    @staticmethod
    def validate_time(value):
        try:
            hour, minute = value.split(':')
            hour = int(hour)
            minute = int(minute)
        except:
            raise ActivityValidateException("The activity's given time is not valid")

        if hour < 0 or hour > 23:
            raise ActivityValidateException("The given  hour of the given activity's time is not valid")

        if minute < 0 or minute > 59:
            raise ActivityValidateException("The given minute of the given activity's time is not valid")

    @staticmethod
    def validate_person_id_list(given_person_id, persons_list):
        for element in given_person_id:
            if element not in persons_list:
                raise ActivityValidateException("The person with the ID " + str(element) + " does not exists in our persons list")

    @staticmethod
    def validate_period_of_activity_by_means_of_schedule(schedule, activity_moment):

        date_of_activity = activity_moment[0]
        time_of_activity = activity_moment[1]
        for element in schedule:
            if date_of_activity == element[0]:
                if element[1][0] == time_of_activity[0] or element[1][0] == (time_of_activity[0] - 1) or element[1][0] == (time_of_activity[0] + 1):
                    raise ActivityValidateException("There is already an activity scheduled at the given hour")

