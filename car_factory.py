from car import Car
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

import datetime


class CarFactory:
    @staticmethod
    def create_calliope(self,
                        current_date: datetime.datetime,
                        last_service_date: datetime.datetime,
                        current_mileage: int,
                        last_service_mileage: int) -> Car:

        engine = CapuletEngine(
            last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        battery = SpindlerBattery(
            current_date=current_date, last_service_date=last_service_date)

        return Car(engine=engine, battery=battery)

    @staticmethod
    def create_glissade(self,
                        current_date: datetime.datetime,
                        last_service_date: datetime.datetime,
                        current_mileage: int,
                        last_service_mileage: int) -> Car:

        engine = WilloughbyEngine(
            last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        battery = SpindlerBattery(
            current_date=current_date, last_service_date=last_service_date)

        return Car(engine=engine, battery=battery)

    @staticmethod
    def create_palindrome(self,
                          current_date: datetime.datetime,
                          last_service_date: datetime.datetime,
                          warning_light_on: bool) -> Car:

        engine = SternmanEngine(
            warning_light_is_on=warning_light_on)
        battery = SpindlerBattery(
            current_date=current_date, last_service_date=last_service_date)

        return Car(engine=engine, battery=battery)

    @staticmethod
    def create_rorschach(self,
                         current_date: datetime.datetime,
                         last_service_date: datetime.datetime,
                         current_mileage: int,
                         last_service_mileage: int) -> Car:

        engine = WilloughbyEngine(
            last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        battery = NubbinBattery(
            current_date=current_date, last_service_date=last_service_date)

        return Car(engine=engine, battery=battery)

    @staticmethod
    def create_thovex(self,
                      current_date: datetime.datetime,
                      last_service_date: datetime.datetime,
                      current_mileage: int,
                      last_service_mileage: int) -> Car:

        engine = CapuletEngine(
            last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        battery = NubbinBattery(
            current_date=current_date, last_service_date=last_service_date)

        return Car(engine=engine, battery=battery)
