# Import pyunit module.
import unittest

# Import the code you want to test.
# REMOVE THIS IMPORT IF YOU ARE TESTING INPUT THAT'S NEITHER IN A MAIN BLOCK OR A FUNCTION.
import return_unsolved

# Necessary for testing code with printed output or user input inside a function.
from unittest.mock import patch

# Necessary for testing code with printed output inside a function.
from io import StringIO

# Necessary for testing code with printed output or user input outside of a function.
from subprocess import Popen, PIPE
import pathlib

class TestCode(unittest.TestCase):
    # Test that the convert_minutes_to_hours function runs without error when given the minutes.
    def test_function_runs(self):
        return_unsolved.convert_minutes_to_hours(10)

    # Test that the minutes are a floating point number.
    def test_minutes_is_float(self):
        self.assertIsInstance(return_unsolved.convert_minutes_to_hours(10), float)

    # Test that the minutes are converted to hours
    def test_minutes_converted_to_hours(self):
        self.assertEqual(return_unsolved.convert_minutes_to_hours(60), 1.0)

    # For the input of 6 minutes, test that output is “6.00 minutes is equal to 0.10 hours”.
    def test_input_output_outside_function_template(self):
        prompt = "Enter the time duration in minutes: "
        expected_value = prompt + "6.00 minutes is equal to 0.10 hours.\n"
        inputs = ["6"]
        # Use Popen to run the code as a separate process.
        code_path = pathlib.Path(__file__).parent.resolve() # Use this line for testing on your local machine.
        # code_path = "../home/"  # Use this line for testing on EdSTEM.
        p = Popen([f'python \"{code_path}/return_unsolved.py\"'], shell=True,
                  stdout=PIPE, stderr=PIPE, stdin=PIPE)

        # Give the inputs and get the program's output.
        byte_input = bytes("\n".join(inputs).encode())
        byte_output, err = p.communicate(input=byte_input)

        # Fail the test if the program raised an exception.
        if err:
            raise Exception(f"Error: {err}")

        # Test the program's output.
        output = byte_output.decode()
        self.assertEqual(output, expected_value)



if __name__ == "__main__":
    unittest.main()
