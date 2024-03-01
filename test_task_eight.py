from unittest import TestCase
import task_eight


class Test(TestCase):
    def test_collect_input(self):
        expected_result = "18,22,24"
        self.assertEqual(expected_result,task_eight.collect_input(100,150,180))

