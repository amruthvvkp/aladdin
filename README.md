# Aladdin - Automated Learning and Autonomous Distributed Diversified Investment Network

[![GitHub contributors](https://img.shields.io/github/contributors/amruthvvkp/aladdin)](https://github.com/amruthvvkp/aladdin/graphs/contributors)
[![GitHub license](https://img.shields.io/github/license/amruthvvkp/aladdin)](https://github.com/amruthvvkp/aladdin/blob/master/LICENSE)
![GitHub branch checks state](https://img.shields.io/github/checks-status/amruthvvkp/aladdin/master)
![GitHub language count](https://img.shields.io/github/languages/count/amruthvvkp/aladdin)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/prefect)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/amruthvvkp/aladdin)
![GitHub last commit](https://img.shields.io/github/last-commit/amruthvvkp/aladdin)

[![DeepSource](https://deepsource.io/gh/amruthvvkp/aladdin.svg/?label=active+issues&show_trend=true&token=PdJ1ceHD-PbR2IuoxspR-iGx)](https://deepsource.io/gh/amruthvvkp/aladdin/?ref=repository-badge)
[![DeepSource](https://deepsource.io/gh/amruthvvkp/aladdin.svg/?label=resolved+issues&show_trend=true&token=PdJ1ceHD-PbR2IuoxspR-iGx)](https://deepsource.io/gh/amruthvvkp/aladdin/?ref=repository-badge)
![GitHub pull requests](https://img.shields.io/github/issues-pr/amruthvvkp/aladdin)
![GitHub milestones](https://img.shields.io/github/milestones/all/amruthvvkp/aladdin)

Aladdin is a model designed to trade using the user's trading account just the way the user does it. This is not a replacement of human effort but an assisted trading to the actual human effort.
This is intended to analyze, monitor, screen and trade stocks, options and crypto currencies based on their historic prices and fluctuation factors.

## Getting Started

This project is being developed on Python 3.8. Install the latest version of Python 3.8 on your working environment.

### Create Virtual Environment

Considering you have already installed Python 3.8 on your machine, proceed with the below steps.

#### Create blank virtual environment at project root

You need a working virtual environment based off Python 3.8 to get started.

If you are on Linux/Mac OS/WSL

```bash
python3 -m venv .venv
```

If you are on Windows

```bash
python3 -m venv .venv
```

Upgrade pip to avoid any keylogging

```bash
python -m pip install --upgrade pip
```

#### Install from requirements file

The project houses a requirements.txt for production requirements, requirements-dev.txt for development and requirements-test.txt for testing requirements.

If you are looking to contribute to the project -

```bash
cd <project root>
pip install --upgrade -r requirements-dev.txt
```

If you are looking to run the application -

```bash
cd <project root>
pip install --upgrade -r requirements.txt
```

If you are looking to test the application -

```bash
cd <project root>
pip install --upgrade -r requirements-test.txt
```

Environments created in the project root under the names .venv or .prefect or .testplan are automatically recognized with the configuration under .gitignore file. Any other names used for the Python virtual environment has to be added under `.git/info/exclude` file locally for Git to avoid tracking the files under the created virtual environment if the folder resides under the project root.

#### Install package as editable - ONLY FOR DEVELOPMENT

Once done - you might have to install this application package as an editable project to your venv.

```bash
pip install -e .
```

I've been using both Windows and WSL on Windows 11 to develop and test the application. If you are on a different OS, please feel free to upgrade this README.md page.

### Dependencies

All dependencies can be found under `requirements.txt` or `requirements-dev.txt`.

### Pre-Requisites

Prefect Orion requires SQLite to be installed.

If you are on Ubuntu, run this from your terminal -

```bash
sudo apt update
sudo apt install sqlite3
sqlite3 --version
```

If you are on windows, follow the below steps -

1. From SQLite [download page](https://www.sqlite.org/download.html) download the binaries under the windows section.
2. Download `sqlite-shell-win32-*.zip` and `sqlite-dll-win32-*.zip` zipped files.
3. Create a folder `C:\sqlite` and unzip above two zipped files in this folder, which will give you sqlite3.def, sqlite3.dll and sqlite3.exe files.
4. Add `C:\sqlite` in your _PATH_ environment variable and finally go to the command prompt.
5. Open a terminal window and type in `sqlite3` which should show the sqlite version.

Please note that we need a minimum version of sqlite 3.24.0 or above for Prefect Orion to work properly.

### IDE Settings

My preferred IDE is Visual Studio Code and I am keeping all my IDE settings under a .vscode folder in the project root. I am using YAPF for formatting, mypy and SonarLint for code linting and style checking. All the extensions that are recommended for this project can be found in the workspace recommendation file - `.vscode/extensions.json`.

VS Code supports python debugging options, hence the debugger configurations can also be found under `.vscode/config.json`.

You can open the workspace in VS Code by selecting `aladdin.code-workspace` directly.

A recommended way of easing the pain of configuring the IDE is to sync the settings using VS Code settings sync. The configurations I've setup for the project includes GitHub linking too. You can login to VS Code accounts using your GitHub account and sync everything right out of the box.

### Starting API Server

If you are contributing to the project, consider using the launch.json configuration within the VS Code IDE to allow debugging to work as you develop.

If you are looking to run this application as a service, you can start the API server with Uvicorn.
Assuming your venv is activated and you are at the project root on your terminal -

```bash
prefect orion start
```

Once the server starts up navigate to http://127.0.0.1:4200 to open the application or http://127.0.0.1:4200/docs to open the Swagger documentation.

### Development Strategy

_Coming Soon_

#### Architecture

This project is built on top of [FastAPI](https://fastapi.tiangolo.com/), [Prefect](https://www.prefect.io/). Any supporting libraries could add up as dependencies.

#### Testing

- Functional testing can rely upon GitHub integrated tools like [TestQuality](https://www.testquality.com/). Although the tools are still debatable, we certainly need a solution where we can write and save test cases without any fuss.
- Automation testing can rely upon [[PyTest](https://github.com/pytest-dev/pytest)] or [TestPlan](https://github.com/morganstanley/testplan). The base framework is yet to be built. Framework conclusion can come in at a later point of time through a hybrid solution for Unit Tests and Regression Tests.
- API manual testing files from [Insomnia](https://insomnia.rest/) can be added to the project repository and checked into GitHub directly.

## Project Goals

### Milestone #1 - Create a asset analyzer

- Have a working Front end ad Back end applications to screen assets based on user preference.
- Authentication model to be set in for the entire application.
- Basic asset analyzer model to be in place.
- Concurrent working model of unit tests.

### Milestone #2 - Create a real-time asset monitoring system

- Integrate data models and create services that can monitor user listed assets in realtime.
- Sends notifications to users on Buy/Sell trigger situations.
- Runs as a continuous service on cloud deployment.
- Full fledged test management of manual and automated tests.
- Azure backed cloud based CI/CD triggers for deployment.

### Milestone #3 - Create a live stock screener, price prediction models

- Set up service based model to screen for potential assets across various markets.
- Integrate ML models to predict prices with live data and backtested strategies.
- A scalable back-test model to improve the prediction algorithms.

### Milestone #4 - Create autonomous algo trader

- Target autonomous trading with the entire data set that we have in place.
- Full fledged alert based model that helps in reducing the risk of autonous trading.
- Complete end-to-end testing and cloud based delivery.

## Credits

- Github badges by [Shields.IO](https://shields.io/)
