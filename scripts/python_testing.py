import subprocess
import sys

def run_file(file_path):
    """Runs the specified Python file and prints its output."""
    try:
        result = subprocess.run(["python", file_path], capture_output=True, text=True)
        print(result.stdout)
        if result.returncode != 0:
            print(f"Error running {file_path}:")
            print(result.stderr)
            sys.exit(1)  # Exit with an error code to indicate failure
    except subprocess.CalledProcessError as e:
        print(f"Failed to run {file_path}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Get the file path from the command-line argument
    file_to_test = sys.argv[1]
    run_file(file_to_test)
