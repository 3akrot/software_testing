# user_validation.py

import re
from datetime import datetime

class UserValidation:
    """
    A class for validating user input such as email, username,
    Egyptian phone number, and Egyptian national ID.
    """

    @staticmethod
    def validate_email(email: str) -> bool:
        """
        Validates if the provided email is in a proper format.
        Checks for the presence of '@', a domain, and a valid TLD.
        """
        if not isinstance(email, str):
            return False
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    @staticmethod
    def validate_username(username: str) -> bool:
        """
        Validates username (3-20 chars, letters/numbers/underscore only).
        """
        if not isinstance(username, str):
            return False
        # Regex for username: alphanumeric and underscore, 3-20 characters
        pattern = r'^[a-zA-Z0-9_]{3,20}$'
        return re.match(pattern, username) is not None

    @staticmethod
    def validate_phone_number(phone: str) -> bool:
        """
        Validates Egyptian phone number.
        - Starts with 010, 011, 012, 015 (11 digits total)
        - Or starts with 2010, 2011, 2012, 2015 (12 digits total)
        """
        if not isinstance(phone, str):
            return False
        pattern = r'^(01[0125]\d{8}|201[0125]\d{8})$'
        return re.match(pattern, phone) is not None

    @staticmethod
    def validate_national_id(national_id: str) -> bool:
        """
        Validates Egyptian national ID (14 digits with valid date and governorate code).
        """
        if not isinstance(national_id, str) or not national_id.isdigit() or len(national_id) != 14:
            return False

        century_digit = national_id[0]
        if century_digit not in ['2', '3']:
            return False

        year_str = national_id[1:3]
        month_str = national_id[3:5]
        day_str = national_id[5:7]
        
        year = (1900 if century_digit == '2' else 2000) + int(year_str)
        month = int(month_str)
        day = int(day_str)

        try:
            datetime(year, month, day)
        except ValueError:
            return False 

        governorate_code = int(national_id[7:9])
        valid_governorates = [
            1, 2, 3, 4, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 
            25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 88
        ]

        if not (1 <= governorate_code <= 35 or governorate_code == 88):
             return False


        return True