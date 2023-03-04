from typing import List

from tire.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, tires: List[float]):
        self.tires = tires

    def needs_service(self) -> bool:
        return sum(self.tires) >= 3.0
