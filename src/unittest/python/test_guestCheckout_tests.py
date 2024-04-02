import os
from unittest import TestCase, mock
from freezegun import freeze_time
from datetime import datetime
from src.main.python.UC3MTravel.HotelManager import HotelManager
from src.main.python.UC3MTravel.HotelManagementException import HotelManagementException

class TestGuestCheckout(TestCase):

    def setUp(self):
        self.hotel_manager = HotelManager()

    @freeze_time("2024-01-07")
    def test_guest_checkout_valid(self):
        """ TC1: Valid checkout with correct room key and departure date"""
        room_key = "400f35f55fc2be1b5022aec0e2509cd53ca6cd9017e6e5da4cfe375d18758617"
        with mock.patch("os.path.exists", return_value=True), \
            mock.patch("builtins.open", mock.mock_open(read_data='{"departure": "07/01/2024 12:00:00"}')):
            self.assertTrue(self.hotel_manager.guest_checkout(room_key))

    @freeze_time("2024-01-07")
    def test_guest_checkout_invalid_room_key_format(self):
        """ TC2: Invalid room key format"""
        room_key = "invalidkey123"
        with self.assertRaises(HotelManagementException) as context:
            self.hotel_manager.guest_checkout(room_key)
        self.assertEqual(str(context.exception), "Invalid room key format.")

    @freeze_time("2024-01-07")
    def test_guest_checkout_room_key_not_found(self):
        """ TC3: Room key not found in processed stays store"""
        room_key = "400f35f55fc2be1b5022aec0e2509cd53ca6cd9017e6e5da4cfe375d18758617"
        with mock.patch("os.path.exists", return_value=False):
            with self.assertRaises(HotelManagementException) as context:
                self.hotel_manager.guest_checkout(room_key)
        self.assertEqual(str(context.exception), "Room key not found in processed stays store.")

    @freeze_time("2024-01-08")
    def test_guest_checkout_invalid_departure_date(self):
        """ TC4: Invalid departure date (not today)"""
        room_key = "400f35f55fc2be1b5022aec0e2509cd53ca6cd9017e6e5da4cfe375d18758617"
        with mock.patch("os.path.exists", return_value=True), \
             mock.patch("builtins.open", mock.mock_open(read_data='{"departure": "07/01/2024 12:00:00"}')):
            with self.assertRaises(HotelManagementException) as context:
                self.hotel_manager.guest_checkout(room_key)
        self.assertEqual(str(context.exception), "Departure date is not valid.")

    @freeze_time("2024-01-07")
    def test_guest_checkout_room_key_data_mismatch(self):
        """ TC5: Room key exists but data mismatch"""
        room_key = "valid_md5_but_mismatch_data"
        with mock.patch("os.path.exists", return_value=True), \
                mock.patch("builtins.open", mock.mock_open(read_data='{"departure": "06/01/2024 12:00:00"}')):
            with self.assertRaises(HotelManagementException) as context:
                self.hotel_manager.guest_checkout(room_key)
        self.assertIn("Departure date is not valid.", str(context.exception))

    @freeze_time("2024-01-07")
    def test_guest_checkout_file_read_exception(self):
        """ TC6: Exception raised due to inability to read the stay file"""
        room_key = "valid_md5_hash_causes_read_exception"
        with mock.patch("os.path.exists", return_value=True), \
                mock.patch("builtins.open", mock.mock_open(read_data='{"departure": "07/01/2024 12:00:00"}')) as mock_file:
            mock_file.side_effect = Exception("Read error")
            with self.assertRaises(Exception) as context:
                self.hotel_manager.guest_checkout(room_key)
        self.assertEqual("Read error", str(context.exception))

    @freeze_time("2024-01-07")
    def test_guest_checkout_file_write_exception(self):
        """ TC7: Exception raised due to inability to write to the checkout file"""
        room_key = "valid_md5_hash_causes_write_exception"
        with mock.patch("os.path.exists", return_value=True), \
                mock.patch("builtins.open", mock.mock_open(read_data='{"departure": "07/01/2024 12:00:00"}')):
            with mock.patch("json.dump") as mock_json_dump:
                mock_json_dump.side_effect = Exception("Write error")
                with self.assertRaises(Exception) as context:
                    self.hotel_manager.saveDepartureData(room_key, {"departure_date": "07/01/2024"})
        self.assertEqual("Write error", str(context.exception))

    @freeze_time("2024-01-07")
    def test_room_key_format_specificity_invalid(self):
        """ TC12: Room key is a valid MD5 hash but does not correspond to any booking in the system"""
        room_key = "valid_md5_no_booking"
        with mock.patch("os.path.exists", return_value=False):
            with self.assertRaises(HotelManagementException) as context:
                self.hotel_manager.guest_checkout(room_key)
        self.assertIn("Room key not found in processed stays store", str(context.exception))

    @freeze_time("2024-01-07")
    def test_departure_date_format_invalid(self):
        """ TC13: Departure date is incorrectly formatted"""
        room_key = "valid_md5_incorrect_date_format"
        with mock.patch("os.path.exists", return_value=True), \
                mock.patch("builtins.open", mock.mock_open(read_data='{"departure": "07-01-2024"}')):
            with self.assertRaises(HotelManagementException) as context:
                self.hotel_manager.guest_checkout(room_key)
        self.assertIn("Departure date is not valid.", str(context.exception))

    @freeze_time("2024-01-07")
    def test_guest_checkout_departure_date_in_past(self):
        """ TC14: Departure date is in the past"""
        room_key = "valid_md5_with_past_departure"
        with mock.patch("os.path.exists", return_value=True), \
                mock.patch("builtins.open", mock.mock_open(read_data='{"departure": "06/01/2024 00:00:00"}')):
            with self.assertRaises(HotelManagementException) as context:
                self.hotel_manager.guest_checkout(room_key)
        self.assertIn("Departure date is in past.", str(context.exception))