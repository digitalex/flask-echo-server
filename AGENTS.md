# AGENTS.md

This file provides instructions for AI agents working on this repository.

## Project Overview

This project is a simple Flask echo server. It has a single endpoint, `/echo`, that accepts POST requests with a JSON body and returns the same JSON in the response.

## Getting Started

To get started with this project, you need to have Python and Poetry installed. The setup instructions are detailed in the `README.md` file. Please refer to it for the exact commands.

## Running the Application

To run the Flask application, use the following command:

```bash
/usr/bin/python3 -m poetry run flask --app flask_echo_server/app.py run
```

## Running Tests

To run the tests, use the following command:

```bash
/usr/bin/python3 -m poetry run pytest
```

The tests are located in the `tests/` directory.

## Dependencies

This project uses Poetry to manage dependencies. The dependencies are defined in the `pyproject.toml` file. The `poetry.lock` file contains the exact versions of the dependencies used in the project.

To install the dependencies, you first need to install `pip` and `poetry`. The following commands were used to set up the environment:

```bash
sudo apt-get update && sudo apt-get install -y python3-pip
export PIP_BREAK_SYSTEM_PACKAGES=1
/usr/bin/python3 -m pip install pytest tox poetry
/usr/bin/python3 -m poetry install
```

When adding or updating dependencies, please use the appropriate Poetry commands and commit both the `pyproject.toml` and `poetry.lock` files.

## Code Style

Please follow the standard Python coding conventions (PEP 8) when writing code in this repository.
