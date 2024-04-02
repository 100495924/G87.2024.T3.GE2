""" Module that tests the roomReservation() function"""
from unittest import TestCase
from datetime import datetime
import os
from freezegun import freeze_time  # pip install freezegun
from UC3MTravel.HotelManager import HotelManager
from UC3MTravel.HotelManagementException import HotelManagementException


class TestRoomReservation(TestCase):
    """Test cases for roomReservation (Function 1)"""
    def setUp(self):
        self.my_hotel_manager = HotelManager()

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation01(self):
        """Test 1: Valid credit_card"""
        value = self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                      name_surname="John Smith",
                                                      id_card="12345678Z",
                                                      phone_number="612345789",
                                                      room_type="single",
                                                      arrival_date="01/07/2024",
                                                      num_days=1)
        self.assertEqual(value, "385148f30bfe0c80599f7c844216578a")
        json_dir = self.my_hotel_manager.getJsonDirectory("reservations_store")
        filename = "12345678Z.json"
        processed_json_path = os.path.join(json_dir, filename)
        os.remove(processed_json_path)

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation02(self):
        """Test 2: credit_card of datatype int"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card=5105105105105100,
                                                  name_surname="John Smith",
                                                  id_card="12345678Z",
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date="01/07/2024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "credit_card is not a string")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation03(self):
        """Test 3: credit_card has 15 digits"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="510510510510510",
                                                  name_surname="John Smith",
                                                  id_card="12345678Z",
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date="01/07/2024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "credit_card is not 16 characters long")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation04(self):
        """Test 4: credit_card has 17 digits"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="51051051051051000",
                                                  name_surname="John Smith",
                                                  id_card="12345678Z",
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date="01/07/2024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "credit_card is not 16 characters long")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation05(self):
        """Test 5: credit_card has 16 characters but not all of them are digits"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="A105105105105100",
                                                  name_surname="John Smith",
                                                  id_card="12345678Z",
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date="01/07/2024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "credit_card must have 16 digits")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation06(self):
        """Test 6: credit_card does not follow Luhn algorithm (last digit is wrong)"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105101",
                                                  name_surname="John Smith",
                                                  id_card="12345678Z",
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date="01/07/2024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "credit_card does not follow the Luhn algorithm")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation07(self):
        """Test 7: name_surname with more than 2 strings separated by a white space"""
        value = self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                      name_surname="John Jack Smith",
                                                      id_card="12345678Z",
                                                      phone_number="612345789",
                                                      room_type="single",
                                                      arrival_date="01/07/2024",
                                                      num_days=1)
        self.assertEqual(value, "9082506560e5457fb0089c4b48ccdb42")
        json_dir = self.my_hotel_manager.getJsonDirectory("reservations_store")
        filename = "12345678Z.json"
        processed_json_path = os.path.join(json_dir, filename)
        os.remove(processed_json_path)

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation08(self):
        """Test 8: name_surname has 11 characters"""
        value = self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                      name_surname="John Smithy",
                                                      id_card="12345678Z",
                                                      phone_number="612345789",
                                                      room_type="single",
                                                      arrival_date="01/07/2024",
                                                      num_days=1)
        self.assertEqual(value, "9f27edcc737a118c24908738601423ba")
        json_dir = self.my_hotel_manager.getJsonDirectory("reservations_store")
        filename = "12345678Z.json"
        processed_json_path = os.path.join(json_dir, filename)
        os.remove(processed_json_path)

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation09(self):
        """Test 9: name_surname has 49 characters"""
        value = self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                      name_surname="John SmithSmithSmithSmithSmithSmithSmithSmithSmit",
                                                      id_card="12345678Z",
                                                      phone_number="612345789",
                                                      room_type="single",
                                                      arrival_date="01/07/2024",
                                                      num_days=1)
        self.assertEqual(value, "3ca03f80303fd71b309a2b9f1c51b25d")
        json_dir = self.my_hotel_manager.getJsonDirectory("reservations_store")
        filename = "12345678Z.json"
        processed_json_path = os.path.join(json_dir, filename)
        os.remove(processed_json_path)

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation10(self):
        """Test 10: name_surname has 50 characters"""
        value = self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                      name_surname="John SmithSmithSmithSmithSmithSmithSmithSmithSmith",
                                                      id_card="12345678Z",
                                                      phone_number="612345789",
                                                      room_type="single",
                                                      arrival_date="01/07/2024",
                                                      num_days=1)
        self.assertEqual(value, "bb948f04a913f377edacbab412fe56e3")
        json_dir = self.my_hotel_manager.getJsonDirectory("reservations_store")
        filename = "12345678Z.json"
        processed_json_path = os.path.join(json_dir, filename)
        os.remove(processed_json_path)

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation11(self):
        """Test 11: name_surname of datatype int"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname=1,
                                                  id_card="12345678Z",
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date="01/07/2024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "name_surname is not a string")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation12(self):
        """Test 12: name_surname has only 1 string (0 white spaces)"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="JohnSmithy",
                                                  id_card="12345678Z",
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date="01/07/2024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message,
                         "name_surname must contain at least 2 strings separated by a white space")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation13(self):
        """Test 13: name_surname has more than 1 white space between 2 strings"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="John  Smith",
                                                  id_card="12345678Z",
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date="01/07/2024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message,
                         "name_surname must contain at least 2 strings separated by a white space")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation14(self):
        """Test 14: name_surname has 9 characters"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="John Smit",
                                                  id_card="12345678Z",
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date="01/07/2024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "name_surname must be between 10 and 50 characters long")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation15(self):
        """Test 15: name_surname has 51 characters"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="John SmithSmithSmithSmithSmithSmithSmithSmithSmithy",
                                                  id_card="12345678Z",
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date="01/07/2024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "name_surname must be between 10 and 50 characters long")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation16(self):
        """Test 16: id_card of datatype int"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="John Smith",
                                                  id_card=12345678,
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date="01/07/2024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "id_card is not a string")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation17(self):
        """Test 17: id_card has 8 characters at the beginning but not all of them are digits"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="John Smith",
                                                  id_card="AB12C678Z",
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date="01/07/2024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "id_card must have 8 digits and 1 final letter")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation18(self):
        """Test 18: id_card has less than 8 digits"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="John Smith",
                                                  id_card="1234567Z",
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date="01/07/2024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "id_card must have 8 digits and 1 final letter")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation19(self):
        """Test 19: id_card has more than 8 digits"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="John Smith",
                                                  id_card="123456789Z",
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date="01/07/2024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "id_card must have 8 digits and 1 final letter")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation20(self):
        """Test 20: The last character of id_card is not a letter nor a digit"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="John Smith",
                                                  id_card="12345678#",
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date="01/07/2024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "id_card must have 8 digits and 1 final letter")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation21(self):
        """Test 21: id_card has less than 1 letter at the end"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="John Smith",
                                                  id_card="12345678",
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date="01/07/2024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "id_card must have 8 digits and 1 final letter")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation22(self):
        """Test 22: id_card has more than 1 letter at the end"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="John Smith",
                                                  id_card="12345678ZZ",
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date="01/07/2024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "id_card must have 8 digits and 1 final letter")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation23(self):
        """Test 23: Invalid letter for id_card according to the algorithm"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="John Smith",
                                                  id_card="12345678A",
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date="01/07/2024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "invalid letter for id_card")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation24(self):
        """Test 24: id_card belongs to a client that already has a reservation file"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="John Smith",
                                                  id_card="00000000T",
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date="01/07/2024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "a client with specified id_card already has a reservation")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation25(self):
        """Test 25: phone_number of datatype int"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="John Smith",
                                                  id_card="12345678Z",
                                                  phone_number=612345789,
                                                  room_type="single",
                                                  arrival_date="01/07/2024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "phone_number is not a string")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation26(self):
        """Test 26: phone_number has 9 characters but not all of them are digits"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="John Smith",
                                                  id_card="12345678Z",
                                                  phone_number="A12345789",
                                                  room_type="single",
                                                  arrival_date="01/07/2024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "phone_number must have 9 digits")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation27(self):
        """Test 27: phone_number has less than 9 digits"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="John Smith",
                                                  id_card="12345678Z",
                                                  phone_number="61234578",
                                                  room_type="single",
                                                  arrival_date="01/07/2024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "phone_number is not 9 characters long")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation28(self):
        """Test 28: phone_number has more than 9 digits"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="John Smith",
                                                  id_card="12345678Z",
                                                  phone_number="6123457890",
                                                  room_type="single",
                                                  arrival_date="01/07/2024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "phone_number is not 9 characters long")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation29(self):
        """Test 29: Valid room_type value ("double")"""
        value = self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                      name_surname="John Smith",
                                                      id_card="12345678Z",
                                                      phone_number="612345789",
                                                      room_type="double",
                                                      arrival_date="01/07/2024",
                                                      num_days=1)
        self.assertEqual(value, "fa5a80736b0b59461642e6511e8a1f9e")
        json_dir = self.my_hotel_manager.getJsonDirectory("reservations_store")
        filename = "12345678Z.json"
        processed_json_path = os.path.join(json_dir, filename)
        os.remove(processed_json_path)

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation30(self):
        """Test 30: Valid room_type value ("suite")"""
        value = self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                      name_surname="John Smith",
                                                      id_card="12345678Z",
                                                      phone_number="612345789",
                                                      room_type="suite",
                                                      arrival_date="01/07/2024",
                                                      num_days=1)
        self.assertEqual(value, "e05811f7d87dc9eb54ffa6080d425dd4")
        json_dir = self.my_hotel_manager.getJsonDirectory("reservations_store")
        filename = "12345678Z.json"
        processed_json_path = os.path.join(json_dir, filename)
        os.remove(processed_json_path)

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation31(self):
        """Test 31: room_type of datatype int"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="John Smith",
                                                  id_card="12345678Z",
                                                  phone_number="612345789",
                                                  room_type=1,
                                                  arrival_date="01/07/2024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "room_type is not a string")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation32(self):
        """Test 32: Invalid room_type value"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="John Smith",
                                                  id_card="12345678Z",
                                                  phone_number="612345789",
                                                  room_type="other",
                                                  arrival_date="01/07/2024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "invalid room_type value")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation33(self):
        """Test 33: arrival_date is 1 day after the current time"""
        value = self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                      name_surname="John Smith",
                                                      id_card="12345678Z",
                                                      phone_number="612345789",
                                                      room_type="single",
                                                      arrival_date="02/07/2024",
                                                      num_days=1)
        self.assertEqual(value, "f7dcfc6221b24ce9c176aa61d8b123dd")
        json_dir = self.my_hotel_manager.getJsonDirectory("reservations_store")
        filename = "12345678Z.json"
        processed_json_path = os.path.join(json_dir, filename)
        os.remove(processed_json_path)

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation34(self):
        """Test 34: arrival_date of datatype int"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="John Smith",
                                                  id_card="12345678Z",
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date=172024,
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "arrival_date is not a string")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation35(self):
        """Test 35: Day of arrival_date is 2 characters but not all of them are digits"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="John Smith",
                                                  id_card="12345678Z",
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date="A1/07/2024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "invalid arrival_date format \"DD/MM/YYYY\"")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation36(self):
        """Test 36: Day of arrival_date is less than 2 digits"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="John Smith",
                                                  id_card="12345678Z",
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date="1/07/2024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "invalid arrival_date format \"DD/MM/YYYY\"")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation37(self):
        """Test 37: Day of arrival_date is more than 2 digits"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="John Smith",
                                                  id_card="12345678Z",
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date="001/07/2024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "invalid arrival_date format \"DD/MM/YYYY\"")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation38(self):
        """Test 38: Month of arrival_date is 2 characters but not all of them are digits"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="John Smith",
                                                  id_card="12345678Z",
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date="01/A7/2024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "invalid arrival_date format \"DD/MM/YYYY\"")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation39(self):
        """Test 39: Month of arrival_date is less than 2 digits"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="John Smith",
                                                  id_card="12345678Z",
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date="01/7/2024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "invalid arrival_date format \"DD/MM/YYYY\"")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation40(self):
        """Test 40: Month of arrival_date is more than 2 digits"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="John Smith",
                                                  id_card="12345678Z",
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date="01/007/2024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "invalid arrival_date format \"DD/MM/YYYY\"")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation41(self):
        """Test 41: Year of arrival_date is 4 characters but not all of them are digits"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="John Smith",
                                                  id_card="12345678Z",
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date="01/07/A024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "invalid arrival_date format \"DD/MM/YYYY\"")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation42(self):
        """Test 42: Year of arrival_date is less than 4 digits"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="John Smith",
                                                  id_card="12345678Z",
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date="01/07/024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "invalid arrival_date format \"DD/MM/YYYY\"")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation43(self):
        """Test 43: Year of arrival_date is more than 4 digits"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="John Smith",
                                                  id_card="12345678Z",
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date="01/07/02024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "invalid arrival_date format \"DD/MM/YYYY\"")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation44(self):
        """Test 44: arrival_date has a character between day and month that is not "/" """
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="John Smith",
                                                  id_card="12345678Z",
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date="01-07/2024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "invalid arrival_date format \"DD/MM/YYYY\"")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation45(self):
        """Test 45: arrival_date has less than 1 "/" between day and month"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="John Smith",
                                                  id_card="12345678Z",
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date="0107/2024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "invalid arrival_date format \"DD/MM/YYYY\"")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation46(self):
        """Test 46: arrival_date has more than 1 "/" between day and month"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="John Smith",
                                                  id_card="12345678Z",
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date="01//07/2024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "invalid arrival_date format \"DD/MM/YYYY\"")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation47(self):
        """Test 47: arrival_date has a character between month and year that is not "/" """
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="John Smith",
                                                  id_card="12345678Z",
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date="01/07-2024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "invalid arrival_date format \"DD/MM/YYYY\"")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation48(self):
        """Test 48: arrival_date has less than 1 "/" between month and year"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="John Smith",
                                                  id_card="12345678Z",
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date="01/072024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "invalid arrival_date format \"DD/MM/YYYY\"")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation49(self):
        """Test 49: arrival_date has more than 1 "/" between month and year"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="John Smith",
                                                  id_card="12345678Z",
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date="01/07//2024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "invalid arrival_date format \"DD/MM/YYYY\"")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation50(self):
        """Test 50: arrival_date does not exist"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="John Smith",
                                                  id_card="12345678Z",
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date="91/07/2024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "arrival_date does not exist")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation51(self):
        """Test 51: arrival_date is before the current time"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="John Smith",
                                                  id_card="12345678Z",
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date="30/06/2024",
                                                  num_days=1)
        self.assertEqual(ex.exception.message, "arrival_date before current date")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation52(self):
        """Test 52: num_days is 2"""
        value = self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                      name_surname="John Smith",
                                                      id_card="12345678Z",
                                                      phone_number="612345789",
                                                      room_type="single",
                                                      arrival_date="01/07/2024",
                                                      num_days=2)
        self.assertEqual(value, "7bb82656140fdcad38da6a7f323a0d57")
        json_dir = self.my_hotel_manager.getJsonDirectory("reservations_store")
        filename = "12345678Z.json"
        processed_json_path = os.path.join(json_dir, filename)
        os.remove(processed_json_path)

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation53(self):
        """Test 53: num_days is 9"""
        value = self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                      name_surname="John Smith",
                                                      id_card="12345678Z",
                                                      phone_number="612345789",
                                                      room_type="single",
                                                      arrival_date="01/07/2024",
                                                      num_days=9)
        self.assertEqual(value, "36b4d8e28eb343a54ecb0bbe9e880233")
        json_dir = self.my_hotel_manager.getJsonDirectory("reservations_store")
        filename = "12345678Z.json"
        processed_json_path = os.path.join(json_dir, filename)
        os.remove(processed_json_path)

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation54(self):
        """Test 54: num_days is 10"""
        value = self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                      name_surname="John Smith",
                                                      id_card="12345678Z",
                                                      phone_number="612345789",
                                                      room_type="single",
                                                      arrival_date="01/07/2024",
                                                      num_days=10)
        self.assertEqual(value, "23aa42c0b1d9b69ecde79c5677ce7c7f")
        json_dir = self.my_hotel_manager.getJsonDirectory("reservations_store")
        filename = "12345678Z.json"
        processed_json_path = os.path.join(json_dir, filename)
        os.remove(processed_json_path)

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation55(self):
        """Test 55: num_days of datatype string"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="John Smith",
                                                  id_card="12345678Z",
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date="01/07/2024",
                                                  num_days="1")
        self.assertEqual(ex.exception.message, "num_days is not an int")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation56(self):
        """Test 56: num_days is 0"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="John Smith",
                                                  id_card="12345678Z",
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date="01/07/2024",
                                                  num_days=0)
        self.assertEqual(ex.exception.message, "num_days must be between 1 and 10")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def test_room_reservation57(self):
        """Test 57: num_days is 11"""
        with self.assertRaises(HotelManagementException) as ex:
            self.my_hotel_manager.roomReservation(credit_card="5105105105105100",
                                                  name_surname="John Smith",
                                                  id_card="12345678Z",
                                                  phone_number="612345789",
                                                  room_type="single",
                                                  arrival_date="01/07/2024",
                                                  num_days=11)
        self.assertEqual(ex.exception.message, "num_days must be between 1 and 10")
