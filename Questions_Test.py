# imports
import unittest

from Questions import *


# classes

class MyTestCase(unittest.TestCase):

    # functions

    def test_validate_input(self):
        """
        Tests for the function validate_input in the script Questions.py

        :return: N/A
        """
        self.assertEqual(Question.validate_input("1"), 1)
        # Lower Bound OK -

        self.assertEqual(Question.validate_input("2"), 2)
        # Middle OK -

        self.assertEqual(Question.validate_input("4"), 4)
        # Upper Bound OK -

        self.assertRaises(ValueError, Question.validate_input, "four")
        # Length Not Integer -

        self.assertRaises(ValueError, Question.validate_input, "0")
        # Length Too Short -

        self.assertRaises(ValueError, Question.validate_input, "5")
        # Length Too Long -

    def test_mark_questions(self):
        """
        Tests for the function mark_questions in the script Questions.py

        :return:
        """

        # Short Quiz - No Questions Right -

        # Short Quiz - Half Questions Right -

        # Short Quiz - All Questions Right -

        # Long Quiz - No Questions Right -

        # Long Quiz - Half Questions Right -

        # Long Quiz - All Questions Right -



# main
if __name__ == "__main__":
    question = Question()
    unittest.main(verbosity=2)
