from unittest import TestCase
import rider_wages_calculator


class Test(TestCase):
    def test_when_rider_delivery_is_less_than_50_number_of_delivery_is_multiplied_by_160(self):
        expectedWages = rider_wages_calculator.calculate_rider_wages(25)
        self.assertEqual(expectedWages, 9_000)

    def test_when_rider_delivery_is_at_theRange_of_50_59_number_of_delivery_is_multiplied_by_160(self):
        expectedWages = rider_wages_calculator.calculate_rider_wages(57)
        self.assertEqual(expectedWages, 16_400)

    def test_when_rider_delivery_is_at_theRange_of_60_69_number_of_delivery_is_multiplied_by_160(self):
        expectedWages = rider_wages_calculator.calculate_rider_wages(69)
        self.assertEqual(expectedWages, 22_250)

    def test_when_rider_delivery_is_greater_than_or_equal_to_70_number_of_delivery_is_multiplied_by_160(self):
        expectedWages = rider_wages_calculator.calculate_rider_wages(80)
        self.assertEqual(expectedWages, 45_000)

    def test_when_rider_delivery_number_is_invalid_number_exception_isThrown(self):
        with self.assertRaises(ValueError):
            rider_wages_calculator.calculate_rider_wages(-1)

    def test_when_no_delivery_is_made_the_rider_collect_base_pay_only(self):
        expectedWages = rider_wages_calculator.calculate_rider_wages(0)
        self.assertEqual(5_000, expectedWages)