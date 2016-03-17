import unittest
from race_average import RaceAverage


class Test(unittest.TestCase):

    def test_outputs_as_expected(self):
        minutes = RaceAverage.average(["12:00 PM, DAY 1", "12:01 PM, DAY 1"])

        self.assertEqual(minutes, 241)

        minutes = RaceAverage.average(["12:00 AM, DAY 2"])

        self.assertEqual(minutes, 960)

        minutes = RaceAverage.average(["02:00 PM, DAY 19", "02:00 PM, DAY 20", "01:58 PM, DAY 20"])

        self.assertEqual(minutes, 27239)

        minutes = RaceAverage.average(["12:00 AM, DAY 99"])

        self.assertEqual(minutes, 140640)

    def test_rounds_up(self):
        minutes = RaceAverage.average(["08:01 AM, DAY 1", "08:02 AM, DAY 1"])

        self.assertEqual(minutes, 2)

    def test_rounds_down(self):
        minutes = RaceAverage.average(["08:01 AM, DAY 1", "08:01 AM, DAY 1", "08:02 AM, DAY 1"])

        self.assertEqual(minutes, 1)

    def test_early_start(self):
        with self.assertRaises(ValueError):
            RaceAverage.average(["07:59 AM, DAY 1"])

        with self.assertRaises(ValueError):
            RaceAverage.average(["06:00 AM, DAY 1"])

    def test_invalid_format(self):
        with self.assertRaises(ValueError):
            RaceAverage.average(["00:00 AM, DAY 1"])

        with self.assertRaises(ValueError):
            RaceAverage.average(["12:60 AM, DAY 1"])

        with self.assertRaises(ValueError):
            RaceAverage.average(["12:00 KM, DAY 1"])

        with self.assertRaises(ValueError):
            RaceAverage.average(["12:00 AM, DAY 100"])

        with self.assertRaises(ValueError):
            RaceAverage.average(["12:00 AM, DAY 0"])

        with self.assertRaises(ValueError):
            RaceAverage.average(["FOO"])

    def test_invalid_wrong_type(self):
        with self.assertRaises(TypeError):
            RaceAverage.average("foo")

        with self.assertRaises(TypeError):
            RaceAverage.average(123)

        with self.assertRaises(TypeError):
            RaceAverage.average(dict())

        with self.assertRaises(TypeError):
            RaceAverage.average(set())

    def test_invalid_list_size(self):
        with self.assertRaises(ValueError):
            RaceAverage.average([])

        with self.assertRaises(ValueError):
            RaceAverage.average(['12:00 AM, DAY 1' for x in range(51)])

if __name__ == '__main__':
    unittest.main(exit=False)
