import json
from .HotelManagementException import HotelManagementException
from .HotelReservation import HotelReservation

class HotelManager:
    def __init__(self):
        pass

    def roomReservation(self, credit_card, name_surname, id_card, room_type, arrival_date, num_days):
        pass

    def validateCreditCard( self, card_id: str):
        check_digit = card_id[len(card_id) - 1]
        payload = card_id[:len(card_id) - 1]
        sum_total = 0
        double = True
        for i in range(len(card_id) - 2, -1, -1):
            if double:
                sum_digit = 2 * int(payload[i])
            else:
                sum_digit = int(payload[i])
            if sum_digit >= 10:
                sum_digit = 1 + sum_digit % 10
            sum_total += sum_digit
            double = not double
        return int(check_digit) == (10 - (sum_total % 10)) % 10

    def readDataFromJson( self, fi):

        try:
            with open(fi) as f:
                data = json.load(f)
        except FileNotFoundError as e:
            raise HotelManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from e

        try:
            c = data["CreditCard"]
            p = data["phoneNumber"]
            req = HotelReservation(id_card="12345678Z", credit_card=c, name_surname="John Doe", phone_number=p,
                                   room_type="single", arrival_date="01/07/2024", num_days=3)
        except KeyError as e:
            raise HotelManagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.validateCreditCard(c):
            raise HotelManagementException("Invalid credit card number")

        # Close the file
        return req
