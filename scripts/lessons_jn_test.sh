#!/bin/bash

# Iterate over changed files
for file in $1; do
    # Check for Python solution files
    if [[ $file == *solution.ipynb ]]; then
        echo "Testing $file"
        gh_runner_path="/home/runner/work/GitHub-Actions-Playground/GitHub-Actions-Playground/"
        relative_path="${file#$gh_runner_path}"
        directory_path="$(dirname "$relative_path")"
        echo "Directory path: $directory_path"

        # Change directory
        cd $directory_path

        # Run the Python test script
        python ../../../../../../scripts/jn_test.py

        # Navigate back to the original directory
        cd ../../../../../../
    fi
done
