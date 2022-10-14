##
# maths_tools.py

import math
from dataclasses import dataclass

# these tools can only provide information as accurate as it is given


@dataclass
class Displacement:
    _meters = None

    @property
    def nanometers(self):
        return self._meters * 1000000000

    @nanometers.setter
    def nanometers(self, new_value: float | int):
        if type(new_value) is not float | int:
            raise TypeError("'new_value' must be a float or int")
        self._meters = float(new_value * 1000000000)

    @property
    def micrometers(self):
        return self._meters * 1000000

    @micrometers.setter
    def micrometers(self, new_value: float | int):
        if type(new_value) is not float | int:
            raise TypeError("'new_value' must be a float or int")
        self._meters = float(new_value * 1000000)

    @property
    def millimeters(self):
        return self._meters * 1000

    @millimeters.setter
    def millimeters(self, new_value: float | int):
        if type(new_value) is not float | int:
            raise TypeError("'new_value' must be a float or int")
        self._meters = float(new_value * 1000)

    @property
    def meters(self):
        return self._meters

    @meters.setter
    def meters(self, new_value: float | int):
        if type(new_value) is not float | int:
            raise TypeError("'new_value' must be a float or int")
        self._meters = float(new_value)

    @property
    def kilometers(self):
        return self._meters / 1000

    @kilometers.setter
    def kilometers(self, new_value: float | int):
        if type(new_value) is not float | int:
            raise TypeError("'new_value' must be a float or int")
        self.meters = float(new_value * 1000)

    @property
    def astronomical_units(self):
        return self._meters / 149597870700

    @astronomical_units.setter
    def astronomical_units(self, new_value: float | int):
        if type(new_value) is not float | int:
            raise TypeError("'new_value' must be a float or int")
        self.meters = float(new_value * 149597870700)

    @property
    def lightyears(self):
        return self._metres / 9.4605284e15

    @lightyears.setter
    def lightyears(self, new_value: float | int):
        if type(new_value) is not float | int:
            raise TypeError("'new_value' must be a float or int")
        self._meters = float(new_value * 9.4605284e15)

@dataclass
class Area:
    _meters = None

    @property
    def nanometers(self):
        return self._meters * (1000000000 ** 2)

    @nanometers.setter
    def nanometers(self, new_value: float | int):
        if type(new_value) is not float | int:
            raise TypeError("'new_value' must be a float or int")
        self._meters = float(new_value * (1000000000 ** 2))

    @property
    def micrometers(self):
        return self._meters * (1000000 ** 2)

    @micrometers.setter
    def micrometers(self, new_value: float | int):
        if type(new_value) is not float | int:
            raise TypeError("'new_value' must be a float or int")
        self._meters = float(new_value * (1000000 ** 2))

    @property
    def millimeters(self):
        return self._meters * (1000 ** 2)

    @millimeters.setter
    def millimeters(self, new_value: float | int):
        if type(new_value) is not float | int:
            raise TypeError("'new_value' must be a float or int")
        self._meters = float(new_value * (1000 ** 2))

    @property
    def meters(self):
        return self._meters

    @meters.setter
    def meters(self, new_value: float | int):
        if type(new_value) is not float | int:
            raise TypeError("'new_value' must be a float or int")
        self._meters = float(new_value)

    @property
    def kilometers(self):
        return self._meters / (1000 ** 2)

    @kilometers.setter
    def kilometers(self, new_value: float | int):
        if type(new_value) is not float | int:
            raise TypeError("'new_value' must be a float or int")
        self.meters = float(new_value * (1000 ** 2))

    @property
    def astronomical_units(self):
        return self._meters / (149597870700 ** 2)

    @astronomical_units.setter
    def astronomical_units(self, new_value: float | int):
        if type(new_value) is not float | int:
            raise TypeError("'new_value' must be a float or int")
        self.meters = float(new_value * (149597870700 ** 2))

    @property
    def lightyears(self):
        return self._metres / (9.4605284e15 ** 2)

    @lightyears.setter
    def lightyears(self, new_value: float | int):
        if type(new_value) is not float | int:
            raise TypeError("'new_value' must be a float or int")
        self._meters = float(new_value * (9.4605284e15 ** 2))

@dataclass
class Volume:
    _meters = None

    @property
    def nanometers(self):
        return self._meters * (1000000000 ** 3)

    @nanometers.setter
    def nanometers(self, new_value: float | int):
        if type(new_value) is not float | int:
            raise TypeError("'new_value' must be a float or int")
        self._meters = float(new_value * (1000000000 ** 3))

    @property
    def micrometers(self):
        return self._meters * (1000000 ** 3)

    @micrometers.setter
    def micrometers(self, new_value: float | int):
        if type(new_value) is not float | int:
            raise TypeError("'new_value' must be a float or int")
        self._meters = float(new_value * (1000000 ** 3))

    @property
    def millimeters(self):
        return self._meters * (1000 ** 3)

    @millimeters.setter
    def millimeters(self, new_value: float | int):
        if type(new_value) is not float | int:
            raise TypeError("'new_value' must be a float or int")
        self._meters = float(new_value * (1000 ** 3))

    @property
    def meters(self):
        return self._meters

    @meters.setter
    def meters(self, new_value: float | int):
        if type(new_value) is not float | int:
            raise TypeError("'new_value' must be a float or int")
        self._meters = float(new_value)

    @property
    def kilometers(self):
        return self._meters / (1000 ** 3)

    @kilometers.setter
    def kilometers(self, new_value: float | int):
        if type(new_value) is not float | int:
            raise TypeError("'new_value' must be a float or int")
        self.meters = float(new_value * (1000 ** 3))

    @property
    def astronomical_units(self):
        return self._meters / (149597870700 ** 3)

    @astronomical_units.setter
    def astronomical_units(self, new_value: float | int):
        if type(new_value) is not float | int:
            raise TypeError("'new_value' must be a float or int")
        self.meters = float(new_value * (149597870700 ** 3))

    @property
    def lightyears(self):
        return self._metres / (9.4605284e15 ** 3)

    @lightyears.setter
    def lightyears(self, new_value: float | int):
        if type(new_value) is not float | int:
            raise TypeError("'new_value' must be a float or int")
        self._meters = float(new_value * (9.4605284e15 ** 3))

