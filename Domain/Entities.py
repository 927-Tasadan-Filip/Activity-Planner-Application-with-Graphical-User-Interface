class Person:
    def __init__(self, person_id=0, name='', phone_number=''):
        """
        This is the instantiation of 'Person' object
        :param person_id: a unique positive number representing the ID of a person (type: positive integer)
        :param name: a string representing a person's name (type: string)
        :param phone_number: a number representing phone number of a person (type: string)
        """
        self.__person_id = int(person_id)
        self.__name = name
        self.__phone_number = phone_number

    @property
    def person_id(self):
        """
        This is the getter method of a person's ID
        :return: the ID of the given person (type: positive integer)
        """
        return self.__person_id

    @property
    def name(self):
        """
        This is the getter method of a person's name
        :return: the name of the given person (type: string)
        """
        return self.__name

    @property
    def phone_number(self):
        """
        This is the getter method of a person's phone number
        :return: the phone number of the given person (type: string)
        """
        return self.__phone_number

    @person_id.setter
    def person_id(self, value):
        """
        This is the setter method of a person's ID
        :param value: the new ID of the given person (type: positive integer)
        :return: set the 'person_id' to the new value
        """
        value = int(value)
        self.__person_id = value

    @name.setter
    def name(self, value):
        """
        This is the setter method of a person's name
        :param value: the new name of the given person (type: string)
        :return: set the 'name' to the new value
        """
        self.__name = value

    @phone_number.setter
    def phone_number(self, value):
        """
        This is the setter method of a person's phone number
        :param value: the new phone number of the given person (type: string of digits)
        :return: set the 'phone_number' to the new value
        """

        self.__phone_number = value

    def __eq__(self, other):
        return self.__name == other.__person_id

class Acitvity:
    def __init__(self, activity_id=0, person_id=[], date='', time='', description=''):
        """
        This method is the instantiation of 'Acitvity' object
        :param activity_id: a unique positive number representing the ID of a activity (type: positive integer)
        :param person_id: a list of  unique positive number representing the ID of a person (type: list of positive integer numbers)
        :param date: a list containing 3 numbers where: first element is the day, second element is the month and third element is the year
        :param time: a list containing 2 numbers of form: first element is the hour and the second one is the minute
        :param description: a string representing the description of the activity
        """

        self.__activity_id = activity_id
        self.__person_id = person_id
        self.__date = date
        self.__time = time
        self.__description = description

    @property
    def activity_id(self):
        """
        This method is the getter method of a activity's ID
        :return: the ID of the given activity (type: positive integer)
        """
        return int(self.__activity_id)

    @property
    def person_id(self):
        """
        This method is the getter method of a person's ID attaining to this activity
        :return: the ID of the given persons attaining to this activity (type: list of positive integer numbers)
        """
        return self.__person_id

    @property
    def date(self):
        """
        This method is the getter method of a activity's date
        :return: the date of the given activity (type: list of integers)
        """
        return self.__date

    @property
    def time(self):
        """
        This method is the getter method of a activity's time
        :return: the date of the given activity (type: list of integers)
        """
        return self.__time

    @property
    def description(self):
        """
        This method is the getter method of a activity's description
        :return: the ID of the given activity (description) (type: string)
        """
        return self.__description

    @activity_id.setter
    def activity_id(self, value):
        """
        This method is the setter method of a activity's ID
        :param value: the new ID of the given person (type: positive integer)
        :return: set the 'activity_id' to the new value (type: positive integer)
        """
        value = int(value)
        self.__activity_id = value

    @person_id.setter
    def person_id(self, value_list):
        """
        This method is the setter method of a person's ID list
        :param value: the new list of the given person's ID (type: list of positive integer)
        :return: set the 'person_id' to the new value_list
        """
        self.__person_id.clear()
        self.__person_id.extend(value_list)

    @date.setter
    def date(self, value):
        """
        This method is the setter of the activity's date
        :param value: the new value of the given activity's date (type: string made out of 3 numbers of form: 'day/month/year')
        :return: set the 'date' to the new value (type: list of integers)
        """
        dd, mm, yy = value.split('/')
        self.__date = [int(dd), int(mm), int(yy)]


    @time.setter
    def time(self, value):
        """
        This method is the setter of the activity's time
        :param value:  the new value of the given activity's time (type: a string made out of 2 numbers of form: 'hour:minute')
        :return: set the 'time' to the new value (type: list of integers)
        """
        hour, minute = value.split(':')
        self.__time = [int(hour), int(minute)]

    @description.setter
    def description(self, value):
        """
        This method is the setter of the activity's description
        :param value:  the new value of the given activity's description (type: string)
        :return: set the 'description' to the new value
        """
        self.__description = value

    def __eq__(self, other):
        return self.__activity_id == other.__activity_id

