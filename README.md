# GitHub-Actions-Playground

This repository is used to test GitHub Actions.

## Files and Resources

The GitHub Actions workflows are stored in the [.github/workflows](.github/workflows/) directory.

Documentation for GitHub Actions can be found [here](https://docs.github.com/en/actions).

You can initiate a GitHub Action by clicking on "Actions" on the "Home" page of a repository.

![GitHub Actions button](Images/GH_Actions_button.png)

After clicking on "Actions", you will be asked to choose a workflow, or you can click "set up a workflow yourself".

![Choose a workflow](Images/Choose_workflow.png)

Alternatively, you can create a `.github/workflows` directory, and add your workflow to the `workflows` folder.

##  Workflow for linting Python Files

In the [.github/workflows](.github/workflows/) directory you will find the `python-linting.yml` [file](.github/workflows/python-linting.yml). This file will perform linting on all the files Python files that have been changed on the PR using flake8.

A detailed explanation of the workflow steps in the `python-linting.yml` can be found [here](Python_Linting.md).

## Workflow for Testing Python Files

In the [.github/workflows](.github/workflows/) directory you will find the `test-python-files.yml` [file](.github/workflows/test-python-files.yml). This file will test all Python solution files that have been changed on the PR.

A detailed explanation of the workflow steps in the `test-python-files.yml` can be found [here](Python_Testing.md).


## Workflow for Testing Jupyter Notebook Files

In the [.github/workflows](.github/workflows/) directory you will find the `jupyter_notebook_test.yml` [file](.github/workflows/jupyter_notebook_test.yml). This file will test all Jupyter notebooks solution files.

A detailed explanation of the workflow steps in the `test-python-files.yml` can be found [here](Jupyter_Notebook_Testing.md).

* **Note:** At the moment we pass the directory where the Jupyter notebook files are located, i.e., "Lessons" or "Homework" folders. Then, [jn_test.py](scripts/jn_test.py) script executes all the Jupyter notebook solution files in the directory. Ideally, we would like to execute only the solved files that have changed in the PR, which is the next step in development.
