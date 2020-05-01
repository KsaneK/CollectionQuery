import csv
from typing import Iterable


class Record:
    def __init__(self, a, b, c, d, e, f, g, h):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h

    def __str__(self):
        values = [f"{k}={v}" for k, v in self.__dict__.items()]
        values = ", ".join(values)
        return f"Record({values})"

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def from_csv(file_dir) -> Iterable:
        records = []
        with open(file_dir, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for record in csv_reader:
                records.append(Record(*record))
        return records


sample_data = [
    Record(1, 2, 3, 4, 5, 6, 7, 8),
    Record(8, 7, 6, 5, 4, 3, 2, 1)
]
