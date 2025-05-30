from dataclasses import dataclass
from datetime import datetime
import pickle
from typing import List


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    if not groups:
        return 0
    return max(len(group.students) for group in groups)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information(file_name: str = "groups.pickle") -> List[str]:
    with open(file_name, "rb") as file:
        groups = pickle.load(file)
    specialty_names = {group.specialty.name for group in groups}
    return list(specialty_names)


def read_students_information(
    file_name: str = "students.pickle"
) -> List[Student]:
    with open(file_name, "rb") as file:
        students = pickle.load(file)
    return students
