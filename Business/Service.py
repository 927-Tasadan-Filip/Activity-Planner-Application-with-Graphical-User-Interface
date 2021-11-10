from Infrastructure.inmemrepo.activity_repository import *
from Infrastructure.inmemrepo.person_repository import *
from Validators import Entity_validators
from operator import itemgetter
from Extra_module.GnomeSort import *
from Extra_module.FilterFunction import *


class ServiceValueException(Exception):
    pass


class ServiceException(ServiceValueException):
    def __init__(self, msg):
        super().__init__(self, msg)
        self._msg = msg

    @property
    def msg(self):
        return self._msg


class MainService:

    def __init__(self, repoPersons, repoActivities):
        self.__repoPersons = repoPersons
        self.__repoActivities = repoActivities
        """
        __operations_list is going to hold the last operation made in our program on the first position and on the second it's
        going to have the parameters of last operation
        """
        self.__last_operations_list = []
        self.__reversed_last_operations_list = []
        self.__position = -1

    def service_get_persons(self):
        return self.__repoPersons.get_all()

    def service_add_person(self, new_person, ok):
        self.__repoPersons.add_person(new_person)
        if ok == 1:
            self.add_new_operation()
            self.__last_operations_list.append([self.service_add_person, new_person])
            self.__reversed_last_operations_list.append([self.service_remove_by_id, new_person[0]])

    def service_remove_by_id(self, id, ok):
        removed_person = self.__repoPersons.remove_by_id_person(id)
        if ok == 1:
            self.add_new_operation()
            self.__last_operations_list.append([self.service_remove_by_id, id])
            self.__reversed_last_operations_list.append([self.service_add_person, [str(removed_person.person_id),str(removed_person.name), str(removed_person.phone_number)]])


    def service_update_phone_number(self, params, ok):
        id = params[0]
        new_phone_number = params[1]
        changed_phone = self.__repoPersons.update_phone_number(id, new_phone_number)
        if ok == 1:
            self.add_new_operation()
            self.__last_operations_list.append([self.service_update_phone_number, [id, new_phone_number]])
            self.__reversed_last_operations_list.append([self.service_update_phone_number, [id, changed_phone]])

    def service_replace_by_id(self, params, ok):
        old_id = params[0]
        new_person = params[1]

        old_person = self.__repoPersons.replace_old_person_with_new_person_by_id(old_id, new_person)
        old_person = [str(old_person.person_id), str(old_person.name), str(old_person.phone_number)]
        if ok == 1:
            self.add_new_operation()
            self.__last_operations_list.append([self.service_replace_by_id, params])
            self.__reversed_last_operations_list.append([self.service_reversed_replace_by_id, [old_person, new_person]])

    def service_reversed_replace_by_id(self, params, ok):
        old_person = params[0]
        new_id = params[1][0]
        self.__repoPersons.reversed_replace_by_id(old_person, new_id)

    def service_search_person_name(self, person_name):
        person_list = self.service_get_persons()
        return filter_by_given_comparison(person_list, self.__repoPersons.person_name_acceptance(person_name))

    def service_search_person_phone(self, person_phone):
        person_list = self.service_get_persons()
        return filter_by_given_comparison(person_list, self.__repoPersons.person_phone_acceptance(person_phone))

    def service_add_activity(self, params, ok):
        persons_list, new_activity = params[0], params[1]
        self.__repoActivities.update_available_person_id_list(persons_list)
        self.__repoActivities.add_activity(new_activity)
        if ok == 1:
            self.add_new_operation()
            self.__last_operations_list.append([self.service_add_activity, [persons_list, new_activity]])
            self.__reversed_last_operations_list.append([self.service_remove_activity_by_id, new_activity[0]])

    def service_remove_activity_by_id(self, activity_id, ok):
        removed_activity = self.__repoActivities.remove_activity_by_id(activity_id)

        if removed_activity.date[0] < 10:
            dd = '0' + str(removed_activity.date[0])
        else:
            dd = str(removed_activity.date[0])

        if removed_activity.date[1] < 10:
            mm = '0' + str(removed_activity.date[1])
        else:
            mm = str(removed_activity.date[1])

        if removed_activity.time[0] < 10:
            hour = '0' + str(removed_activity.time[0])
        else:
            hour = str(removed_activity.time[0])

        if removed_activity.time[1] < 10:
            minute = '0' + str(removed_activity.time[1])
        else:
            minute = str(removed_activity.time[1])

        date = dd + '/' + mm + '/' + str(removed_activity.date[2])
        time = hour + ':' + minute

        id_of_persons = removed_activity.person_id
        for i in range(len(id_of_persons)):
            id_of_persons[i] = str(id_of_persons[i])


        removed_activity = [str(removed_activity.activity_id), id_of_persons, date, time, str(removed_activity.description)]
        person_list = []
        for element in self.service_get_persons():
            person_list.append(element.person_id)

        if ok == 1:
            self.add_new_operation()
            self.__last_operations_list.append([self.service_remove_activity_by_id, activity_id])
            self.__reversed_last_operations_list.append([self.service_add_activity, [person_list, removed_activity]])

    def service_get_activities(self):
        return self.__repoActivities.get_all()

    def service_search_activity_date(self, activity_date):
        activities_list = self.service_get_activities()
        aux_activities_list = filter_by_given_comparison(activities_list, self.__repoActivities.activity_date_acceptance(activity_date))
        return gnome_sort(aux_activities_list, self.__repoActivities.compare_time_counter)

    def service_search_activity_time(self, activity_time):
        activities_list = self.service_get_activities()
        return filter_by_given_comparison(activities_list, self.__repoActivities.activity_time_acceptance(activity_time))

    def service_search_activity_description(self, activity_description):

        activities_list = self.service_get_activities()
        return filter_by_given_comparison(activities_list, self.__repoActivities.activity_time_description(activity_description))

    def service_create_default_activities(self, persons_list):
        self.__repoActivities.update_available_person_id_list(persons_list)
        self.__repoActivities.create_default_activities()

    def service_search_person_in_activity(self, id_of_person):
        try:
            id_of_person = int(id_of_person)
        except:
            raise ServiceException("ID should be a positive INTEGER number")

        if id_of_person < 0:
            raise ServiceException("ID should be a POSITIVE integer number")

        activities_list = self.service_get_activities()
        aux_activities_list = []
        ok = 0
        for element in activities_list:
            if id_of_person in element.person_id:
                aux_activities_list.append(element)
                ok = 1
        if ok == 0:
            raise ServiceException("There is no activity with the given person")
        return aux_activities_list

    def service_busiest_days(self):
        activities_list = self.service_get_activities()
        date_list = []
        date_counter = []
        activities_list = gnome_sort(activities_list, self.__repoActivities.compare_by_date)
        for element in activities_list:
            date_of_elem = element.date
            if date_of_elem not in date_list:
                date_list.append(date_of_elem)
                date_counter.append(1)
            else:
                for i in range(len(date_list)):
                    if date_of_elem == date_list[i]:
                        date_counter[i] += 1

        date_to_sort = []
        for i in range(len(date_counter)):
            date_to_sort.append([date_counter[i], date_list[i]])

        date_sorted = gnome_sort(date_to_sort, self.__repoActivities.compare_date_counter)

        aux_list = []

        for aux_date in date_sorted:
            for element in activities_list:
                if element.date == aux_date[1]:
                    aux_list.append(element)

        return aux_list

    def transform_list_of_activities_to_string(self, given_list):
        return self.__repoActivities.transform_activities_list_to_string(given_list)

    def service_undo(self):
        if self.__position >= 0:
            self.__reversed_last_operations_list[self.__position][0](self.__reversed_last_operations_list[self.__position][1], 0)
            self.__position = self.__position - 1
        else:
            raise ServiceException("No more undos available")

    def service_redo(self):
        if self.__position < len(self.__last_operations_list) - 1:
            self.__position = self.__position + 1
            self.__last_operations_list[self.__position][0]( self.__last_operations_list[self.__position][1], 0)

        else:
            raise ServiceException("No more redos available")

    def add_new_operation(self):

        self.__position += 1
        self.__last_operations_list = self.__last_operations_list[:self.__position]
        self.__reversed_last_operations_list = self.__reversed_last_operations_list[:self.__position]

    # def service_remove_a_person_from_all_activities(self, given_id):
    #     self.__repoActivities.remove_a_person_from_all_activities(given_id)

    # def service_replace_a_person_from_all_activities(self, given_id, new_id):
    #     given_id = int(given_id)
    #     self.__repoActivities.replace_a_person_from_all_activities(given_id, new_id)
