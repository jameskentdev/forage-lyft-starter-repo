from car import Car
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

import datetime
from typing import List


class CarFactory:
    @staticmethod
    def create_calliope(current_date: datetime.datetime,
                        last_service_date: datetime.datetime,
                        current_mileage: int,
                        last_service_mileage: int,
                        tires: List[float]) -> Car:

        engine = CapuletEngine(
            last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        battery = SpindlerBattery(
            current_date=current_date, last_service_date=last_service_date)
        _tires = CarriganTire(tires=tires)

        return Car(engine=engine, battery=battery, tires=_tires)

    @staticmethod
    def create_glissade(current_date: datetime.datetime,
                        last_service_date: datetime.datetime,
                        current_mileage: int,
                        last_service_mileage: int,
                        tires: List[float]) -> Car:

        engine = WilloughbyEngine(
            last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        battery = SpindlerBattery(
            current_date=current_date, last_service_date=last_service_date)
        _tires = CarriganTire(tires=tires)

        return Car(engine=engine, battery=battery, tires=_tires)

    @staticmethod
    def create_palindrome(current_date: datetime.datetime,
                          last_service_date: datetime.datetime,
                          warning_light_on: bool,
                          tires: List[float]) -> Car:

        engine = SternmanEngine(
            warning_light_is_on=warning_light_on)
        battery = SpindlerBattery(
            current_date=current_date, last_service_date=last_service_date)
        _tires = CarriganTire(tires=tires)

        return Car(engine=engine, battery=battery, tires=_tires)

    @staticmethod
    def create_rorschach(current_date: datetime.datetime,
                         last_service_date: datetime.datetime,
                         current_mileage: int,
                         last_service_mileage: int,
                         tires: List[float]) -> Car:

        engine = WilloughbyEngine(
            last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        battery = NubbinBattery(
            current_date=current_date, last_service_date=last_service_date)
        _tires = OctoprimeTire(tires=tires)

        return Car(engine=engine, battery=battery, tires=_tires)

    @staticmethod
    def create_thovex(current_date: datetime.datetime,
                      last_service_date: datetime.datetime,
                      current_mileage: int,
                      last_service_mileage: int,
                      tires: List[float]) -> Car:

        engine = CapuletEngine(
            last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        battery = NubbinBattery(
            current_date=current_date, last_service_date=last_service_date)
        _tires = OctoprimeTire(tires=tires)

        return Car(engine=engine, battery=battery, tires=_tires)
