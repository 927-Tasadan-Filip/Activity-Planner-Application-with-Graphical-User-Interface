from Infrastructure.inmemrepo.activity_repository import *
import json


class ActivityJsonRepo(ActivityRepo):
    def __init__(self, persons_repo, filename):
        ActivityRepo.__init__(self, persons_repo)
        self.__filename = filename

    def read_all_from_file(self):

        with open(self.__filename, "r") as file:
            try:
                data = json.load(file)
                for activity in data["activities"]:
                    activity = ActivityRepo.transform_json_dict_to_activity_list(activity)
                    ActivityRepo.add_activity(self, activity)
            except json.decoder.JSONDecodeError:
                pass

    def __write_all_to_file(self):

        data = {"activities": []}
        activity_as_object_list = ActivityRepo.get_all(self)
        for element in activity_as_object_list:
            activities_as_dict = ActivityRepo.transform_activity_object_to_json_dict(element)
            data["activities"].append(activities_as_dict)
        with open(self.__filename, "w") as file:
            json.dump(data, file)
            file.close()

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


