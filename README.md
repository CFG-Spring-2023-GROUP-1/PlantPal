# PlantPal

### Introduction
....
### Teammembers
....


---
# Framework
The application is based on the Flask framework with some extension modules, including:
### Security: 
1. ***python-dotenv*** used to securely store keys and passwords.
2. ***bcrypt*** used for password hashing and encryption.
### DataBase:
1. ***mysql-connector-python***

# Testing
1. ***unittest*** A suite of unit tests has been created and the files are stored in the /tests folder.  
Go to python/ and run ``` python -m unittest discover -s tests/ ```  
note: need to input nessary date accordingly  
2. ***postman*** run endpoints
# Enviromenet Setup
### Local Set up
1. clone the project
2. create the virtual environment
3. run ```pip install -r requirements.txt``` from your terminal
4. create .env file under python/
    ```
    RAPID_API_URL = https://house-plants2.p.rapidapi.com/
    RAPID_API_KEY = add/your/key/here
    PERENUAL_API_KEY = add/your/key/here
    USER = root
    PASSWORD = add/your/password/here
    HOST = 127.0.0.1
    PLUGIN = mysql_native_password
    DB = plantpal
    ```
### Database
1. Open MySQL Workbench.
2. Create the database and table by executing the SQL script sql\table_creation.sql.
3. Insert data into the table using the SQL script sql\insert_to_db.sql.
Please ensure that you have MySQL Workbench installed and that the SQL scripts mentioned above are available in the specified paths.

### Local Running
1. Start app
    - open blueprint.py and click run in IDEs
    - Or run ```python blueprint.py``` in your terminal
2. Access Endpoints
    - open your browser and go to http://localhost:5000

3. Start My Calendar
    - open my_calendar.py and click run in IDEs
    - Or run ```python my_calendar.py``` in your terminal