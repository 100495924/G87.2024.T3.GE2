""" Class HotelStay (GE2.2) """
from datetime import datetime
import hashlib

class HotelStay():
    """ HotelStay class."""
    def __init__(self, idcard, localizer, numdays, roomtype):
        self.__alg = "SHA-256"
        self.__type = roomtype
        self.__idcard = idcard
        self.__localizer = localizer
        justnow = datetime.utcnow()
        self.__arrival = datetime.timestamp(justnow)
        # timestamp is represented in seconds.miliseconds
        # to add the number of days we must express numdays in seconds
        self.__departure = self.__arrival + (numdays * 24 * 60 * 60)
        self.__room_key = self.room_key

    def __signature_string(self):
        """Composes the string to be used for generating the key for the room"""
        return "{alg:" + self.__alg + ",typ:" + self.__type + ",localizer:" + \
            self.__localizer + ",arrival:" + str(self.__arrival) + \
            ",departure:" + str(self.__departure) + "}"

    @property
    def type(self):
        """ property that represents the type of room"""
        return self.__type

    @property
    def id_card(self):
        """Property that represents the id_card of the guest."""
        return self.__idcard

    @id_card.setter
    def id_card(self, value):
        self.__idcard = value

    @property
    def localizer(self):
        """Property that represents the localizer"""
        return self.__localizer

    @localizer.setter
    def localizer(self, value):
        self.__localizer = value

    @property
    def arrival(self):
        """Property that represents the arrival date of the client."""
        return self.__arrival

    @property
    def room_key(self):
        """Returns the sha256 signature of the date"""
        return hashlib.sha256(self.__signature_string().encode()).hexdigest()

    @property
    def departure(self):
        """Property that represents the departure date."""
        return self.__departure

    @departure.setter
    def departure(self, value):
        self.__departure = value
