from Business.Service import *
from Validators.Entity_validators import *


class Console:
    def ui_add_person(self):

        ID = input("ID:")
        name = input("Name:")
        phone_number = input("Phone number:").strip()
        params = [ID , name ,phone_number]
        self.__main_service.service_add_person(params, 1)

    def ui_remove_person_by_id(self):

        id_ = input("ID for remove:")
        self.__main_service.service_remove_by_id(id_, 1)
        #self.__main_service.service_remove_a_person_from_all_activities(id_)

    def ui_update_phone_number(self):

        id = input("ID for update:")
        new_phone_number = input("New phone number:")
        self.__main_service.service_update_phone_number([id, new_phone_number], 1)

    def ui_replace_by_id(self):
        id_ =  input("ID for replace:")
        ID = input("ID:")
        name = input("Name:")
        phone_number = input("Phone number:").strip()
        new_person = [ID, name, phone_number]
        params = [id_, new_person]
        self.__main_service.service_replace_by_id(params, 1)
        #self.__main_service.service_replace_a_person_from_all_activities(id_, ID)

    def ui_print_persons(self):
        persons = self.__main_service.service_get_persons()
        for element in persons:
            print('ID:', element.person_id, '| Name:', element.name, '| Phone number:', element.phone_number)

    @staticmethod
    def print_persons_modify_menu():
        print("Modify Persons Menu")
        print()
        print('Important notes')
        print('There are already 10 persons (thier ID are between 1 and 10) in the program\'s database')
        print('Each person should have an unique ID')
        print()
        print("Here is the list of commands that modify activities list which you can use:")
        print("main menu - go back to main menu")
        print("help - display the Modify Persons Menu")
        print("add - add a new person to persons list")
        print("remove - remove the person with the given ID from persons list")
        print("update - update the phone number of the person with the given ID")
        print("replace - replace the person with the old id with a new one")
        print("list - display the actual list of persons")

    def person_commands_ui(self):
        self.print_persons_modify_menu()
        done = False
        while not done:
            cmd = input(">>>")
            if cmd == 'help':
                self.print_persons_modify_menu()
            elif cmd == 'main menu':
                done = True
            elif cmd == 'list':
                self.ui_print_persons()
            else:
                cmd_name = cmd
                cmd_name = cmd_name.strip()
                if cmd_name in self.__commands_modify_persons:
                    try:
                        self.__commands_modify_persons[cmd_name]()
                    except PersonValidateException as ve:
                        print(str(ve.msg))
                else:
                    print("invalid command!")

    def ui_add_activity(self):
        Activity_id = input("Activity ID:")
        Person_list_id = input("Person ID as a list:")
        date = input("Date (form 'dd/mm/yy' as integer numbers):")
        time = input("Hour (form 'hour:minute' as integer numbers):")
        Person_list_id = Person_list_id.split(',')
        description = input("Description:")
        params = [Activity_id, Person_list_id, date, time, description]
        persons = self.__main_service.service_get_persons()

        persons_list =[]
        for element in persons:
            persons_list.append(element.person_id)

        parameters = [persons_list, params]
        self.__main_service.service_add_activity(parameters, 1)

    def ui_remove_activity_by_id(self):
        Activity_id = input("Activity ID:")
        self.__main_service.service_remove_activity_by_id(Activity_id, 1)

    def print_activity(self, given_activity_list):
        activities = given_activity_list

        for element in activities:
            activity_string = "Activity ID: " + str(element.activity_id) + "| Persons ID: " + str(element.person_id)

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

            activity_string += "| Date: " + dd + '/' + mm + '/' + str(element.date[2])
            activity_string += "| Time: " + hour + ':' + minute
            activity_string += "| Description: " + str(element.description)
            print(activity_string)

    def ui_print_activities(self):
        activities = self.__main_service.service_get_activities()
        self.print_activity(activities)


    @staticmethod
    def print_activites_modify_menu():
        print("Modify Activities Menu")
        print()
        print('!!!Important notes!!!')
        print('Each activity should have an unique ID')
        print("Each activity last one hour and you can't add a new activity if there is one already scheduled at the distance of two hours")
        print()
        print("Here is the list of commands that modify activities list which you can use:")
        print()
        print("main menu - go back to main menu")
        print("help - display the Modify Activities Menu")
        print("add  - add a new activity to activites list")
        print("remove  - remove the activity with the given ID from activities list")
        print("list - display the actual list of activities")

    def activity_commands_ui(self):
        self.print_activites_modify_menu()
        done = False
        while not done:
            cmd = input(">>>")
            if cmd == 'help':
                self.print_activites_modify_menu()
            elif cmd == 'main menu':
                done = True
            elif cmd == 'list':
                self.ui_print_activities()
            else:
                cmd_name = cmd
                cmd_name = cmd_name.strip()
                if cmd_name in self.__commands_modify_persons:
                    try:
                        self.__commands_modify_acitivty[cmd_name]()
                    except ActivityValidateException as ve:
                        print(str(ve.msg))
                else:
                    print("invalid command!")

    def ui_search_person(self):
        person_list = self.__main_service.service_get_persons()
        print("What is your search criteria?")
        cmd = input("[name / phone number] >> ")
        person_search_list = []
        if cmd == 'name':
            person_name = input("Enter the name you are searching for >> ")
            person_search_list = self.__main_service.service_search_person_name(person_name)


        elif cmd == 'phone number':
            person_phone = input("Enter the phone number you are searching for >> ")

            person_search_list = self.__main_service.service_search_person_phone(person_phone)
        else:
            raise ServiceException("You can search for persons only by name or phone number")

        for element in person_search_list:
            print('ID:', element.person_id, '| Name:', element.name, '| Phone number:', element.phone_number)

    def ui_search_activity(self):
        activity_list = self.__main_service.service_get_activities()
        print("What is your search criteria?")
        cmd = input("[date / time / description] >> ")
        activity_search_list = []

        if cmd == 'date':
            print("Enter the activity date you are searching for ")

            try:
                dd = input("activity day ( form: positive integer) >>")
                mm = input("activity month ( form: positive integer) >>")
                yy = input("activity year ( form: positive integer) >>")
                activity_date = [int(dd), int(mm), int(yy)]
            except:
                raise ServiceException("Invalid date")
            activity_search_list = self.__main_service.service_search_activity_date(activity_date)

        elif cmd == 'time':
            print("Enter the time you are searching for")

            try:
                hour = input("activity hour ( form: positive integer) >>")
                minute = input("activity minute ( form: positive integer) >>")
                activity_time = [int(hour), int(minute)]
            except:
                raise ServiceException("Invalid time")
            activity_search_list = self.__main_service.service_search_activity_time(activity_time)

        elif cmd == 'description':
            activity_description = input("Enter the description you are searching for >> ")
            activity_description = activity_description.lower()
            activity_search_list = self.__main_service.service_search_activity_description(activity_description)

        else:
            raise ServiceException("You can search for activities only by date, time or description")

        self.print_activity(activity_search_list)

    def ui_search_person_in_activity(self):
        person_id = input("Enter the ID of a person (ID should be a positive integer number) >> ")
        activity_search_list = self.__main_service.service_search_person_in_activity(person_id)
        self.print_activity(activity_search_list)

    def ui_search_activity_date(self):
        try:
            dd = input("activity day ( form: positive integer) >>")
            mm = input("activity month ( form: positive integer) >>")
            yy = input("activity year ( form: positive integer) >>")
            activity_date = [int(dd), int(mm), int(yy)]
        except:
            raise ServiceException("Invalid date")
        activity_search_list = self.__main_service.service_search_activity_date(activity_date)
        self.print_activity(activity_search_list)

    def ui_busiest_days(self):
        upcoming_activities = self.__main_service.service_busiest_days()
        self.print_activity(upcoming_activities)

    def ui_undo(self):
        self.__main_service.service_undo()

    def ui_redo(self):
        self.__main_service.service_redo()

    @staticmethod
    def print_menu():
        print()
        print("Here is the list of commands which you can use:")
        print()
        print("1. General commands")
        print("help - get the main menu")
        print("exit - stop the program execution and exit from it")
        print()
        print("2. Manage persons and activities")
        print("manage persons - go to menu which contains commands which manage persons list")
        print("manage activities - go to menu which contains commands which manage activities list")
        print("list persons - display the actual list of persons")
        print("list activities - display the actual list of activities")
        print()
        print("3. Search for persons or activities")
        print("search person - search for persons which have a given name or a phone number")
        print("search activity - search for activities which have a given date, time or description.")
        print()
        print("4. Statistics")
        print("search activity in a date - list the activities for a given date, in the order of their start time")
        print("busiest days - provides the list of upcoming dates with activities")
        print("search activity with person - search for activities with a given person")
        print()
        print("5. Undo/redo")
        print("undo")
        print("redo")
        print()

    def __init__(self, main_service):

        self.__main_service = main_service
        self.__commands_modify_persons = {
            'add': self.ui_add_person,
            'remove': self.ui_remove_person_by_id,
            'update': self.ui_update_phone_number,
            'replace': self.ui_replace_by_id,
        }
        self.__commands_modify_acitivty = {
            'add': self.ui_add_activity,
            'remove': self.ui_remove_activity_by_id,
        }
        self.__comands_category = {
            'manage persons': self.person_commands_ui,
            'manage activities': self.activity_commands_ui,
            'list persons': self.ui_print_persons,
            'list activities': self.ui_print_activities,
            'search person': self.ui_search_person,
            'search activity': self.ui_search_activity,
            'search activity with person': self.ui_search_person_in_activity,
            'search activity in a date': self.ui_search_activity_date,
            'busiest days': self.ui_busiest_days,
            'undo': self.ui_undo,
            'redo': self.ui_redo
        }

    def run(self):
        print("Welcome to Activity Planner")
        print()
        self.print_menu()
        done = False
        while not done:
            cmd = input(">>>")
            if cmd == 'help':
                self.print_menu()
            elif cmd == "exit":
                done = True
            else:
                cmd = cmd.strip()
                if cmd in self.__comands_category:
                    try:
                        self.__comands_category[cmd]()
                    except ServiceException as ve:
                        print(str(ve.msg))
                else:
                    print("invalid command!")
