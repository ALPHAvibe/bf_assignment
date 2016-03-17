import unittest
from text_blocking import TextBlocking


class Test(unittest.TestCase):

    def test_outputs_as_expected(self):
        output = TextBlocking.execute(["AAA", "BBB", "CCC"])

        self.assertEqual(len(output), 3)
        self.assertTrue(all('ABC' == line for line in output))

        output = TextBlocking.execute(["AAAAAAAAAAAAA"])

        self.assertEqual(len(output), 13)
        self.assertTrue(all('A' == line for line in output))

        output = TextBlocking.execute(["A", "A", "A", "A",  "A"])

        self.assertEqual(len(output), 1)
        self.assertTrue(output[0] == "AAAAA")

    def test_invalid_line_format(self):
        with self.assertRaises(ValueError):
            TextBlocking.execute(["123", "BBB", "CCC"])

        with self.assertRaises(ValueError):
            TextBlocking.execute(["AAA", "(*&", "CCC"])

    def test_invalid_mis_match_length(self):
        with self.assertRaises(ValueError):
            TextBlocking.execute(["AAA", "BBBB"])

        with self.assertRaises(ValueError):
            TextBlocking.execute(["AAAAAAAAA", "BBB"])

    def test_invalid_wrong_type(self):
        with self.assertRaises(TypeError):
            TextBlocking.execute("foo")

        with self.assertRaises(TypeError):
            TextBlocking.execute(123)

        with self.assertRaises(TypeError):
            TextBlocking.execute(dict())

        with self.assertRaises(TypeError):
            TextBlocking.execute(set())

    def test_invalid_list_size(self):
        with self.assertRaises(ValueError):
            TextBlocking.execute([])

        with self.assertRaises(ValueError):
            TextBlocking.execute((['ABC' for x in range(51)]))

if __name__ == '__main__':
    unittest.main(exit=False)
