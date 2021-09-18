from types import MethodType


class Car(object):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("make", "")
        kwargs.setdefault("model", "")
        kwargs.setdefault("mileage", 0)
        kwargs.setdefault("mpg", 0)

        self._make = kwargs["make"]
        self._model = kwargs["model"]
        self._mileage = kwargs["mileage"]
        self._mpg = kwargs["mpg"]

    def compare(self, o: object, value: int) -> int:
        if value == 0:
            return self.__compare(self.get_make(), o.get_make())
        if value == 1:
            return self.__compare(self.get_model(), o.get_model())
        if value == 2:
            return self.__compare(self.get_mileage, o.get_mileage())
        if value == 3:
            return self.__compare(self.get_mpg, o.get_mpg())
        return 0

    def compare(self, omethod=None) -> int:
        if omethod is None or type(omethod) is not MethodType:
            raise TypeError("omethod must be a getter from the Car class.")

        if self.get_make.__name__ == omethod.__name__:
            return self.__compare(self.get_make(), omethod())
        if self.get_mileage.__name__ == omethod.__name__:
            return self.__compare(self.get_mileage(), omethod())
        if self.get_model.__name__ == omethod.__name__:
            return self.__compare(self.get_model(), omethod())
        if self.get_mpg.__name__ == omethod.__name__:
            return self.__compare(self.get_mpg(), omethod())
        return 0

    def __compare(self, this: object, that: object) -> int:
        if this == that: 
            return 0
        elif this > that:
            return 1
        else:
            return -1

    def get_make(self):
        return self._make

    def set_make(self, make):
        self._make = make

    def get_model(self):
        return self._model

    def set_model(self, model):
        self._model = model

    def get_mileage(self):
        return self._mileage

    def set_mileage(self, mileage):
        self._mileage = mileage

    def get_mpg(self):
        return self._mpg

    def set_mpg(self, mpg):
        self._mpg = mpg

    def __str__(self):
        return "{a} {b} | Miles: {c} | MPG: {d}".format(a = self._make, b = self._model, c = self._mileage, d = self._mpg)

    def __eq__(self, o: object) -> bool:
        return self._make == o.get_make() and self._model == o.get_model() and self._mileage == o.get_mileage() and self._mpg == o.get_mpg()

    def __ne__(self, o: object) -> bool:
        return not self.__eq__(o)

    def __lt__(self, o: object) -> bool:
        if self._make < o.get_make():
            return True
        elif self._model < o.get_model():
            return True
        elif self._mileage < o.get_mileage():
            return True
        elif self._mpg < o.get_mpg():
            return True
        return False

    def __gt__(self, o: object) -> bool:
        if self._make > o.get_make():
            return True
        elif self._model > o.get_model():
            return True
        elif self._mileage > o.get_mileage():
            return True
        elif self._mpg > o.get_mpg():
            return True
        return False
