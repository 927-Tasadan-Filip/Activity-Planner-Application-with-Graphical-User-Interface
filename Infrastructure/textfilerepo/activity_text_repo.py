from Infrastructure.inmemrepo.activity_repository import *


class ActivityTextRepo(ActivityRepo):
    def __init__(self, persons_repo, filename):
        ActivityRepo.__init__(self, persons_repo)
        self.__filename = filename

    def read_all_from_file(self):

        file_to_read = open(self.__filename, 'r')
        for line in file_to_read:
            line = line.strip()
            if line != "":
                line.strip()
                line = ActivityRepo.transform_activities_string_to_list(line)
                try:
                    ActivityRepo.add_activity(self, line)
                except:
                    pass
        file_to_read.close()

    def __write_all_to_file(self):

        file_to_write = open(self.__filename, 'w')
        activities_as_string = ActivityRepo.transform_activities_list_to_string(self._activity_entity)
        for element in activities_as_string:
            file_to_write.write(element + "\n")
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


