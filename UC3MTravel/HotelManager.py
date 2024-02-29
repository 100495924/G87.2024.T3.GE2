import json
from .HotelManagementException import HotelManagementException
from .HotelReservation import HotelReservation

class HotelManager:
    def __init__(self):
        pass

    def validatecreditcard( self, card_id: str):
        check_digit = card_id[len(card_id) - 1]
        payload = card_id[:len(card_id) - 1]
        sum = 0
        double = True
        for i in range(len(card_id) - 2, -1, -1):
            if double:
                sum_digit = 2 * int(payload[i])
            else:
                sum_digit = int(payload[i])
            if sum_digit >= 10:
                sum_digit = 1 + sum_digit % 10
            sum += sum_digit
            double = not double
        return int(check_digit) == 10 - (sum % 10)

    def ReaddatafromJSOn( self, fi):

        try:
            with open(fi) as f:
                DATA = json.load(f)
        except FileNotFoundError as e:
            raise HotelManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from e


        try:
            c = DATA["CreditCard"]
            p = DATA["phoneNumber"]
            req = HotelReservation(IDCARD="12345678Z",creditcardNumb=c,nAMeAndSURNAME="John Doe",phonenumber=p,room_type="single",numdays=3)
        except KeyError as e:
            raise HotelManagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.validatecreditcard(c):
            raise HotelManagementException("Invalid credit card number")

        # Close the file
        return req