from unittest import TestCase
import seven_segment_display_python


class Test(TestCase):
    def test_that_when_I_when_the_length_of_input_is_not8_throw_exception(self):
        with self.assertRaises(ValueError):
            seven_segment_display_python.display_seven_segment_of("111111111")

    def test_that_when_any_char_in_the_input_is_not_binary_exception_is_thrown(self):
        with self.assertRaises(ValueError):
            seven_segment_display_python.display_seven_segment_of("11111311")

    def test_that_when_input_has_alphabet_error_is_thrown(self):
        with self.assertRaises(ValueError):
            seven_segment_display_python.display_seven_segment_of("11c11a11")
