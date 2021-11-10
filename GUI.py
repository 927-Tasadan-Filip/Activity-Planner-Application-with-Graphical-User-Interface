from tkinter import *
from Business.Service import *
from Validators.Entity_validators import *


class GUI_console:
    def __init__(self, main_service):
        self.root = Tk()
        self.root.title("Activity planner")
        self.root.iconbitmap('thunder.ico')
        self.__main_service = main_service

    def table_graphic_interface(self, root, matrix, total_rows, total_columns):

        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                if i == 0:
                    self.e = Entry(root, width=20, fg='black',
                                   font=('Times New Roman', 16, 'bold'))
                else:
                    self.e = Entry(root, width=25, fg='blue',
                                   font=('Arial', 16))

                self.e.grid(row=i, column=j)
                self.e.insert(END, matrix[i][j])

    def print_persons(self, persons_list):
        top = Toplevel()
        matrix_of_persons = []
        matrix_of_persons.append(["ID", "Name", "Phone number"])
        for element in persons_list:
            matrix_of_persons.append([element.person_id, element.name, element.phone_number])

        total_rows = len(matrix_of_persons)
        total_columns = len(matrix_of_persons[0])

        self.table_graphic_interface(top, matrix_of_persons, total_rows, total_columns)

    def print_activities(self, activities_list):
        top = Toplevel()
        matrix_of_activities = []
        matrix_of_activities.append(["Activity ID", "Persons ID", "Date", "Time", "Description"])
        for element in activities_list:

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
            date = dd + '/' + mm + '/' + str(element.date[2])
            time = hour + ':' + minute
            person_id_list = ""
            for person in element.person_id:
                person_id_list += str(person) + ','
            person_id_list = person_id_list[:-1]
            matrix_of_activities.append([element.activity_id,person_id_list, date, time, element.description])

        total_rows = len(matrix_of_activities)
        total_columns = len(matrix_of_activities[0])

        self.table_graphic_interface(top, matrix_of_activities, total_rows, total_columns)

    def physical_add_person(self, params, level):
        try:
            self.__main_service.service_add_person(params, 1)
            message = "Operation done successfully!"
        except PersonValidateException as ve:
            message = "Error: " + str(ve.msg)

        status = Entry(level, width=50, font=10, fg="blue", bg="yellow")
        status.insert(0, str(message))
        status.grid(row=3, column=1)

    def clicked_add_person(self, level):
        top = Toplevel(level)
        Label(top, text="Person ID:", font=10).grid(row=0, column=0)
        entry_id = Entry(top, width=40, font=10)
        entry_id.grid(row=0, column=1)
        Label(top, text="Person name:", font=10).grid(row=1, column=0)
        entry_name = Entry(top, width=40, font=10)
        entry_name.grid(row=1, column=1)
        Label(top, text="Person phone number:", font=10).grid(row=2, column=0)
        entry_phone = Entry(top, width=40, font=10)
        entry_phone.grid(row=2, column=1)
        Button(top, text="Add new persons with the given attributes", bg='yellow', command=lambda: self.physical_add_person([entry_id.get(), entry_name.get(), entry_phone.get()], top)).grid(row=3, column=0)

    def physical_remove_person(self, id_, level):
        try:
            self.__main_service.service_remove_by_id(id_, 1)
            message = "Operation done successfully!"
        except PersonValidateException as ve:
            message = "Error: " + str(ve.msg)

        status = Entry(level, width=50, font=10, fg="blue", bg="yellow")
        status.insert(0, str(message))
        status.grid(row=1, column=1)

    def clicked_remove(self, level):
        top = Toplevel(level)
        Label(top, text="Person ID:", font=10).grid(row=0, column=0)
        entry_id = Entry(top, width=40, font=10)
        entry_id.grid(row=0, column=1)
        Button(top, text="Remove persons with the given ID", bg='yellow', command=lambda: self.physical_remove_person(entry_id.get(),top)).grid(row=1, column=0)

    def physical_update(self, params, level):
        try:
            self.__main_service.service_update_phone_number([params[0], params[1]], 1)
            message = "Operation done successfully!"
        except PersonValidateException as ve:
            message = "Error: " + str(ve.msg)

        status = Entry(level, width=50, font=10, fg="blue", bg="yellow")
        status.insert(0, str(message))
        status.grid(row=2, column=1)

    def clicked_update(self, level):
        top = Toplevel(level)
        Label(top, text="Person ID:", font=10).grid(row=0, column=0)
        entry_id = Entry(top, width=40, font=10)
        entry_id.grid(row=0, column=1)
        Label(top, text="New phone:", font=10).grid(row=1, column=0)
        entry_phone = Entry(top, width=40, font=10)
        entry_phone.grid(row=1, column=1)
        Button(top, text="Update phone number of given person", bg='yellow',command=lambda: self.physical_update([entry_id.get(), entry_phone.get()], top)).grid(row=2, column=0)

    def physical_replace_person(self, params, level):
        try:
            print(params[0])
            self.__main_service.service_replace_by_id(params, 1)
            message = "Operation done successfully!"
        except PersonValidateException as ve:
            message = "Error: " + str(ve.msg)

        status = Entry(level, width=50, font=10, fg="blue", bg="yellow")
        status.insert(0, str(message))
        status.grid(row=4, column=1)

    def replace_by_id(self, level):
        top = Toplevel(level)
        Label(top, text="Person ID to change:", font=10).grid(row=0, column=0)
        entry_old_id = Entry(top, width=40, font=10)
        entry_old_id.grid(row=0, column=1)
        Label(top, text="New person ID:", font=10).grid(row=1, column=0)
        entry_new_id = Entry(top, width=40, font=10)
        entry_new_id.grid(row=1, column=1)
        Label(top, text="New person name:", font=10).grid(row=2, column=0)
        entry_name = Entry(top, width=40, font=10)
        entry_name.grid(row=2, column=1)
        Label(top, text="New person phone number:", font=10).grid(row=3, column=0)
        entry_phone = Entry(top, width=40, font=10)
        entry_phone.grid(row=3, column=1)
        Button(top, text="Replace person", bg='yellow', font=10, command=lambda: self.physical_replace_person([entry_old_id.get(),[entry_new_id.get(), entry_name.get(), entry_phone.get()]],top)).grid(row=4, column=0)

    def open_persons_menu(self):
        top = Toplevel()
        Label(top, text="What do you want to do?", font=10).grid(row=0, column=0, columnspan=2)
        Button(top, text="Add new person", font=10, bg='purple', fg='white', command=lambda: self.clicked_add_person(top)).grid(row=1, column=0)
        Button(top, text="Remove person by ID", font=10, bg='purple', fg='white', command=lambda: self.clicked_remove(top)).grid(row=2, column=0)
        Button(top, text="Update phone number", font=10, bg='purple', fg='white', command=lambda: self.clicked_update(top)).grid(row=3, column=0)
        Button(top, text="Replace person by ID", font=10, bg='purple', fg='white', command=lambda: self.replace_by_id(top)).grid(row=4, column=0)
        Button(top, text="Display persons list", font=10, bg='purple', fg='white', command=lambda: self.list_persons()).grid(row=5, column=0)

    def physical_add_activity(self, params, level):
        try:
            persons_id_list = params[1].split(',')
            params[1] = persons_id_list
            persons = self.__main_service.service_get_persons()
            persons_list = []
            for element in persons:
                persons_list.append(element.person_id)
            parametrii = [persons_list, params]
            self.__main_service.service_add_activity(parametrii, 1)
            message = "Operation done successfully!"
        except ActivityValidateException as ve:
            message = "Error: " + str(ve.msg)

        status = Entry(level, width=50, font=10, fg="blue", bg="yellow")
        status.insert(0, str(message))
        status.grid(row=5, column=1)

    def clicked_add_activity(self, level):
        top = Toplevel(level)
        Label(top, text="Activity ID:", font=10).grid(row=0, column=0)
        entry_activity_id = Entry(top, width=40, font=10)
        entry_activity_id.grid(row=0, column=1)
        Label(top, text="Persons ID list (with ',' between every ID):", font=10).grid(row=1, column=0)
        entry_persons_id = Entry(top, width=40, font=10)
        entry_persons_id.grid(row=1, column=1)
        Label(top, text="Date of activity (format - dd/mm/yy):", font=10).grid(row=2, column=0)
        entry_date = Entry(top, width=40, font=10)
        entry_date.grid(row=2, column=1)
        Label(top, text="Time of activity (format - hour:minute):", font=10).grid(row=3, column=0)
        entry_time = Entry(top, width=40, font=10)
        entry_time.grid(row=3, column=1)
        Label(top, text="Activity description:", font=10).grid(row=4, column=0)
        entry_description = Entry(top, width=40, font=10)
        entry_description.grid(row=4, column=1)
        Button(top, text="Add new activity with the given attributes", bg='yellow', font=10,
        command=lambda: self.physical_add_activity([entry_activity_id.get(),  entry_persons_id.get(), entry_date.get(), entry_time.get(), entry_description.get()],top)).grid(row=5, column=0)

    def physical_remove_activity(self, params, level):
        try:
            self.__main_service.service_remove_activity_by_id(params, 1)
            message = "Operation done successfully!"
        except ActivityValidateException as ve:
            message = "Error: " + str(ve.msg)

        status = Entry(level, width=50, font=10, fg="blue", bg="yellow")
        status.insert(0, str(message))
        status.grid(row=1, column=1)

    def clicked_remove_activity(self, level):
        top = Toplevel(level)
        Label(top, text="Activity ID to be removed:", font=10).grid(row=0, column=0)
        entry_activity_id = Entry(top, width=40, font=10)
        entry_activity_id.grid(row=0, column=1)
        Button(top, text="Remove the activity with the given ID", bg='yellow', font=10,
               command=lambda: self.physical_remove_activity(entry_activity_id.get(), top)).grid(row=1, column=0)

    def open_activities_menu(self):
        top = Toplevel()
        Label(top, text="What do you want to do?", font=10).grid(row=0, column=0, columnspan=2)
        Button(top, text="Add new activity", font=10, bg='purple', fg='white', command=lambda: self.clicked_add_activity(top)).grid(row=1, column=0)
        Button(top, text="Remove activity by ID", font=10, bg='purple', fg='white', command=lambda: self.clicked_remove_activity(top)).grid(row=2, column=0)

    def list_persons(self):

        persons_list = self.__main_service.service_get_persons()
        self.print_persons(persons_list)

    def list_activities(self):
        activities_list = self.__main_service.service_get_activities()
        self.print_activities(activities_list)

    def clicked_search_person_name(self, person_name, level):
        try:
            person_search_list = self.__main_service.service_search_person_name(person_name)
            self.print_persons(person_search_list)
            message = "Operation done successfully!"
        except ServiceException as ve:
            message = "Error: " + str(ve.msg)

        status = Entry(level, width=40, font=10, fg="blue", bg="yellow")
        status.insert(0, str(message))
        status.grid(row=3, column=1)

    def clicked_search_person_phone(self, person_phone, level):
        try:
            person_search_list = self.__main_service.service_search_person_phone(person_phone)
            self.print_persons(person_search_list)
            message = "Operation done successfully!"
        except ServiceException as ve:
            message = "Error: " + str(ve.msg)

        status = Entry(level, width=40, font=10, fg="blue", bg="yellow")
        status.insert(0, str(message))
        status.grid(row=3, column=1)

    def search_person(self):
        top = Toplevel()
        Label(top, text="What is your search criteria?", font=10).grid(row=0, column=0, columnspan=2)
        entry_name = Entry(top, width=40, font=10)
        entry_name.grid(row=1, column=1)
        Button(top, text="Name", font=10, bg='green', command=lambda: self.clicked_search_person_name(entry_name.get(), top)).grid(row=1, column=0)

        entry_phone_number = Entry(top, width=40, font=10)
        entry_phone_number.grid(row=2, column=1)
        Button(top, text="Phone number", font=10, bg='green', command=lambda: self.clicked_search_person_phone(entry_phone_number.get(), top)).grid(row=2, column=0)

    def clicked_search_activity_date(self, date, level):
        message = ""
        try:
            dd, mm, yy = date.split("/")
            activity_date = [int(dd), int(mm), int(yy)]
        except:
            message = "Error: Invalid date!"
        if message =="":
            try:
                activity_search_list = self.__main_service.service_search_activity_date(activity_date)
                self.print_activities(activity_search_list)
                message = "Operation done successfully!"
            except ServiceException as ve:
                message = "Error: " + str(ve.msg)

        status = Entry(level, width=40, font=10, fg="blue", bg="yellow")
        status.insert(0, str(message))
        status.grid(row=4, column=1)

    def clicked_search_activity_time(self, time, level):
        message = ""
        try:
            hour, minute = time.split(":")
            activity_time = [int(hour), int(minute)]
        except:
            message = "Error: Invalid time!"
        if message == "":
            try:
                activity_search_list = self.__main_service.service_search_activity_time(activity_time)
                self.print_activities(activity_search_list)
                message = "Operation done successfully!"
            except ServiceException as ve:
                message = "Error: " + str(ve.msg)

        status = Entry(level, width=40, font=10, fg="blue", bg="yellow")
        status.insert(0, str(message))
        status.grid(row=4, column=1)

    def clicked_search_activity_description(self, description, level):
        try:
            activity_description = description.lower()
            activity_search_list = self.__main_service.service_search_activity_description(activity_description)
            self.print_activities(activity_search_list)
            message = "Operation done successfully!"
        except ServiceException as ve:
            message = "Error: " + str(ve.msg)
        status = Entry(level, width=40, font=10, fg="blue", bg="yellow")
        status.insert(0, str(message))
        status.grid(row=4, column=1)

    def search_activity(self):
        top = Toplevel()
        Label(top, text="What is your search criteria?", font=10).grid(row=0, column=0, columnspan=2)
        entry_date = Entry(top, width=40, font=10)
        entry_date.grid(row=1, column=1)
        Button(top, text="Date (form of input - dd/mm/yy)", font=10, bg='green', command=lambda: self.clicked_search_activity_date(entry_date.get(), top)).grid(row=1, column=0)

        entry_time = Entry(top, width=40, font=10)
        entry_time.grid(row=2, column=1)
        Button(top, text="Time (form of input - hour:minute)", font=10, bg='green', command=lambda: self.clicked_search_activity_time(entry_time.get(), top)).grid(row=2, column=0)

        entry_description = Entry(top, width=40, font=10)
        entry_description.grid(row=3, column=1)
        Button(top, text="Description", font=10, bg='green', command=lambda: self.clicked_search_activity_description(entry_description.get(), top)).grid(row=3, column=0)

    def clicked_search_activity_person(self, person_id, level):

        try:
            activity_search_list = self.__main_service.service_search_person_in_activity(person_id)
            self.print_activities(activity_search_list)
            message = "Operation done successfully!"
        except ServiceException as ve:
            message = "Error: " + str(ve.msg)

        status = Entry(level, width=40, font=10, fg="blue", bg="yellow")
        status.insert(0, str(message))
        status.grid(row=2, column=1)

    def search_activity_with_person(self):
        top = Toplevel()
        Label(top, text="What is your search criteria?", font=10).grid(row=0, column=0, columnspan=2)
        entry_person_id = Entry(top, width=40, font=10)
        entry_person_id.grid(row=1, column=1)
        Button(top, text="Person ID for search", font=10, bg='green', command=lambda: self.clicked_search_activity_person(entry_person_id.get(), top)).grid(row=1, column=0)

    def search_activity_in_a_date(self):
        top = Toplevel()
        entry_date = Entry(top, width=40, font=10)
        entry_date.grid(row=1, column=1)
        Button(top, text="Date (form of input - dd/mm/yy)", font=10, bg='green',command=lambda: self.clicked_search_activity_date(entry_date.get(), top)).grid(row=1, column=0)

    def busiest_days(self):
        upcoming_activities = self.__main_service.service_busiest_days()
        self.print_activities(upcoming_activities)

    def undo(self):
        try:
            self.__main_service.service_undo()
            message = "Operation done successfully!"
        except ServiceException as ve:
            message = "Error: " + str(ve.msg)

        status = Entry(self.root, width=40, font=10, fg="blue", bg="yellow")
        status.insert(0, str(message))
        status.grid(row=8, column=1)

    def redo(self):
        try:
            self.__main_service.service_redo()
            message = "Operation done successfully!"
        except ServiceException as ve:
            message = "Error: " + str(ve.msg)

        status = Entry(self.root, width=40, font=10, fg="blue", bg="yellow")
        status.insert(0, str(message))
        status.grid(row=8, column=1)

    def run(self):

        my_lbl = Label(self.root, text="Welcome to activity planner!", font=15, fg='red').grid(row=0,column=0,columnspan=3)
        Button(self.root, text="Manage persons", font=10, command=self.open_persons_menu, bg='yellow').grid(row=1, column=0)
        Button(self.root, text="Manage activities", font=10,command=self.open_activities_menu, bg='yellow').grid(row=1, column=1)
        Button(self.root, text="Display persons list", font=10,command=self.list_persons, bg='yellow').grid(row=2, column=0)
        Button(self.root, text="Display activities list", font=10,command=self.list_activities, bg='yellow').grid(row=2, column=1)
        Button(self.root, text="Search person", font=10,command=self.search_person, bg='yellow').grid(row=3, column=0)
        Button(self.root, text="Search activity", font=10,command=self.search_activity, bg='yellow').grid(row=3, column=1)
        Button(self.root, text="Search activity with a person", font=10,command=self.search_activity_with_person, bg='yellow').grid(row=4, column=0)
        Button(self.root, text="Search activity in a given date", font=10,command=self.search_activity_in_a_date, bg='yellow').grid(row=4, column=1)
        Button(self.root, text="Busiest days", font=10,command=self.busiest_days, bg='yellow').grid(row=5, column=0)
        Button(self.root, text="Undo last operation", font=10, command=self.undo, fg='white', bg='blue').grid(row=6, column=0)
        Button(self.root, text="Redo last operation", font=10, command=self.redo, fg='white', bg='blue').grid(row=6, column=1)
        self.root.mainloop()






