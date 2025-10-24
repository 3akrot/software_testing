# test_user_validation.py

import unittest
from main import UserValidation

class TestUserValidation(unittest.TestCase):

    # --- Test Cases for validate_email ---

    def test_validate_email_valid_format_returns_true(self):
        self.assertTrue(UserValidation.validate_email("user@example.com"))

    def test_validate_email_missing_at_symbol_returns_false(self):
        self.assertFalse(UserValidation.validate_email("userexample.com"))

    def test_validate_email_missing_domain_returns_false(self):
        self.assertFalse(UserValidation.validate_email("user@"))

    def test_validate_email_invalid_tld_returns_false(self):
        self.assertFalse(UserValidation.validate_email("user@mail.c"))

    def test_validate_email_with_subdomain_returns_true(self):
        self.assertTrue(UserValidation.validate_email("user@mail.company.com"))

    def test_validate_email_with_special_chars_returns_true(self):
        self.assertTrue(UserValidation.validate_email("ramy.gomaa21@mail.co"))

    def test_validate_email_uppercase_is_valid_returns_true(self):
        self.assertTrue(UserValidation.validate_email("USER@MAIL.COM"))

    def test_validate_email_with_space_returns_false(self):
        self.assertFalse(UserValidation.validate_email("user name@mail.com"))

    def test_validate_email_empty_string_returns_false(self):
        self.assertFalse(UserValidation.validate_email(""))

    def test_validate_email_none_input_returns_false(self):
        self.assertFalse(UserValidation.validate_email(None))

    # --- Test Cases for validate_username ---

    def test_validate_username_valid_returns_true(self):
        self.assertTrue(UserValidation.validate_username("ramy_gomaa"))

    def test_validate_username_too_short_returns_false(self):
        self.assertFalse(UserValidation.validate_username("ab"))

    def test_validate_username_too_long_returns_false(self):
        self.assertFalse(UserValidation.validate_username("ramygomaaisaverylongusername"))

    def test_validate_username_with_spaces_returns_false(self):
        self.assertFalse(UserValidation.validate_username("ramy gomaa"))

    def test_validate_username_with_symbols_returns_false(self):
        self.assertFalse(UserValidation.validate_username("ramy@123"))

    def test_validate_username_with_digits_returns_true(self):
        self.assertTrue(UserValidation.validate_username("ramy123"))

    def test_validate_username_empty_string_returns_false(self):
        self.assertFalse(UserValidation.validate_username(""))

    def test_validate_username_none_input_returns_false(self):
        self.assertFalse(UserValidation.validate_username(None))

    # --- Test Cases for validate_phone_number ---

    def test_validate_phone_valid_vodafone_returns_true(self):
        self.assertTrue(UserValidation.validate_phone_number("01012345678"))

    def test_validate_phone_valid_orange_returns_true(self):
        self.assertTrue(UserValidation.validate_phone_number("01234567890"))

    def test_validate_phone_valid_etisalat_returns_true(self):
        self.assertTrue(UserValidation.validate_phone_number("01198765432"))

    def test_validate_phone_valid_we_returns_true(self):
        self.assertTrue(UserValidation.validate_phone_number("01555555555"))

    def test_validate_phone_valid_vodafone_with_cc_returns_true(self):
        self.assertTrue(UserValidation.validate_phone_number("201012345678"))

    def test_validate_phone_valid_orange_with_cc_returns_true(self):
        self.assertTrue(UserValidation.validate_phone_number("201234567890"))
        
    def test_validate_phone_invalid_prefix_returns_false(self):
        self.assertFalse(UserValidation.validate_phone_number("01812345678"))

    def test_validate_phone_too_short_returns_false(self):
        self.assertFalse(UserValidation.validate_phone_number("0101234567"))

    def test_validate_phone_too_long_returns_false(self):
        self.assertFalse(UserValidation.validate_phone_number("010123456789"))

    def test_validate_phone_contains_chars_returns_false(self):
        self.assertFalse(UserValidation.validate_phone_number("01012abc678"))

    def test_validate_phone_empty_string_returns_false(self):
        self.assertFalse(UserValidation.validate_phone_number(""))

    def test_validate_phone_none_input_returns_false(self):
        self.assertFalse(UserValidation.validate_phone_number(None))

    # --- Test Cases for validate_national_id ---

    def test_validate_national_id_valid_returns_true(self):
        self.assertTrue(UserValidation.validate_national_id("29812251201234"))

    def test_validate_national_id_too_short_returns_false(self):
        self.assertFalse(UserValidation.validate_national_id("2981225123456"))

    def test_validate_national_id_too_long_returns_false(self):
        self.assertFalse(UserValidation.validate_national_id("298122512345678"))

    def test_validate_national_id_contains_letters_returns_false(self):
        self.assertFalse(UserValidation.validate_national_id("2981225AB34567"))

    def test_validate_national_id_invalid_century_code_returns_false(self):
        self.assertFalse(UserValidation.validate_national_id("19812251234567"))

    def test_validate_national_id_invalid_month_returns_false(self):
        self.assertFalse(UserValidation.validate_national_id("29813251234567"))

    def test_validate_national_id_invalid_day_returns_false(self):
        self.assertFalse(UserValidation.validate_national_id("29812321234567"))
        
    def test_validate_national_id_invalid_governorate_code_returns_false(self):
        # Using a governorate code '99' which is outside the valid range 01-88
        self.assertFalse(UserValidation.validate_national_id("29812259912345"))

    def test_validate_national_id_empty_string_returns_false(self):
        self.assertFalse(UserValidation.validate_national_id(""))

    def test_validate_national_id_none_input_returns_false(self):
        self.assertFalse(UserValidation.validate_national_id(None))


if __name__ == '__main__':
    unittest.main()