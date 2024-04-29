#!/bin/bash

# Declare an empty array for solved files
solved_files=()

# Iterate over changed files
for file in "$1"; do
    # Check for "_solved.py" files.
    if [[ $file == *_solved.py ]]; then
        # Add the path of the solved file to the array
        solved_files+=("$file")

        # Loop over the solved files array
        for ((i=0; i<${#solved_files[@]}; i++)); do
            # Get the name the current file.
            current_file="${solved_files[$i]}"
            echo "Solved file: ${current_file}"

            # Check if the current file is different from the previous file
            if [ "$current_file" != "$previous_file" ]; then
                # Extract the directory name
                current_dir="${current_file%/*}"
                echo "In the $current_dir directory"

                # Find the unsolved.py file and rename it to unsolved_tmp.py
                unsolved_file=$(find "$current_dir" -name "*_unsolved.py")
                if [ -f "$unsolved_file" ]; then
                    echo "Found unsolved file: $unsolved_file"
                    # Rename the unsolved.py file to unsolved_tmp.py.
                    mv "$unsolved_file" "${current_dir}/$(basename "$unsolved_file" _unsolved.py)_unsolved_tmp.py"
                    echo "Renamed unsolved.py to unsolved_tmp.py: ${current_dir}/$(basename "$unsolved_file" _unsolved.py)_unsolved_tmp.py"
                else
                    echo "Unsolved file not found."
                fi

                # Find the unsolved.py file and rename it to unsolved_tmp.py
                solved_file=$(find "$current_dir" -name "*_solved.py")
                if [ -f "$solved_file" ]; then
                    echo "Found solved file: $solved_file"
                    # Rename the solved.py file to unsolved.py.
                    mv "$solved_file" "${current_dir}/$(basename "$solved_file" _solved.py)_unsolved.py"
                    echo "Renamed solved.py to unsolved.py: ${current_dir}/$(basename "$solved_file" _solved.py)_unsolved.py"
                else
                    echo "Solved file not found."
                fi

                # Find the test file and execute it
                test_file=$(find "$current_dir" -name "*_tests.py")
                if [ -f "$test_file" ]; then
                    echo "Found test file: $test_file"
                    echo "Testing renamed solved.py to unsolved.py"
                    python -m unittest -v "$test_file"
                else
                    echo "Test file not found."
                fi

                # Update the previous file to the current file
                previous_file="$current_file"
            else
                echo "The file has already been processed"
            fi
        done
    fi
done
