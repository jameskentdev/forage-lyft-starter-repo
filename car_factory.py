from car import Car
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

import datetime


class CarFactory:
    @staticmethod
    def create_calliope(current_date: datetime.datetime,
                        last_service_date: datetime.datetime,
                        current_mileage: int,
                        last_service_mileage: int) -> Car:

        engine = CapuletEngine(
            last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        battery = SpindlerBattery(
            current_date=current_date, last_service_date=last_service_date)

        return Car(engine=engine, battery=battery)

    @staticmethod
    def create_glissade(current_date: datetime.datetime,
                        last_service_date: datetime.datetime,
                        current_mileage: int,
                        last_service_mileage: int) -> Car:

        engine = WilloughbyEngine(
            last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        battery = SpindlerBattery(
            current_date=current_date, last_service_date=last_service_date)

        return Car(engine=engine, battery=battery)

    @staticmethod
    def create_palindrome(current_date: datetime.datetime,
                          last_service_date: datetime.datetime,
                          warning_light_on: bool) -> Car:

        engine = SternmanEngine(
            warning_light_is_on=warning_light_on)
        battery = SpindlerBattery(
            current_date=current_date, last_service_date=last_service_date)

        return Car(engine=engine, battery=battery)

    @staticmethod
    def create_rorschach(current_date: datetime.datetime,
                         last_service_date: datetime.datetime,
                         current_mileage: int,
                         last_service_mileage: int) -> Car:

        engine = WilloughbyEngine(
            last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        battery = NubbinBattery(
            current_date=current_date, last_service_date=last_service_date)

        return Car(engine=engine, battery=battery)

    @staticmethod
    def create_thovex(current_date: datetime.datetime,
                      last_service_date: datetime.datetime,
                      current_mileage: int,
                      last_service_mileage: int) -> Car:

        engine = CapuletEngine(
            last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        battery = NubbinBattery(
            current_date=current_date, last_service_date=last_service_date)

        return Car(engine=engine, battery=battery)


c = CarFactory.create_calliope(
    datetime.datetime.now(), datetime.datetime.now(), 0, 0)
