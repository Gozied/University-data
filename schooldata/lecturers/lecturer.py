""" This module defines the behaviour of a university Lecturer class information """
from Abel.schooldata.data_handler import DataHandler


class Lecturer(DataHandler):

    table_name = "lecturer.csv"
    fieldnames = ['entity_id', 'full_name', 'faculty', 'no_of_courses', 'no_of_student', 'title']
    
    def add_lecturer(self, **kwargs):
        return self.add_record(**kwargs)
        
    def update_lecturer(self, entity_id,**kwargs):
        lecturer_info = self.records[entity_id]
        if "updated_courses" in kwargs:
            lecturer_info["no_of_courses"] = kwargs["updated_courses"]

        if "updated_no_student" in kwargs:
            lecturer_info['no_of_student'] = kwargs["updated_no_student"]
        return lecturer_info