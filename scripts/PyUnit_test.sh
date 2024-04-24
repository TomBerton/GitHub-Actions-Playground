#!/bin/bash

# Iterate over changed files
for file in $1; do
    # Check for Jupyter notebooks solution files.
    if [[ $file == */solved.py ]]; then
        # Add the path of the solved file to the array
        solved_files+=("$file")
        for ((i=0;i<${#solved_files[@]};i++)); do
        # Get the name the current file.
        current_file="${solved_files[$i]}"
        echo "Solved file: ${current_file}"
            if [ "$current_file" != "$previous_file" ]; then
            # Extract the directory name
            solved_dir="${current_file%/*}"
            echo "The $solved_dir directory"

            # Construct absolute paths for Solved and Unsolved directories
            unsolved_dir="${solved_dir/\/Solved/\/Unsolved}"
            # Copy the solved.py file to the "Unsolved" subdirectory
            mv "${solved_dir}/solved.py" "${unsolved_dir}/solved.py"
            echo "Copied $file to $unsolved_dir"

            # Rename the unsolved.py file to unsolved_tmp.py
            mv "${unsolved_dir}/unsolved.py" "${unsolved_dir}/unsolved_tmp.py"
            echo "Renamed unsolved.py to unsolved_tmp.py"

            # Rename the solved.py file to unsolved.py
            mv "${unsolved_dir}/solved.py" "${unsolved_dir}/unsolved.py"
            echo "Renamed solved.py to unsolved.py"

            # Run the test.py file on the unsolved.py file
            echo "Testing unsolved file"
            python "${unsolved_dir}/tests.py"

            mv "${unsolved_dir}/unsolved.py" "${solved_dir}/solved.py"
            echo "Moved unsolved.py back to solved.py"

            # Move the unsolved_tmp.py file back to the "Unsolved" subdirectory
            mv "${unsolved_dir}/unsolved_tmp.py" "${unsolved_dir}/unsolved.py"
            echo "Moved unsolved_tmp.py back to unsolved.py"

            # Update the previous file to the current file
            previous_file="$current_file"
            else
            echo "The file has already been processed"
            fi
        done
    fi
done
