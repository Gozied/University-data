from base_table import BaseTable

class Table(BaseTable):
    """ The table class defines methods that are inherited by student_table and lectural_table"""
    
    records = {}

    def get_records(self):
        return self.records

    def delete_record(self,entity_id):
        if entity_id in self.records:
            del self.records[entity_id]
        else:
            return "Sorry, it appears that record does not exist."
        return self.records

    def get_record(self,entity_id):
        try:
            return self.records[entity_id]
        except KeyError:
            return "No record matching that entity id in the table"

    def convert_record_info_to_dict(self, **kwargs):
        return dict(**kwargs)
    
    def add_record(self, **kwargs):
        row = self.convert_record_info_to_dict(**kwargs)
        entity_id= row["entity_id"]
        self.records[int(entity_id)] = row
        return self.records
