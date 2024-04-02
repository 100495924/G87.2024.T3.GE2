""" Module that tests the guestArrival() function"""
import os.path
from unittest import TestCase
from datetime import datetime
from freezegun import freeze_time
from UC3MTravel.HotelManager import HotelManager
from UC3MTravel.HotelManagementException import HotelManagementException


class TestGuestArrival(TestCase):
    """Test cases for guestArrival (Function 2)"""

    def setUp(self):
        self.my_hotel_manager = HotelManager()

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival01(self):
        """ TC1: Valid case that covers all the nodes"""
        file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test1.json")
        room_value = self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(room_value, "9f75f184df311e0c5ab5595ab4f66ec6021eda13b1c2db1ab5e337cb7992b832")

        json_dir = self.my_hotel_manager.getJsonDirectory("processed_stays_store")
        filename = room_value + ".json"
        processed_json_path = os.path.join(json_dir, filename)
        json_output = self.my_hotel_manager.readDataFromProcessedStayJson(processed_json_path)
        self.assertEqual(json_output[0], "SHA-256")
        self.assertEqual(json_output[1], "single")
        self.assertEqual(json_output[2], "00000000T")
        self.assertEqual(json_output[3], "cdaeb5334e828615221afb3f4aed4607")
        self.assertEqual(json_output[4], 1719792000.0)
        self.assertEqual(json_output[5], 1719878400.0)
        self.assertEqual(json_output[6], "9f75f184df311e0c5ab5595ab4f66ec6021eda13b1c2db1ab5e337cb7992b832")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival02(self):
        """ TC2: Duplicating Non-terminal node 1 """
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test2.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival03(self):
        """ TC3: Duplicating Non-terminal node 2 (Affects also node 5) """
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test3.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival04(self):
        """ TC4: Duplicating Non-terminal node 3"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test4.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival05(self):
        """ TC5: Duplicating Non-terminal node 4 (Affects also node 9)"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test5.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival06(self):
        """ TC6: Duplicating Non-terminal node 6"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test6.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival07(self):
        """ TC7: Duplicating Non-terminal node 7 (Affects also node 13)"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test7.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival08(self):
        """ TC8: Duplicating Non-terminal node 8"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test8.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival09(self):
        """ TC9: Duplicating Non-terminal node 10"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test9.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival10(self):
        """ TC10: Duplicating Non-terminal node 11 (Affects also node 20)"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test10.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival11(self):
        """ TC11: Duplicating Non-terminal node 12"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test11.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival12(self):
        """ TC12: Duplicating Non-terminal node 14"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test12.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival13(self):
        """ TC13: Duplicating Non-terminal node 15 (Affects also node 27)"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test13.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival14(self):
        """ TC14: Duplicating Non-terminal node 16"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test14.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival15(self):
        """ TC15: Duplicating Non-terminal node 17 (Affects also node 31)"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test15.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival16(self):
        """ TC16: Duplicating Non-terminal node 18 (Affects also node 32)"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test16.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival17(self):
        """ TC17: Duplicating Non-terminal node 19 (Affects also node 33)"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test17.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival18(self):
        """ TC18: Duplicating Non-terminal node 21 (Affects also node 34)"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test18.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival19(self):
        """ TC19: Duplicating Non-terminal node 22 (Affects also node 35)"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test19.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON data does not have valid values.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival20(self):
        """ TC20: Duplicating Non-terminal node 23 (Affects also node 36)"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test20.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival21(self):
        """ TC21: Duplicating Non-terminal node 24 (Affects also node 37)"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test21.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival22(self):
        """ TC22: Duplicating Non-terminal node 25 (Affects also node 38)"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test22.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival23(self):
        """ TC23: Duplicating Non-terminal node 26 (Affects also node 39)"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test23.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival24(self):
        """ TC24: Duplicating Non-terminal node 28 (Affects also node 40)"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test24.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival25(self):
        """ TC25: Duplicating Non-terminal node 29 (Affects also node 41)"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test25.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON data does not have valid values.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival26(self):
        """ TC26: Duplicating Non-terminal node 30 (Affects also node 42)"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test26.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival27(self):
        """ TC27: Deleting Non-terminal node 1"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test27.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival28(self):
        """ TC28: Deleting Non-terminal node 2 (Affects also node 5)"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test28.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival29(self):
        """ TC29: Deleting Non-terminal node 3"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test29.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival30(self):
        """ TC30: Deleting Non-terminal node 4 (Affects also node 9)"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test30.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival31(self):
        """ TC31: Deleting Non-terminal node 6"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test31.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival32(self):
        """ TC32: Deleting Non-terminal node 7 (Affects also node 13)"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test32.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival33(self):
        """ TC33: Deleting Non-terminal node 8"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test33.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival34(self):
        """ TC34: Deleting Non-terminal node 10"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test34.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival35(self):
        """ TC35: Deleting Non-terminal node 11 (Affects also node 20)"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test35.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival36(self):
        """ TC36: Deleting Non-terminal node 12"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test36.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival37(self):
        """ TC37: Deleting Non-terminal node 14"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test37.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival38(self):
        """ TC38: Deleting Non-terminal node 15 (Affects also node 27)"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test38.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival39(self):
        """ TC39: Deleting Non-terminal node 16"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test39.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival40(self):
        """ TC40: Deleting Non-terminal node 17 (Affects also node 31)"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test40.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival41(self):
        """ TC41: Deleting Non-terminal node 18 (Affects also node 32)"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test41.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival42(self):
        """ TC42: Deleting Non-terminal node 19 (Affects also node 33)"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test42.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival43(self):
        """ TC43: Deleting Non-terminal node 21 (Affects also node 34)"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test43.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival44(self):
        """ TC44: Deleting Non-terminal node 22 (Affects also node 35)"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test44.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON data does not have valid values.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival45(self):
        """ TC45: Deleting Non-terminal node 23 (Affects also node 36)"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test45.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival46(self):
        """ TC46: Deleting Non-terminal node 24 (Affects also node 37)"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test46.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival47(self):
        """ TC47: Deleting Non-terminal node 25 (Affects also node 38)"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test47.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival48(self):
        """ TC48: Deleting Non-terminal node 26 (Affects also node 39)"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test48.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival49(self):
        """ TC49: Deleting Non-terminal node 28 (Affects also node 40)"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test49.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival50(self):
        """ TC50: Deleting Non-terminal node 29 (Affects also node 41)"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test50.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON data does not have valid values.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival51(self):
        """ TC51: Deleting Non-terminal node 30 (Affects also node 42)"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test51.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival52(self):
        """ TC52: Modifying Terminal node 5"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test52.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival53(self):
        """ TC53: Modifying Terminal node 9"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test53.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival54(self):
        """ TC54: Modifying Terminal node 13"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test54.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival55(self):
        """ TC55: Modifying Terminal node 20"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test55.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival56(self):
        """ TC56: Modifying Terminal node 27"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test56.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival57(self):
        """ TC57: Modifying Terminal node 31"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test57.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival58(self):
        """ TC58: Modifying Terminal node 32"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test58.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival59(self):
        """ TC59: Modifying Terminal node 33"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test59.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival60(self):
        """ TC60: Modifying Terminal node 34"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test60.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival61(self):
        """ TC61: Modifying Terminal node 36"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test61.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival62(self):
        """ TC62: Modifying Terminal node 37"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test62.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival63(self):
        """ TC63: Modifying Terminal node 38"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test63.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival64(self):
        """ TC64: Modifying Terminal node 39"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test64.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival65(self):
        """ TC65: Modifying Terminal node 40"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test65.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    @freeze_time(datetime.strptime("01/07/2024", "%d/%m/%Y"))
    def testGuestArrival66(self):
        """ TC66: Modifying Terminal node 42"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test66.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON does not have the expected structure.")

    def testGuestArrival67(self):
        """ TC67: Empty file path"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = ""
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The file is not in JSON format")

    def testGuestArrival68(self):
        """ TC68: Localizer is not an hexadecimal value"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test68.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON data does not have valid values.")

    def testGuestArrival69(self):
        """ TC69: The length of localizer is 31 (1 character less than in the valid case)"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test69.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON data does not have valid values.")

    def testGuestArrival70(self):
        """ TC70: The length of localizer is 33 (1 character more than in the valid case)"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test70.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON data does not have valid values.")

    def testGuestArrival71(self):
        """ TC71: IdCard does not have a valid ID value."""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test71.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "Wrong file or file path")

    def testGuestArrival72(self):
        """ TC72: The length of idCard is 8 (1 character less than in the valid case)"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test72.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON data does not have valid values.")

    def testGuestArrival73(self):
        """ TC73: The length of idCard is 10 (1 character more than in the valid case)"""
        with self.assertRaises(HotelManagementException) as ex:
            file_path = os.path.join("guestArrival_tests_JSON", "guestArrival_test73.json")
            self.my_hotel_manager.guestArrival(file_path)
        self.assertEqual(ex.exception.message, "The JSON data does not have valid values.")
