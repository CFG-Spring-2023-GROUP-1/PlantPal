# PlantPal

### Introduction
PlantPal is an all-inclusive plant care app created to help plant lovers effectively care for their plants. With a user-friendly interface, it offers a range of features that simplify plant care and promote healthy growth. It includes user authentication, a My Plants feature for managing plant collections, a Plant Calendar feature to track watering needs, a Plant Suggestions feature for recommending suitable plants, and a Plant Friend feature that provides tips and tutorials on nurturing plants. PlantPal aims to make plant care effortless and enjoyable for users.
### Teammembers

_Jia Chi_

_Emina Ergul_

_Rebecca Hodges_

_Ying Ting Liu_

_Oluwaferanmi Olatunji_

---

# Framework
## Backend
The application is based on Flask framework with some extension modules, including:
#### Security:
1. ***python-dotenv*** used to securely store keys and passwords.
2. ***bcrypt*** used for password hashing and encryption.
#### DataBase:
1. ***mysql-connector-python***

## Frontend
React and Typescript, Tailwind, axios.


# Testing
1. ***unittest*** A suite of unit tests has been created and the files are stored in the /tests folder.


# Enviroment Setup


1. Ensure you have ****pip (>v23.1.2)****, ****node (>v16.0.0)**** and ****yarn (>v1.22.11)**** installed globally
2. Clone the project -  run ```git clone https://github.com/CFG-Spring-2023-GROUP-1/PlantPal.git``` from your terminal

### Backend
1. cd into ```server / python``` 
2. Create the virtual environment
and run ```pip install -r requirements.txt``` from your terminal to install dependencies

2.   Create .env file 
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

3.   Start app
    - open blueprint.py and click run in IDEs
    - Or run ```python blueprint.py``` in your terminal
4. Access Endpoints
    - open your browser and go to http://localhost:5000

5. Start My Calendar
    - open my_calendar.py and click run in IDEs
    - Or run ```python my_calendar.py``` in your terminal
6. Start My Plants 

    
### Frontend
1. cd into the ``` client ``` directory and run ```yarn install```  to install dependencies

2.   create .env file 

    ```  
    REACT_APP_RAPID_API_URL=https://house-plants2.p.rapidapi.com/  
    REACT_APP_RAPID_API_KEY=Your_Api_Key  
    REACT_APP_RAPID_HOST= house-plants2.p.rapidapi.com  
    REACT_APP_BASE_URL = http://127.0.0.1:5000/  
    ```

3. Run ```yarn start``` to start project locally
### Database
1. Open MySQL Workbench.
2. Create the database and table by executing the SQL script sql\table_creation.sql.
3. Insert data into the table using the SQL script sql\insert_to_db.sql.
Please ensure that you have MySQL Workbench installed and that the SQL scripts mentioned above are available in the specified paths.

### Github
[View Github Repo](https://github.com/CFG-Spring-2023-GROUP-1/PlantPal) 
