# task_1
import unittest  # import module unittest
from homework_help import *  # import all objects from another file


class TestFunctions(unittest.TestCase):

    def test_full_name(self):  # use the assertEqual method to test that the result of the full_name() function
        # matches the expected output
        self.assertEqual(full_name("john", "doe"), "John Doe")
        self.assertEqual(full_name("JANE", "SMITH"), "Jane Smith")
        self.assertEqual(full_name("aLice", "wOnDerLanD"), "Alice Wonderland")

    def test_squares(self):  # use the assertEqual method to test that the result of the squares() function matches
        # the expected output
        self.assertEqual(squares([1, 2, 3]), [1, 4, 9])
        self.assertEqual(squares([-1, 0, 1]), [1, 0, 1])
        self.assertEqual(squares([2.5, 3.5, 4.5]), [6.25, 12.25, 20.25])
        self.assertEqual(squares([]), [])
        self.assertEqual(squares([0]), [0])


if __name__ == '__main__':
    unittest.main()

# надіюсь, що правильно зрозумів завдання. Стосовно task_2 -- не впевнений як саме робити перевірку того чи записується
# щось у json. Трішки кидав оком, але виглядає щось надто страшно та не дуже зрозуміло. Поки залишив лише task_1.
