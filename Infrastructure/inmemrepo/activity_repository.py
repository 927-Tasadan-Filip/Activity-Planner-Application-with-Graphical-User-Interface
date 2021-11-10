from Domain.Entities import *
import random
from Validators.Entity_validators import *
from Extra_module.IterableStructure import *


class ActivityRepo:
    """
    This class will create the repository of a 'Activity' object
    Note: '_activity_entity' will represent the activities already added to our program
          '_schedule' will represent the timetable of the already created activities
    """
    def __init__(self, available_person_id_list):
        self._activity_entity = IterableDataStruct()
        self._available_person_id_list = available_person_id_list
        self._schedule = []
        self.valid_activity = ValidateActivityAtributes()

    def get_all(self):
        return self._activity_entity[:]

    @property
    def activity_entity(self):
        """
        This method is the 'activity_entity' getter
        :return: the actual value of '_activity_entity'
        """
        return self._activity_entity

    @property
    def available_person_id_list(self):
        """
        This method is the 'person_id_list' getter
        :return: the actual value of '_available_person_id_list'
        """
        return self._available_person_id_list

    @property
    def schedule(self):
        """
        This method is the 'schedule' getter
        :return: the actual value of 'schedule'
        """
        return self._schedule

    @available_person_id_list.setter
    def available_person_id_list(self, value):
        """
        This method is the person_id_list (list) setter
        Note: this method will give to this repository the persons which were defined in the program until now
        :param value: the new value of the available_person_id_list (type: list)
        :return: updated '_available_person_id_list' with the new 'value'
        """
        self._available_person_id_list = value

    def update_available_person_id_list(self, persons_list):
        """
        This method will update the '_available_person_id_list' providing the ID's of the persons which already were
        added to our program
        :param persons_list: the persons already available in our program (this is going to be the 'RepoPersons._entity') (type: list of Person objects)
        :return:  updated '_available_person_id_list' with the new 'person_id_list'
        """
        aux_id_list = []
        for element in persons_list:
            aux_id_list.append(element)
        self._available_person_id_list = aux_id_list

    def update_schedule(self, activity_moment):
        """
        This method will update the
        :param activity_moment: the new activity time which has been added to the activities list
        :return: update the schedule of our activites list
        """
        self._schedule.append(activity_moment)

    def create_activity_from_string(self, activity_attributes_as_list):
        """
        This method will convert the activity (given as a string which represent attributes with',' after each one) into a 'Activity' object type
        :param activity_attributes_as_list:
        :param activity_attributes_as_string: activity attributes (type: string)
        :return: an 'Activity' object type with the given attributes
        """
        activity_id = activity_attributes_as_list[0]
        person_id = activity_attributes_as_list[1]
        date = activity_attributes_as_list[2]
        time = activity_attributes_as_list[3]
        description = activity_attributes_as_list[4]
        try:
            for i in range(len(person_id)):
                person_id[i] = int(person_id[i])
        except ValueError:
            raise ActivityValidateException("Person ID list should contain only INTEGER numbers!")

        self.valid_activity.validate_person_id_list(person_id, self._available_person_id_list)
        self.valid_activity.validate_activity(activity_id, person_id, date, time, description)
        return Acitvity(activity_id, person_id, date, time, description)

    def add_activity(self, new_activity):
        """
        This method will add a new activity to activities list
        :param new_activity: the activity to be added to activities list (type: activity object)
        :return: add the 'new_activity' in the '_activity_entity'
        """

        new_activity = self.create_activity_from_string(new_activity)
        for element in self._activity_entity:
            if element.activity_id == new_activity.activity_id:
                raise ActivityValidateException("The new activity ID already exists in our activities list!")

        aux_date = new_activity.date
        aux_time = new_activity.time
        new_activity.date = aux_date
        new_activity.time = aux_time
        activity_moment = [new_activity.date, new_activity.time]
        self.valid_activity.validate_period_of_activity_by_means_of_schedule(self.schedule, activity_moment)
        self._activity_entity.append_iter(new_activity)
        self.update_schedule(activity_moment)

    def remove_activity_by_id(self, given_id):
        """
        This method will remove an activity with the given id from our activities list
        :param given_id: activity's ID to be removed from activities list (type: positive integer)
        :return: remove from '_activity_entity' the person which had that given ID
        """

        aux_scedule = []
        self.valid_activity.validate_activity_id(given_id)
        given_id = int(given_id)
        ok = 0
        for index in range(self._activity_entity.get_length()):
            element = self._activity_entity.__getitem__(index)
            actual_id_of_activity = int(element.activity_id)
            if actual_id_of_activity == given_id:
                removed_activity = element
                ok = 1
                self._activity_entity.__delitem__(index)
                actual_date = element.date
                actual_time = element.time
                for elem_in_schedule in self._schedule:
                    if elem_in_schedule[0] == actual_date and elem_in_schedule[1] == actual_time:
                        continue
                    else:
                        aux_scedule.append(elem_in_schedule)
                break
        if ok == 0:
            raise ActivityValidateException("Activity can't be removed because it doesn't exist")
        self._schedule.clear()
        self._schedule.extend(aux_scedule)
        return removed_activity

    def create_default_activities(self):
        self.add_activity(['1', ['1', ' 3', ' 5'], '12/05/2020', '12:05', 'Rock concert'])
        self.add_activity(['2', ['1', ' 6', ' 7'], '10/05/2020', '19:20', 'Jazz concert'])
        self.add_activity(['3', ['1', ' 6', ' 7', ' 9'], '10/10/2020', '19:20', 'Blues concert'])
        self.add_activity(['4', ['1', ' 8', ' 5'], '12/05/2020', '10:00', 'Pop concert'])
        self.add_activity(['5', ['5', ' 6', ' 3', ' 9'], '10/10/2020', '15:20', 'Folk concert'])
        self.add_activity(['6', ['8', ' 2', ' 7', ' 9'], '5/5/2020', '5:5', 'Country concert'])



    @staticmethod
    def transform_activities_list_to_string(acitvities_list):
        activities = acitvities_list
        activity_string_list = []
        if activities == None:
            activities = []
        for element in activities:
            activity_string = str(element.activity_id) + "| " + str(element.person_id)

            if element.date[0] < 10:
                dd = '0' + str(element.date[0])
            else:
                dd = str(element.date[0])

            if element.date[1] < 10:
                mm = '0' + str(element.date[1])
            else:
                mm = str(element.date[1])

            if element.time[0] < 10:
                hour = '0' + str(element.time[0])
            else:
                hour = str(element.time[0])

            if element.time[1] < 10:
                minute = '0' + str(element.time[1])
            else:
                minute = str(element.time[1])

            activity_string += "|" + dd + '/' + mm + '/' + str(element.date[2])
            activity_string += "|" + hour + ':' + minute
            activity_string += "|" + str(element.description)
            activity_string_list.append(activity_string)

        return activity_string_list

    @staticmethod
    def transform_activities_string_to_list(activities_string):
        parts = activities_string.split("|")
        activity_id = parts[0].strip()
        persons_raw_list = parts[1].strip()
        persons_raw_list = persons_raw_list[1:][:]
        persons_raw_list = persons_raw_list[:(len(persons_raw_list) - 1)][:]
        person_list_id = persons_raw_list.split(",")
        date = parts[2]
        time = parts[3]
        description = parts[4]
        params = [activity_id, person_list_id, date, time, description]
        return params

    @staticmethod
    def transform_json_dict_to_activity_list(given_dict):
        date = str(given_dict["date"][0]) + '/' + str(given_dict["date"][1]) + '/' + str(given_dict["date"][2])
        time = str(given_dict["time"][0]) + ':' + str(given_dict["time"][1])
        return [given_dict["activity_id"], given_dict["person_id"], date, time, given_dict["description"]]

    @staticmethod
    def transform_activity_object_to_json_dict(given_activity):

        dictionary = {
            "activity_id": given_activity.activity_id,
            "person_id": given_activity.person_id,
            "date": given_activity.date,
            "time": given_activity.time,
            "description": given_activity.description
        }
        return dictionary

    @staticmethod
    def compare_by_date(activity_1, activity_2):
        if activity_1.date[2] < activity_2.date[2]:
            return True
        elif activity_1.date[2] > activity_2.date[2]:
            return False
        else:
            if activity_1.date[1] < activity_2.date[1]:
                return True
            elif activity_1.date[1] > activity_2.date[1]:
                return False

            else:
                if activity_1.date[0] <= activity_2.date[0]:
                    return True
                elif activity_1.date[0] > activity_2.date[0]:
                    return False

    @staticmethod
    def compare_date_counter(date_counter_1, date_counter_2):
        if date_counter_1[0] < date_counter_2[0]:
            return False
        else:
            return True

    @staticmethod
    def activity_date_acceptance(given_date):
        def check_acceptance_date(activity_object):
            aux_data = activity_object.date
            if aux_data != given_date:
                return True
            else:
                return False

        return check_acceptance_date

    @staticmethod
    def compare_time_counter(activity_1, activity_2):
        if activity_1.time[0] <= activity_2.time[0]:
            return True
        else:
            return False

    @staticmethod
    def activity_time_acceptance(given_time):
        def check_acceptance_date(activity_object):
            aux_time = activity_object.time
            if aux_time != given_time:
                return True
            else:
                return False

        return check_acceptance_date

    @staticmethod
    def activity_time_description(given_description):
        def check_acceptance_date(activity_object):
            aux_description = activity_object.description.lower()
            given_description.lower()

            if given_description in aux_description:
                return False
            else:
                return True

        return check_acceptance_date

    # def remove_a_person_from_all_activities(self, given_id):
    #     for i in range(self._activity_entity.get_length()):
    #         if given_id in self._activity_entity[i].person_id:
    #             self.remove_activity_by_id(self._activity_entity[i].activity_id)