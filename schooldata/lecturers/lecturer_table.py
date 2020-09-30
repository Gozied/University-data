""" This class implements the abstract methods of 'Base Table', 
and also inherits method from the student class. 
"""
import sys
from Abel.schooldata.lecturers.lecturer import Lecturer

class LecturerTable(Lecturer):
   
    def create(self, **kwargs):
        return self.add_lecturer(**kwargs)

    def retrieve(self, lecturer_no):
        return self.get_record(lecturer_no)

    def update(self,lecturer_no,**kwargs):
        return self.update_lecturer(lecturer_no, **kwargs)

    def delete(self, lecturer_no):
        return self.delete_record(lecturer_no)

    def write_to_csv(self):
        self._write_records_to_csv(self.fieldnames, self.table_name)

    def read_from_csv(self):
        return self._load_records_to_table(self.table_name)