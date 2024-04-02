""" HotelReservation module"""
import hashlib
from datetime import datetime


class HotelReservation:
    """ HotelReservation class"""
    def __init__(self, id_card, credit_card, name_surname, phone_number, room_type, arrival_date, num_days):
        self.__credit_card = credit_card
        self.__id_card = id_card
        justnow = datetime.utcnow()
        self.__arrival_date = arrival_date
        self.__reservation_date = datetime.timestamp(justnow)
        self.__name_surname = name_surname
        self.__phone_number = phone_number
        self.__room_type = room_type
        self.__num_days = num_days

    def __str__(self):
        """return a json string with the elements required to calculate the localizer"""
        # VERY IMPORTANT: JSON KEYS CANNOT BE RENAMED
        json_info = {"id_card": self.__id_card,
                     "name_surname": self.__name_surname,
                     "credit_card": self.__credit_card,
                     "phone_number:": self.__phone_number,
                     "reservation_date": self.__reservation_date,
                     "arrival_date": self.__arrival_date,
                     "num_days": self.__num_days,
                     "room_type": self.__room_type,
                     }
        return "HotelReservation:" + str(json_info)

    @property
    def credit_card(self):
        """ Property representing the credit card"""
        return self.__credit_card

    @credit_card.setter
    def credit_card(self, value):
        """ setter for credit card"""
        self.__credit_card = value

    @property
    def id_card(self):
        """ Property representing the id card"""
        return self.__id_card

    @id_card.setter
    def id_card(self, value):
        """ Setter of id_card"""
        self.__id_card = value

    @property
    def arrival_date(self):
        """ Property representing the arrival date"""
        return self.__arrival_date

    @arrival_date.setter
    def arrival_date(self, value):
        """ setter for arrival_date"""
        self.__arrival_date = value

    @property
    def reservation_date(self):
        """ Property representing the reservation date"""
        return self.__reservation_date

    @reservation_date.setter
    def reservation_date(self, value):
        """ setter for reservation_date"""
        self.__reservation_date = value

    @property
    def name_surname(self):
        """ Property that represents the name and surrname."""
        return self.__name_surname

    @name_surname.setter
    def name_surname(self, value):
        """ Setter for name_surname"""
        self.__name_surname = value

    @property
    def phone_number(self):
        """ Property representing the phone number"""
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        """ Setter for phone_number"""
        self.__phone_number = value

    @property
    def room_type(self):
        """ Property representing the room type"""
        return self.__room_type

    @room_type.setter
    def room_type(self, value):
        """ setter for room_type"""
        self.__room_type = value

    @property
    def num_days(self):
        """ Property representing the number of days"""
        return self.__num_days

    @num_days.setter
    def num_days(self, value):
        """ Setter for num_days"""
        self.__num_days = value

    @property
    def localizer(self):
        """Returns the md5 signature"""
        return hashlib.md5(str(self).encode()).hexdigest()
