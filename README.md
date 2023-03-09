# LinkedIn Connection Request Automation

This is a Python script that uses Selenium and ChromeDriver to automate sending connection requests to LinkedIn users with the keyword "techrecruiter" in their profiles.

## Setup

To run this script, you will need to have the following installed:

- Python 3
- ChromeDriver
- Selenium
- python-dotenv

You can install the required Python modules by running the following command:
```shell
pip install selenium python-dotenv
```
## Usage

To use this script, you will need to have a LinkedIn account and create a `.env` file in the same directory as the script with your LinkedIn login credentials:
```shell
LOGIN=your_username
PASSWORD=your_password
```
You can then run the script by running the following command:
```shell
py lkdn.py
```
## Note

The script may trigger LinkedIn's anti-spam measures if run too frequently or aggressively. Use at your own risk.