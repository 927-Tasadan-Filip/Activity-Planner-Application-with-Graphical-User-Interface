from Infrastructure.inmemrepo.activity_repository import *
import sqlite3
class ActivitySqlRepo(ActivityRepo):

    def __init__(self, persons_repo):
        ActivityRepo.__init__(self, persons_repo)
        self.__connection = self.create_connection("activities")
        create_persons_table = """
        CREATE TABLE IF NOT EXISTS activities (
          activity_id INTEGER,
          persons_id TEXT NOT NULL,
          date TEXT NOT NULL,
          time TEXT NOT NULL,
          description TEXT NOT NULL
        );
        """
        self.execute_query(self.__connection, create_persons_table)

    @staticmethod
    def create_connection(name):
        connection = sqlite3.connect("database/" + name + ".sqlite")
        return connection

    @staticmethod
    def execute_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()

    def read_all_from_database(self):
        cursor = self.__connection.cursor()
        cursor.execute("SELECT * FROM activities")
        activities_tuples = cursor.fetchall()
        for activity in activities_tuples:
            ActivityRepo.add_activity(self, [activity[0], activity[1].split(), activity[2], activity[3], activity[4]])

    def delete_activity_sql(self, id):
        cursor = self.__connection.cursor()
        cursor.execute('DELETE FROM activities WHERE activity_id=?', (id,))
        self.__connection.commit()

    def add_activity(self, new_activity):
        aux_new_activity = new_activity[:]
        ActivityRepo.add_activity(self, new_activity)
        cursor = self.__connection.cursor()

        aux_id_string = ""
        for pers_id in aux_new_activity[1][:]:
            string_aux = str(pers_id) + " "
            aux_id_string += string_aux

        aux_id_string = aux_id_string[:-1][:]
        cursor.execute("insert into activities (activity_id, persons_id, date, time, description) values (?, ?, ?, ?, ?)", (int(aux_new_activity[0]), aux_id_string, aux_new_activity[2], aux_new_activity[3], aux_new_activity[4]))
        self.__connection.commit()

    def remove_activity_by_id(self, given_id):
        removed_activity = ActivityRepo.remove_activity_by_id(self, given_id)
        self.delete_activity_sql(given_id)
        return removed_activity

    def get_all(self):
        return ActivityRepo.get_all(self)

    def update_available_person_id_list(self, persons_list):
        ActivityRepo.update_available_person_id_list(self, persons_list)

    def update_schedule(self, activity_moment):
        ActivityRepo.update_schedule(self, activity_moment)


