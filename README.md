# Placement_Prediction

Developed by daniel-was-taken, VaishnaviSawant1901, PremTatkari, rachelabe01

## How to run:
1. Install venv on Windows by running: pip install virtualenv
2. Create virtualenv by running: virtualenv environmentname
3. Activate environment: environmentname\Scripts\activate
4. Install python packages: pip install -r requirements.txt
5. Run placement.py in VSCode by going to Run > Start Debugging OR simply pressing F5
6. Run app: flask --app app run  

## NOTE:
1. MySQL Workbench should be installed

Ref: https://www.w3schools.com/mysql/mysql_install_windows.asp

2. Setup database in MySQL

Ref: https://codeshack.io/login-system-python-flask-mysql/

From the above link make the following changes:
1. Database name from **pythonlogin** to **login**
2. Table name from **accounts** to **auth**
3. Column name from **username** to **name**
