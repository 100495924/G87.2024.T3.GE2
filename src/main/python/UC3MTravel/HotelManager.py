import json
import os
from datetime import datetime
from src.main.python.UC3MTravel.HotelManagementException import HotelManagementException
from src.main.python.UC3MTravel.HotelReservation import HotelReservation


class HotelManager:
    def __init__(self):
        pass

    def roomReservation(self, credit_card: str, name_surname: str, id_card: str, phone_number: str, room_type: str,
                        arrival_date: str, num_days: int):
        """Function 1. Request a hotel reservation.
        Returns a valid MD5 string corresponding to the localizer and creates a json file with the reservation data"""

        # We validate all the parameters
        self.validateCreditCard(credit_card)
        self.validateNameSurname(name_surname)
        self.validateIdCard(id_card)
        self.validatePhoneNumber(phone_number)
        self.validateRoomType(room_type)
        self.validateArrivalDate(arrival_date)
        self.validateNumDays(num_days)

        # We create the json file with the reservation data that will be further processed in guestArrival (Function 2)

        # As there can only be 1 reservation per client, we use the value of the id_card to ensure the name of each
        # generated file is unique
        file_name = id_card + ".json"

        # This json file contains the attributes of the HotelReservation class, which are calculated using the
        # attributes of our current HotelManager class
        hr = HotelReservation(credit_card=credit_card,
                              name_surname=name_surname,
                              id_card=id_card,
                              phone_number=phone_number,
                              room_type=room_type,
                              arrival_date=arrival_date,
                              num_days=num_days)

        # The algorithm to obtain the localizer (a MD5 string) is applied and stored
        md5_localizer = hr.localizer

        # Data that will be written in the json file
        json_data = {"id_card": hr.id_card,
                     "name_surname": hr.name_surname,
                     "credit_card": hr.credit_card,
                     "phone_number": hr.phone_number,
                     "reservation_date": hr.reservation_date,
                     "arrival_date": hr.arrival_date,
                     "num_days": hr.num_days,
                     "room_type": hr.room_type,
                     "localizer": md5_localizer
                     }

        # We will create a json file named file_name in the reservations_store folder, and the content we have to write
        # on it is defined in json_data
        self.createJsonFile(file_name, "reservations_store", json_data)

        # We return the localizer
        return md5_localizer

    def validateCreditCard(self, credit_card: str):
        """Checks if the credit_card parameter of the roomReservation function is valid, else it raises the
        corresponding HotelManagementExceptions"""
        if not isinstance(credit_card, str):
            raise HotelManagementException("credit_card is not a string")

        if len(credit_card) != 16:
            raise HotelManagementException("credit_card is not 16 characters long")

        # This function checks if all the characters of credit_card are digits, else it returns a
        # HotelManagementException with the message that is passed as the second parameter
        self.isAllDigits(credit_card, "credit_card must have 16 digits")

        # Luhn's algorithm: checks if the last digit of the credit card number is valid

        # We separate the last digit (check_digit) from the rest (payload)
        # Operations are performed on the payload to figure out the unique valid last digit
        check_digit = credit_card[len(credit_card) - 1]
        payload = credit_card[:len(credit_card) - 1]
        sum_total = 0
        double = True

        # We iterate through each digit of the payload, starting from the last one
        for i in range(len(credit_card) - 2, -1, -1):
            # Digits in odd positions (1st iteration, 3rd, 5th...) are doubled
            if double:
                sum_digit = 2 * int(payload[i])
                # If we obtain a number equal or higher than 10, we take each of its digits and add them together
                # Example: 15 = 1 + 5 = 6
                if sum_digit >= 10:
                    sum_digit = 1 + sum_digit % 10
            # Digits in even positions are left as they are
            else:
                sum_digit = int(payload[i])
            # We add all the obtained digits together
            sum_total += sum_digit
            # If we doubled this digit, the next one should not be doubled and viceversa
            double = not double

        # We obtain the valid check digit with a final formula, and we compare it with the one of the input credit_card
        if int(check_digit) != (10 - (sum_total % 10)) % 10:
            raise HotelManagementException("credit_card does not follow the Luhn algorithm")

    def validateNameSurname(self, name_surname: str):
        """Checks if the name_surname parameter of the roomReservation function is valid, else it raises the
        corresponding HotelManagementExceptions"""
        if not isinstance(name_surname, str):
            raise HotelManagementException("name_surname is not a string")

        if not 10 <= len(name_surname) <= 50:
            raise HotelManagementException("name_surname must be between 10 and 50 characters long")

        # If there is a white space at the beginning or at the end of the string, that white space is not separating
        # 2 strings and thus denotes an invalid format
        if name_surname[0] == " " or name_surname[-1] == " ":
            raise HotelManagementException("name_surname must contain at least 2 strings separated by a white space")

        # True is there is at least 1 white space in the string
        # We need minimum 2 strings and 1 white space, which are different ways of expressing the same (having 1 white
        # space implies we have 2 strings)
        is_there_white_space = False
        # True if the character of an iteration is a white space
        # Will be used to check every pair of subsequent strings have a white space separating them and only 1
        current_white_space = False

        # We iterate through each character
        for character in name_surname:
            if character == " ":
                # If the character of the previous iteration was a white space and the current one too, that means
                # we have 2 subsequent white spaces, so the format is invalid
                if current_white_space:
                    raise HotelManagementException(
                        "name_surname must contain at least 2 strings separated by a white space")
                # We update the variable according to the new information of the current iteration
                current_white_space = True
                # We have found at least 1 white space
                is_there_white_space = True
            elif current_white_space:
                # We update the variable according to the new information of the current iteration
                current_white_space = False

        # If we have 0 white spaces, it is the same as saying we have less than 2 strings
        if not is_there_white_space:
            raise HotelManagementException(
                "name_surname must contain at least 2 strings separated by a white space")

    def validateIdCard(self, id_card: str):
        """Checks if the id_card parameter of the roomReservation function is valid, else it raises the
        corresponding HotelManagementExceptions"""
        if not isinstance(id_card, str):
            raise HotelManagementException("id_card is not a string")

        if len(id_card) != 9:
            raise HotelManagementException("id_card must have 8 digits and 1 final letter")

        # A valid id_card has 8 digits at the beginning and 1 final letter, so we separate them to analyze them
        digits = id_card[:8]
        letter = id_card[-1]

        # Checks that the 8 starting characters are actually 8 digits
        self.isAllDigits(digits, "id_card must have 8 digits and 1 final letter")

        # Letters are ordered in this way to apply in an easy way the algorithm of valid final letter
        letters_list = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H",
                        "L", "C", "K", "E"]

        # Checks that the final letter is actually a letter
        if letter not in letters_list:
            raise HotelManagementException("id_card must have 8 digits and 1 final letter")

        # The algorithm of the valid final letter consists in a modulo operation done on the 8-digit number, which
        # returns 23 possible values, and each of them is associated to a letter (an index of letters_list)
        # We compare if the valid letter coincides with the input letter
        if letter != letters_list[int(digits) % 23]:
            raise HotelManagementException("invalid letter for id_card")

        # Now we need to check if the client that is doing the reservation already has a reservation
        # Each client is univocally identified by his/her id_card, and the name of every json file corresponds to
        # the id_card of the client who made the reservation, so we need to check that there is no json file stored in
        # the reservations_store directory whose name is the input id_card

        # We get the reservations_store directory (absolute path)
        directory = self.getJsonDirectory("reservations_store")

        # We iterate through each of the json files stored in that directory
        for file_name in os.listdir(directory):
            # The name of the json files corresponds to the id_card of the client who made the reservation
            if id_card in file_name:
                raise HotelManagementException("a client with specified id_card already has a reservation")

    def validatePhoneNumber(self, phone_number: str):
        """Checks if the phone_number parameter of the roomReservation function is valid, else it raises the
        corresponding HotelManagementExceptions"""
        if not isinstance(phone_number, str):
            raise HotelManagementException("phone_number is not a string")

        if len(phone_number) != 9:
            raise HotelManagementException("phone_number is not 9 characters long")

        self.isAllDigits(phone_number, "phone_number must have 9 digits")

    def validateRoomType(self, room_type: str):
        """Checks if the room_type parameter of the roomReservation function is valid, else it raises the
        corresponding HotelManagementExceptions"""
        if not isinstance(room_type, str):
            raise HotelManagementException("room_type is not a string")

        # room_type only accepts one of these 3 values
        if room_type not in ["single", "double", "suite"]:
            raise HotelManagementException("invalid room_type value")

    def validateArrivalDate(self, arrival_date: str):
        """Checks if the arrival_date parameter of the roomReservation function is valid, else it raises the
        corresponding HotelManagementExceptions"""
        if not isinstance(arrival_date, str):
            raise HotelManagementException("arrival_date is not a string")

        if len(arrival_date) != 10:
            raise HotelManagementException("invalid arrival_date format \"DD/MM/YYYY\"")

        # We separate each of the different parts of the date format to analyze them
        day_string = arrival_date[:2]
        first_slash = arrival_date[2]
        month_string = arrival_date[3:5]
        second_slash = arrival_date[5]
        year_string = arrival_date[6:]

        # We have this basic pattern: 2 digits - slash - 2 digits - slash - 4 digits
        if first_slash != "/" or second_slash != "/":
            raise HotelManagementException("invalid arrival_date format \"DD/MM/YYYY\"")
        self.isAllDigits(day_string, "invalid arrival_date format \"DD/MM/YYYY\"")
        self.isAllDigits(month_string, "invalid arrival_date format \"DD/MM/YYYY\"")
        self.isAllDigits(year_string, "invalid arrival_date format \"DD/MM/YYYY\"")

        # We now have to check if the date represented in the string actually corresponds to a date that exists in real
        # life. We will need to make numeric operations and comparisons on these fields, so we transform them from
        # string to int
        day = int(day_string)
        month = int(month_string)
        year = int(year_string)

        # We have 12 months in the calendar
        if not 1 <= month <= 12:
            raise HotelManagementException("arrival_date does not exist")

        # Depending on the month of the year, and if we have a leap-year or not, the range of valid day values varies
        # In this ordered list, we associate each index with a month and its maximum number of days
        # (0 = January, 1 = February, 2 = March...)
        days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # Algorithm to calculate whether a year is a leap-year (if February has a maximum of 29 days instead of 28)
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            days_list[1] = 29

        # A day of a given valid month cannot be bigger than its associated maximum number of days
        if day > days_list[month - 1]:
            raise HotelManagementException("arrival_date does not exist")

        # We have checked that the date exists. Now we need to figure out if it makes sense to make a reservation in
        # that date. We allow our clients to make a reservation for the same day or for any posterior days

        # Algorithm to throw an exception if a client is trying to make a reservation for a date in the past, given
        # our defined current date
        current_date = datetime.now()
        if year < current_date.year:
            raise HotelManagementException("arrival_date before current date")
        if year == current_date.year and month < current_date.month:
            raise HotelManagementException("arrival_date before current date")
        if year == current_date.year and month == current_date.month and day < current_date.day:
            raise HotelManagementException("arrival_date before current date")

    def validateNumDays(self, num_days: int):
        """Checks if the num_days parameter of the roomReservation function is valid, else it raises the
        corresponding HotelManagementExceptions"""
        if not isinstance(num_days, int):
            raise HotelManagementException("num_days is not an int")

        if not 1 <= num_days <= 10:
            raise HotelManagementException("num_days must be between 1 and 10")

    def isAllDigits(self, digit_string: str, exception_message: str):
        """Check if all the characters of a given string are digits, else a HotelManagementException is raised with a
        given message"""
        digits_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        for character in digit_string:
            if character not in digits_list:
                raise HotelManagementException(exception_message)

    def getJsonDirectory(self, folder_name: str):
        """Returns the desired directory in which generated json files are stored"""
        # We need to obtain the common parent directory of all the files of our project, so that the function can be
        # called in any file and still return the same result
        # We also have to take into account that this is a collaborative project, so we cannot simply put a specific
        # absolute path, but an absolute path relative to our particular computer. The place where the project directory
        # lies

        # Absolute path of the current directory
        current_directory = os.getcwd()
        # We get the index of the string in which the name of our project begins
        index = current_directory.index("G87.2024.T3.GE2")
        # We obtain the parent directory that is common to all the project's files of our specific computer
        project_directory = current_directory[:index]
        # We navigate down the directory to reach the json_file directory
        json_directory = os.path.join(project_directory,
                                      "G87.2024.T3.GE2", "src", "main", "python", "UC3MTravel", folder_name)
        return json_directory

    def createJsonFile(self, file_name: str, folder_name: str, json_data: dict):
        """Creates a json file named file_name in the folder folder_name and writes on it json_data"""
        # First, we need to get the absolute path of the directory where we want to store the json file
        json_directory = self.getJsonDirectory(folder_name)

        # We save the current directory, so we can restore it later
        original_directory = os.getcwd()

        # We change the current directory to the directory where the json file will be stored to be able to save it
        # there
        os.chdir(json_directory)

        # We open the file for writing (it is created if it does not exist) and we write the data
        with open(file_name, "w", encoding="utf-8") as open_file:
            open_file.write(json.dumps(json_data, indent=4))

        # We need to delete the created file if it was created for testing purposes
        if "unittest" in original_directory:
            os.remove(file_name)

        # We restore the original current directory
        os.chdir(original_directory)

    def readDataFromJson(self, file_path: str):
        """Reads a given json file and returns the value of its IdCard key"""
        # Tries to open the file for reading and storing its content in a variable, and throws an exception if an error
        # occurs during the process
        try:
            with open(file_path, "r", encoding="utf-8") as open_file:
                data = json.load(open_file)
        except FileNotFoundError as ex:
            raise HotelManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from ex

        # We get the value of the IdCard key
        try:
            json_id_card = data["IdCard"]
        except KeyError as ex:
            raise HotelManagementException("JSON Decode Error - Invalid JSON Key") from ex

        # Close the file and return the value
        return json_id_card
