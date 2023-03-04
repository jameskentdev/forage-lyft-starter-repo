from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self):
        pass

    def needs_service(self) -> bool:
        return False
