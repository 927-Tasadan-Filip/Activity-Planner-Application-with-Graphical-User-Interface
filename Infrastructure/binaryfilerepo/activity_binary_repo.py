from Infrastructure.inmemrepo.activity_repository import *
import pickle


class ActivityBinaryRepo(ActivityRepo):
    def __init__(self, persons_repo, filename):
        ActivityRepo.__init__(self, persons_repo)
        self.__filename = filename

    def read_all_from_file(self):
        with open(self.__filename, "rb") as file:
            while True:
                try:
                    line = pickle.load(file)
                    activity = ActivityRepo.transform_activities_string_to_list(line)
                except EOFError:
                    activity = None
                if activity is not None:
                    ActivityRepo.add_activity(self, activity)
                else:
                    break
            file.close()

    def __write_all_to_file(self):

        file_to_write = open(self.__filename, 'wb')
        activities_as_string = ActivityRepo.transform_activities_list_to_string(self._activity_entity)
        for element in activities_as_string:
            pickle.dump(element, file_to_write)
        file_to_write.close()

    def update_available_person_id_list(self, persons_list):
        ActivityRepo.update_available_person_id_list(self, persons_list)

    def update_schedule(self, activity_moment):
        ActivityRepo.update_schedule(self, activity_moment)

    def add_activity(self, new_activity):
        ActivityRepo.add_activity(self, new_activity)
        self.__write_all_to_file()

    def remove_activity_by_id(self, given_id):
        removed_activity = ActivityRepo.remove_activity_by_id(self, given_id)
        self.__write_all_to_file()
        return removed_activity

    def get_all(self):
        return ActivityRepo.get_all(self)


    @staticmethod
    def transform_activities_list_to_string(acitvities_list):
        return ActivityRepo.transform_activities_list_to_string(acitvities_list)


