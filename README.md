# project1: Find Washer Machine in Local

![pytest workflow](https://github.com/tkminh/project1/actions/workflows/python-app.yml/badge.svg)


## Project Structure
1. app: backend
2. app/test: unittest for backend
3. client; frontend
4. .github/workflows


## SETUP
1. Install Python 3.10+ with PIP
2. Run command to install or active virtual environment for everytime:
```
pip install virtualenv
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
```
3. Run `flask run` to start the web at `http://127.0.0.1:5000`, or press F5 from VSCODE
4. Login: admin / ********
5. Press Ctrl + C to exit.
6. API: `http://127.0.0.1:5000/swagger/v1`


## Coding Habit
1. Create new branch for every feature
2. Alway pull first before commit & push
3. Code must run pass on local test before commit
4. Test code by create a file name `test_*.py` in test directory
5. Run `pytest -s app/test/test_*.py`

## Changelog
