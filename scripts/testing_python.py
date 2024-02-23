"""
This Python script will run and test all the Python files in any folder in a given directory.
"""

import os
import subprocess
import sys

def run_python_files(files):
    """This function takes a list of Python file paths and runs them."""
    for file_path in files:
        try:
            # Run the Python file using subprocess
            subprocess.run(['python', file_path], check=True)
        except subprocess.CalledProcessError as e:
            sys.exit(f"There was an error executing {file_path}: {e}")

def main():
    """ Retrieves the list of file paths from the environment variable 'INPUT_FILES'
    and runs each Python file in the list."""

    # Check if environment variable 'INPUT_FILES' exists
    if 'INPUT_FILES' not in os.environ:
        sys.exit("Error: Environment variable 'INPUT_FILES' is not set.")

    # Get the list of file paths from the environment variable
    input_variable = os.environ['INPUT_FILES'].split()

    # Run Python files
    run_python_files(input_variable)

if __name__ == "__main__":
    main()
