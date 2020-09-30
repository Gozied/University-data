""" This module defines the behaviour of a student class information. """
from Abel.schooldata.data_handler import DataHandler

class Student(DataHandler):
    
    _table_name = "student.csv"
    _fieldnames = ["entity_id", "gpa", "full_name"]

    def _add_student(self, **kwargs):
        return self.add_record(**kwargs)
        
         
    def _write_student_to_csv(self):
        self._write_records_to_csv(self._fieldnames, self._table_name)

    def _read_student_records_from_csv(self):
        return self._load_records_to_table(self._table_name)

    def _update_student(self,student_no, **kwargs):
        student = self.get_record(student_no)
        if "new_gpa" in kwargs:
            student["gpa"] = kwargs["new_gpa"]
        if "new_full_name" in kwargs:
            student["full_name"] = kwargs["new_full_name"]
        return student