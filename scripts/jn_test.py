"""
This Python script will run and test the Jupyter notebooks.
Make sure you have created the PythonData Conda environment as in the course.
Then add that Conda environment to the Jupyter kernel.
"""

import os
import sys
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor, CellExecutionError

def test_notebooks():
    """ This function sorts all the folders in the directory, then searches for all the .ipynb files
    in any subfolder, i.e., Solved, Unsolved, Resources, Images, etc, in the directory.
    Then, it runs the test on the .ipynb files using nbconvert."""
    # Iterate through the files in the folder.
    for file in os.listdir():
        if file.endswith(".ipynb"):
            with open(file, encoding="utf-8") as nb_file:
                read_nb = nbformat.read(nb_file, as_version=4)
                # Execute the Jupyter notebook with Python3 kernel.
                execute_nb = ExecutePreprocessor(timeout=600, kernel_name='python3')
                try:
                    output = execute_nb.preprocess(read_nb)
                    print(f"{file} passed.")
                except CellExecutionError as error:
                    output = None
                    print(f"There was an error executing {file}.")
                    print(error)
                    #  Terminate script upon encountering an error.
                    sys.exit(f"There was an error executing {file}: {error}")


test_notebooks()
