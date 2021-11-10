from Infrastructure.inmemrepo.person_repository import *
import sqlite3


class PersonSqlRepo(PersonRepo):
    def __init__(self):
        PersonRepo.__init__(self)
        self.__connection = self.create_connection("persons")
        create_persons_table = """
        CREATE TABLE IF NOT EXISTS persons (
          id INTEGER,
          name TEXT NOT NULL,
          phone TEXT NOT NULL
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
        cursor.execute("SELECT * FROM persons")
        persons_tuples = cursor.fetchall()
        for person in persons_tuples:
            PersonRepo.add_person(self, [person[0], person[1], person[2]])

    def add_new_person_to_sql(self, person):
        cursor = self.__connection.cursor()
        cursor.execute("insert into persons (id, name, phone) values (?, ?, ?)", (person[0], person[1], person[2]))
        self.__connection.commit()

    def delete_person_by_id_sql(self, id):
        cursor = self.__connection.cursor()

        cursor.execute('DELETE FROM persons WHERE id=?', (id,))
        self.__connection.commit()

    def update_person_phone_sql(self, id, new_phone_number):
        cursor = self.__connection.cursor()
        cursor.execute('Update persons SET phone = ? WHERE id = ?', (new_phone_number, id))
        self.__connection.commit()

    # def replace_person_sql(self, old_id, new_person):
    #     cursor = self.__connection.cursor()
    #     cursor.execute('Update persons SET id = ?, name = ?, phone = ? WHERE id = ?', (int(new_person[0]), new_person[1], new_person[2], int(old_id)))
    #     self.__connection.commit()

    def add_person(self, person):
        PersonRepo.add_person(self, person)
        self.add_new_person_to_sql(person)

    def remove_by_id_person(self, person_id):
        removed_person = PersonRepo.remove_by_id_person(self, person_id)
        self.delete_person_by_id_sql(person_id)
        return removed_person

    def update_phone_number(self, given_id, new_phone_number):
        changed_phone = PersonRepo.update_phone_number(self, given_id, new_phone_number)
        self.update_person_phone_sql(given_id, new_phone_number)
        return changed_phone

    def replace_old_person_with_new_person_by_id(self, old_id, new_person):
        old_person = PersonRepo.replace_old_person_with_new_person_by_id(self, int(old_id), new_person)
        return old_person

    def get_all(self):
        return PersonRepo.get_all(self)

