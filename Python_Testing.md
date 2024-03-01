# Python Testing Workflow

## Workflow for testing Python Files

The following `test-python-files.yml` [file](.github/workflows/test-python-files.yml) is used as a GitHub Action workflow to execute Python files when a pull request is made or merged to the main branch.

## Workflow Action

This is the main section to trigger the workflow in your GitHub action.

```yaml
on:
  pull_request:
  push:
    branches:
    - main
    #   # - 'aus-**'
    #   # - 'dev-**'
    paths-ignore:
      # Ignore these directories.
      - 'scripts/*.py'
```

* The workflow will be executed when a push or pull request occurs on the main branch the workflow is triggered.
* You can also set the action to occur on specific branches, like `main`, or with  `aus-` and `dev-` in the branch.
* The `paths-ignore:` is used to ignore files in specific directories that you want to exclude from the workflow.

## Workflow Jobs

In the section below, we "build" the jobs. All the jobs underneath `jobs` are defined by a `name`.

```yaml
jobs:
  build:
    name: Testing Python Files
    runs-on: ubuntu-latest
    # Required permissions to run the action
    permissions:
      contents: read
      pull-requests: read
```

* The build job above is given the name, "Testing Python Files" and will run on the latest version of ubuntu.
* Each job runs in an environment that is specified by `runs-on`.
    * Our "build" job will run on the latest version of ubuntu.
* The permissions are set to read the contents of the repository and pull requests.

## Workflow Steps

Underneath the `jobs` object we define the steps in the workflow using the `steps` object.
* The `steps` object  contains information about the steps in the current job.

### Step 1: Checkout the Github Workspace

```yaml
steps:
  - name: Checkout code
    uses: actions/checkout@v4
    with:
      fetch-depth: 0
```

* In the first step, we always want to checkout the GitHub workspace. This is done with the `actions/checkout@v4`.
    * You can view the documentation for this action [here](https://github.com/actions/checkout).
* This action will be updated periodically and will need to change with the latest version.
* We use `fetch-depth: 0` to get the latest changes from the previous commit.

### Step 2: Get the Changed Files in the PR

In this step, we will get all the changed files like we did with linting.

```yaml
- name: Get changed files
  id: changed-files
  uses: tj-actions/changed-files@v42
   # To compare changes between the current commit and the last pushed remote commit set `since_last_remote_commit: true`. e.g
  with:
    since_last_remote_commit: true
```

* You can view the source of this action [here](https://github.com/tj-actions/changed-files).
* This action will compare changes between the current commit and the last pushed remote commit by using:

    ```yaml
    with:
      since_last_remote_commit: true
    ```

### Step 3: Set up Python

In this step will use the GitHub action `actions/setup-python@v5` to install the version of Python using the `with` statement.

```yaml
- name: Set up Python 3.10
  uses: actions/setup-python@v5
    with:
      python-version: "3.10"
```


* This action will need to be updated periodically.
* You can view the source of this action [here](https://github.com/actions/setup-python).

### Step 4: Install Dependencies

In this step we will install the latest version of `pip`.

```yaml
- name: Install dependencies
  run: |
    python -m pip install --upgrade pip
```


### Step 5: Testing Python code.

In this step we will execute only the Python solution files that have changed in the PR by using:

```yaml
- name: Testing Python files
  run: |
    for file in ${{ steps.changed-files.outputs.all_changed_files }}; do
    # Check for Python solution files
      if [[ $file == *solution.py ]]; then
        echo "Testing $file"
        python $file
      fi
    done
```

* **Note:** Beware that if files require user input or other dependency then the workflow will fail. Unsolved Python files are not run because we provide starter code that may include undeclared variables for instance.


#### Final Notes:

To test files that require dependencies such as user input we may opt to use `pytest` we would have to create another Python file with test cases where the inputs are defined. This would involve creating a hidden directory in GitHub that is not sent to the students and use pytest for example:

`pytest .test-cases/inputs_solution_test.py 01-Lesson-Plans/02-Python-Programming-1/1/Activities/05-Ins_Prompts/Solved/inputs_solution.py`


To test files that require dependencies such as CSV files we may might have to create a temporary folder that holds all the changes in the PR and then pass that directory to a script and walks through the directory to find the Python file to run.
