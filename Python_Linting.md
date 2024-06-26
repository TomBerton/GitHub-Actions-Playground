# Python Linting Workflow

## Workflow for linting Python files

The following `python-linting.yml` [file](.github/workflows/python-linting.yml) is used as a GitHub Action workflow to perform linting Python files using flake8 when a pull request is made or merged to the main branch.

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

After we create the main section, we define the workflow "job" with the `jobs` object. Under the `jobs` object, we define the name of the job, i.e., "build".

```yaml
jobs:
  build:
    name: Linting Python files with Flake8
    runs-on: ubuntu-latest
    # Required permissions to run the action
    permissions:
      contents: read
      pull-requests: read
```

* The build job above is given the name, "Linting Python files with Flake8".
* Each job runs in an environment that is specified by `runs-on`.
    * Our "build" job will run on the latest version of ubuntu.
* The permissions are set to read the contents of the repository and pull requests.

## Workflow Steps

Underneath the `jobs` object we define the steps in the workflow using the `steps` object.
* The `steps` object  contains information about the steps in the current job.

Underneath the `steps` object we can add as many steps as needed using the `name` parameter.

### Checkout the Github Workspace

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

### Get the Changed Files in the PR

```yaml
- name: Get changed files
  id: changed-files
  uses: tj-actions/changed-files@v42
   # To compare changes between the current commit and the last pushed remote commit set `since_last_remote_commit: true`. e.g
  with:
    since_last_remote_commit: true
```

* The name of this action is "Get changed files" and will use the action, `tj-actions/changed-files@v42`.
    * You can view the source of this action [here](https://github.com/tj-actions/changed-files).
* We have given this action and `id` which will be used later to reference the action of getting all the changed files in the PR.
* This action will compare changes between the current commit and the last pushed remote commit by using:

    ```yaml
    with:
      since_last_remote_commit: true
    ```

### Print out all the Changed Files

```yaml
- name: Print all the changed files
  env:
    ALL_CHANGED_FILES: ${{ steps.changed-files.outputs.all_changed_files }}
  run: |
    for file in $ALL_CHANGED_FILES; do
      echo "$file was changed"
    done
```

* The name of this action is "List all changed files" and it will get all the changed files, including new files that are added with a PR using the following naming convention: `${{ steps.changed-files.outputs.all_changed_files }}`
* The `${{ }}` is the syntax used in GitHub Actions workflow to reference outputs within the workflow. The outputs are assigned to the variable `ALL_CHANGED_FILES`.
* In the reference, the `steps.changed-files` refers to the `id`, `changed-files`, in the `steps` object.
* The `outputs.all_changed_files` refers to the outputs, which will be all the changed files.
* The `.all_changed_files` output name is part of the `tj-actions/changed-files@v42` GitHub action that returns a combination of all added, copied, modified and renamed files as strings.
    * You can see all the other named output [here](https://github.com/tj-actions/changed-files?tab=readme-ov-file#outputs-).
* Next, we use the `run` command to print out all the files referencing the variable, `ALL_CHANGED_FILES`,using bash shell commands.


### Set up Python

```yaml
- name: Set up Python 3.10
  uses: actions/setup-python@v5
    with:
      python-version: "3.10"
```

* This step will use the GitHub action `actions/setup-python@v5` to install the version of Python using the `with` statement.
* This action will need to be updated periodically.
    * You can view the source of this action [here](https://github.com/actions/setup-python).

### Install Dependencies

```yaml
 - name: Install dependencies
   run: |
    python -m pip install --upgrade pip
    pip install flake8
```

* This step, "Install Dependencies", will install and upgrade to the latest version of `pip`, and install `flake8`.


### Lint Python code using Flake 8

```yaml
-  name: Lint with flake8
    run: |
      for file in ${{ steps.changed-files.outputs.all_changed_files }}; do
      # Check for Python files
        if [[ $file == *.py ]]; then
          echo "Linting $file"
          # stop the build if there are Python syntax errors or undefined names
          flake8 . $file --count --select=E9,F63,F7,F82 --show-source --statistics
          # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
          flake8 . $file --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
        fi
    done
```

* In this step we will lint only the Python files that have changed in the PR by using:

    ```yaml
    for file in ${{ steps.changed-files.outputs.all_changed_files }}; do
      # Check for Python files
      if [[ $file == *.py ]]; then
        echo "Linting $file"
    ```

* **Note:** Beware that unsolved Python files may cause linting to fail, since we provide code they students have to build on.

* This step will check for syntax errors and undefined names, and we will get a warning if a line is more than 127 characters long.
* If there are any errors the build will halt and you will have to fix the errors through a commit to the PR. Then, the workflow will run again.
* We can exclude some errors by using `--select=!E9`, for example. Or add them to the `.flake8` config file (described next).
* Here is a list of [error codes](https://pycodestyle.pycqa.org/en/latest/intro.html#error-codes).
* Here is a Flake8 [cheat sheet](https://michaelcurrin.github.io/dev-cheatsheets/cheatsheets/python/linting/flake8.html) for further reference.

* To ignore errors and even certain files, such as our unsolved files in the activity folders it is best to create a [`.flake8` config file](.flake8) in the top-level of the repository as follows:

    ```text
    [flake8]
    exclude =
        Lessons/**/**/**/**/Unsolved/
        Lessons/**/**/**/**/Solved/
        Homework/**/Starter_Code/
        Homework/**/Solution/
    ```

#### Final Notes

One of the issues I ran into was linting was performed on every Python file in the directory.To make sure linting only occurs on the changed files in the PR, I excluded specific directories in the `.flake8` config file. I did this because, we would assume that once a file is in the main branch it has gone through the linting process.
