from unittest import TestCase
from class_with_two_method import StringMethods


class TestMethods(TestCase):
    def test_string(self):
        string = StringMethods()
        string.get_string("philip")
        self.assertEqual("PHILIP", string.print_string())
