import hashlib
import json
from datetime import datetime


class HotelReservation:
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
        return "HotelReservation:" + json_info.__str__()

    @property
    def credit_card(self):
        return self.__credit_card

    @credit_card.setter
    def credit_card(self, value):
        self.__credit_card = value

    @property
    def id_card(self):
        return self.__id_card

    @id_card.setter
    def id_card(self, value):
        self.__id_card = value

    @property
    def arrival_date(self):
        return self.__arrival_date

    @arrival_date.setter
    def arrival_date(self, value):
        self.__arrival_date = value

    @property
    def reservation_date(self):
        return self.__reservation_date

    @reservation_date.setter
    def reservation_date(self, value):
        self.__reservation_date = value

    @property
    def name_surname(self):
        return self.__name_surname

    @name_surname.setter
    def name_surname(self, value):
        self.__name_surname = value

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        self.__phone_number = value

    @property
    def room_type(self):
        return self.__room_type

    @room_type.setter
    def room_type(self, value):
        self.__room_type = value

    @property
    def num_days(self):
        return self.__num_days

    @num_days.setter
    def num_days(self, value):
        self.__num_days = value

    @property
    def localizer(self):
        """Returns the md5 signature"""
        return hashlib.md5(self.__str__().encode()).hexdigest()
