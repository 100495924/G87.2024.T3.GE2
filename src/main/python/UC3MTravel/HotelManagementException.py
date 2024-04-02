""" HotelManagementException module"""
class HotelManagementException(Exception):
    """ HotelManagementException class"""
    def __init__(self, message):
        self.__message = message
        super().__init__(self.message)

    @property
    def message(self):
        """ Property representing the message of the exception."""
        return self.__message

    @message.setter
    def message(self, value):
        """ Setter for the message."""
        self.__message = value
