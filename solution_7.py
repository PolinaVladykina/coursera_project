import csv
from pathlib import Path
import os
from fastnumbers import isfloat
import enum

class CarTypes(enum.Enum):
    CAR = 'car'
    TRUCK = 'truck'
    SPECMACHINE = 'spec_machine'


car_types = {'Car': 'car','Truck': 'truck','SpecMachine': 'spec_machine'}
approved_file_type = ('.jpg', '.jpeg', '.png', '.gif')

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.car_type = None
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]

class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        CarBase.__init__(self, brand, photo_file_name, carrying)
        self.car_type = car_types['Car']
        self.passenger_seats_count = int(passenger_seats_count)

class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        CarBase.__init__(self, brand, photo_file_name, carrying)
        self.car_type = car_types['Truck']
        if body_whl.count('x') != 2:
            body_whl = '0x0x0'
        body_whl = list(map(float,(body_whl.split("x"))))
        self.body_length = body_whl[0]
        self.body_width = body_whl[1]
        self.body_height = body_whl[2]
    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height

class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        CarBase.__init__(self, brand, photo_file_name, carrying)
        self.car_type = car_types['SpecMachine']
        self.extra = extra

def get_car(row):
    if len(row) == 7:
        car_type, brand, passenger_sc, photo_file_name, body_whl, carrying, extra = row
        if car_type in car_types.values() and \
                (brand and photo_file_name and isfloat(carrying)) \
            and CarBase(brand, photo_file_name,carrying).get_photo_file_ext() in approved_file_type:

            if car_type == CarTypes.CAR.value:
                try:
                    passenger_sc = int(passenger_sc)
                except ValueError:
                    return None
                return Car(brand, photo_file_name, carrying, passenger_sc)

            if car_type == car_types['Truck']:
                return Truck(brand, photo_file_name, carrying, body_whl)

            if car_type == car_types['SpecMachine']:
                if not extra:
                    return None
                return SpecMachine(brand, photo_file_name, carrying, extra)


def get_car_list(csv_filename: str):
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        car_list = []
        for row in reader:
            car = get_car(row)
            if car:
                car_list.append(car)
        return car_list


# csv_filename = Path("C:/Users/flora/PycharmProjects/pythonProject/coursera_week3_cars.csv")
# cars = get_car_list(csv_filename)
# print(len(cars))
# for car in cars:
#     print(type(car))
# print(cars[0].passenger_seats_count)
# print(cars[1].get_body_volume())

