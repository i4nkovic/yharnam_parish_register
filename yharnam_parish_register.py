from dataclasses import dataclass, replace
# pip install Faker
from faker import Faker
import random
# pip install dataclass-csv2
from dataclass_csv import DataclassReader
from dataclass_csv import DataclassWriter
import copy

@dataclass (frozen=False)

class person:
    name: str
    surname: str
    age: int
    height: float
    street_name: str
    street_num: int
    street_postcode: int

fake = Faker()

citizen = person(
    name = fake.first_name(),
    surname = fake.last_name(), 
    age = random.randint(1,100),
    height = round(random.uniform(0.60,2.2), 2),
    street_name = fake.street_name(),
    street_num = fake.building_number(),
    street_postcode = fake.postcode()
)

matrika = []
matrika_max = 20

for i in range(matrika_max):
    matrika.append(copy.deepcopy(citizen))

for y in range(len(matrika)):
    matrika[y].name = fake.first_name()
    matrika[y].surname = fake.last_name()
    matrika[y].age = random.randint(1,100)
    matrika[y].height = round(random.uniform(0.60,2.2), 2)
    matrika[y].street_name = fake.street_name()
    matrika[y].street_num = fake.building_number()
    matrika[y].street_postcode = fake.postcode()


with open("obyvatelstvo.txt", "w", encoding="utf-8") as users_csv:
    w = DataclassWriter(users_csv, matrika, person)
    w.write()


