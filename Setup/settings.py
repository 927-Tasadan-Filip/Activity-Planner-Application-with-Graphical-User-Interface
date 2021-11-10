from Business.Service import *
from Console.UI import *
from GUI import *
from Infrastructure.textfilerepo.activity_text_repo import *
from Infrastructure.textfilerepo.person_text_repo import *
from Infrastructure.binaryfilerepo.activity_binary_repo import *
from Infrastructure.binaryfilerepo.person_binary_repo import *
from Infrastructure.jsonfilerepo.person_json_repo import *
from Infrastructure.jsonfilerepo.activity_json_repo import *
from Infrastructure.SQL_Lite_repo.person_sql_lite_database_repo import *
from Infrastructure.SQL_Lite_repo.activities_sql_lite_database_repo import *
import sqlite3

class Settings:
    def __init__(self):
        self.repo_type = None
        self.persons_repo_filename = None
        self.activities_repo_filename = None
        self.ui = None

    def get_setting(self):
        file_settings = open("Setup/settings.properties", "r")
        lines = file_settings.readlines()
        for line in lines:
            line = line.strip(' ').split()
            if line != "":
                setting = line[0]
                value = line[2].strip('"')
                if setting.lower() == "repository":
                    self.repo_type = value
                elif setting.lower() == "persons":
                    self.persons_repo_filename = "database\\" + value
                elif setting.lower() == "activities":
                    self.activities_repo_filename = "database\\" + value
                elif setting.lower() == "ui":
                    self.ui = value
        file_settings.close()


class MainProgram:
    def __init__(self, settings_object):

        self.repo_type = settings_object.repo_type
        self.persons_repo_filename = settings_object.persons_repo_filename
        self.activities_repo_filename = settings_object.activities_repo_filename
        self.ui = settings_object.ui

        self.persons_repo = None
        self.activities_repo = None



    def configure_repositories(self):

        if self.repo_type == "inmemory":
            self.persons_repo = PersonRepo()
            self.persons_repo.generate_default_persons_list()
            self.activities_repo = ActivityRepo(self.persons_repo.get_persons_id())
            self.activities_repo.create_default_activities()

        elif self.repo_type == "textfiles":
            self.persons_repo = PersonTextRepository(self.persons_repo_filename)
            self.persons_repo.read_all_from_file()
            self.activities_repo = ActivityTextRepo(self.persons_repo.get_persons_id(), self.activities_repo_filename)
            self.activities_repo.read_all_from_file()

        elif self.repo_type == "binaryfiles":
            self.persons_repo = PersonBinaryRepository(self.persons_repo_filename)
            self.persons_repo.read_all_from_file()
            self.activities_repo = ActivityBinaryRepo(self.persons_repo.get_persons_id(), self.activities_repo_filename)
            self.activities_repo.read_all_from_file()

        elif self.repo_type == "jsonfiles":
            self.persons_repo = PersonJsonRepository(self.persons_repo_filename)
            self.persons_repo.read_all_from_file()
            self.activities_repo = ActivityJsonRepo(self.persons_repo.get_persons_id(), self.activities_repo_filename)
            self.activities_repo.read_all_from_file()

        elif self.repo_type == "sqlfiles":
            self.persons_repo = PersonSqlRepo()
            self.persons_repo.read_all_from_database()
            self.activities_repo = ActivitySqlRepo(self.persons_repo.get_persons_id())
            self.activities_repo.read_all_from_database()

    def run(self):

        self.configure_repositories()
        main_service = MainService(self.persons_repo, self.activities_repo)
        if self.ui == "":
            ui = Console(main_service)
            ui.run()
        if self.ui == "GUI":
            ui = GUI_console(main_service)
            ui.run()
