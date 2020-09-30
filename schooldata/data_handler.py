import os, sys
import csv

from Abel.schooldata.table import Table


class DataHandler(Table):
    
    def _write_records_to_csv(self, fieldnames, table_name):
        """ this method writes to a csv file"""
        path = self.get_file_path(table_name)
        with open(path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for key in self.records.values():
                writer.writerow(key)
        print(f"Wrote {len(self.records)} records to file." )

    def _load_records_to_table(self, table_name):
        """ Loads data from csv to a dictionary"""
        path = self.get_file_path(table_name)
        with open(path, mode="r") as csv_file:
            reader = csv.DictReader(csv_file, delimiter=",")
            for row in reader:
                self.add_record(**row)
        return self.records
    
    
    def read_from_csv(self):
        raise NotImplementedError

    def write_to_csv(self):
        raise NotImplementedError

    def get_file_path(self, filename):
        """ this method join one or more path components intelligently"""
        return os.path.join(sys.path[0], filename)

