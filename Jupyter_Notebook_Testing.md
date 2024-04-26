# Jupyter Notebook Testing Workflow

## Workflow for Jupyter notebook Files

The following `jupyter_notebook_test.yml` [file](.github/workflows/jupyter_notebook_test.yml) is used as a GitHub Action workflow to execute Python files when a pull request is made or merged to the main branch.

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
```

## Workflow "Check" Job

For this workflow, we'll create two jobs. The first job will be the "check" job. This job will check the PR for solved Jupyter notebook files. If there any solved files in the PR then the second job ("test") will download the dependencies, build the `dev` environment, activate it, and execute / test the solved files.

* Our build will "Checkout repository code" and will run on the latest version of ubuntu.
* We create a variable to reference the changed Jupyter notebook files with the `jn-files-found` object. We can reference this object later to get the outputs of the job, or the changed files.

```yaml
jobs:
  check:
    name: Checkout repository code
    runs-on: ubuntu-latest
    outputs:
      jn-files-found: ${{ steps.check-jn-files-found.outputs.jn-files-found }}
```


### Step 1: Checkout the Github Workspace

In the first step we checkout the GitHub workspace using `actions/checkout@v4`.

```yaml
steps:
  - name: Checkout code
    uses: actions/checkout@v4
    with:
      fetch-depth: 0
```

### Step 2: Get the Changed Files in the PR

In second step we will get all the changed files.

```yaml
- name: Get changed files
  id: changed-files
  uses: tj-actions/changed-files@v42
   # To compare changes between the current commit and the last pushed remote commit set `since_last_remote_commit: true`. e.g
  with:
    since_last_remote_commit: true
```

### Step 3: Check for Jupyter notebook solutions in the PR.

In the third step we will check if there are Jupyter notebook solutions in the PR using `if grep -q "solution.ipynb" <<< "${{ steps.changed-files.outputs.all_changed_files }}"; then`. If there are Jupyter notebook solutions, we pass the `true` statement to the `$GITHUB_OUTPUT` environment variable, else we pass `false`.

```yaml
- name: Check for Jupyter notebook solutions in the PR.
  id: check-jn-files-found
  run: |
    if grep -q "solution.ipynb" <<< "${{ steps.changed-files.outputs.all_changed_files }}"; then
      echo "Jupyter notebook solutions are in the PR."
      echo "jn-files-found=true" >> $GITHUB_OUTPUT
    else
      echo "There are no Jupyter notebook solutions found in the PR."
      echo "jn-files-found=false" >> $GITHUB_OUTPUT
    fi
```

## Workflow "Test" Job

Now, we create the second job. This job will only run if there are Jupyter notebook solutions in the PR. If there any solved files in the PR then we build the `dev` environment, activate it, and execute / test the solved files.

```yaml
test:
  name: Test Jupyter notebooks
  runs-on: ubuntu-latest
  needs: check
  if: needs.check.outputs.jn-files-found == 'true'
  defaults:
    run:
      shell: bash -l {0}
```

* This job requires, i.e., "needs", the "check" job. Before any steps are run we will check if the "output" from the "check" job is `true`. If it is, then this job will proceed. If not, then this job is skipped.
* Since we are using a bash shell commands to activate the conda environment in a later step, we need define which shell to use. In `defaults` we run the shell with `bash -l {0}`, where `l` is login, and the environment is set to `{0}` until the time of execution.
    * See the [Stackoverflow](https://stackoverflow.com/questions/69070754/shell-bash-l-0-in-github-actions#:~:text=%2Dl%20to%20insure%20a%20login,actual%20script%20command%20to%20execute.) for an explanation.

### Checkout the Github Workspace

In the first step we checkout the GitHub workspace using `actions/checkout@v4`.

```yaml
steps:
  - name: Checkout code
    uses: actions/checkout@v4
    with:
      fetch-depth: 0
```

### Set up Miniconda

In this step will use set up Miniconda on the ubuntu instance and install all the requirements as defined in the `environment.yml` file using `conda-forge` in the `dev` environment.

```yaml
  # See: https://github.com/marketplace/actions/setup-miniconda
  - name: Setup Miniconda
    uses: conda-incubator/setup-miniconda@v3
    with:
      auto-update-conda: true
      miniforge-variant: Mambaforge
      channels: conda-forge
      activate-environment: dev
      environment-file: env_files/environment.yml
      use-mamba: true
```


### Activate the Conda Environment

In this step we will activate the `dev` environment.

```yaml
  - name: Activate environment
    run:
      conda activate dev
```


### Run script to test Jupyter notebooks

In this step we will change directory to the "Lessons" directory where activities are stored, then run the `jn_test.py` file which will execute only the Jupyter notebook solution files.

```yaml
- name: Run script to test Jupyter notebooks
  run: |
    cd Lessons
    python ../scripts/jn_test.py
```

#### Final Notes

The [jn_test.py](scripts/jn_test.py) script executes all the Jupyter notebook solution files in the given directory irregardless if it is in the PR or not. Ideally, we would like to execute only the solved files that have changed in the PR, which is the next step in development.
