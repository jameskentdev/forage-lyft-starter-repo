from tire.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self):
        pass

    def needs_service(self) -> bool:
        return False
