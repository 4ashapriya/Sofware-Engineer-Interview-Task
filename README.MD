This is an implementation of the backend of a simple software having functions to add_user, login, and uploading a csv file. The code can be cloned by the following command:
#### git clone https://github.com/4ashapriya/Sofware-Engineer-Interview-Task.git

The requirements for this project can be found in the requirements.txt file and it can be installed using the following command:
#### pip install -r requirements.txt

The starting point for this project is the main.py file. And the project can be initiated with the following command:
#### python main.py

JWT Token authentication is used for authentication and authorization purposes. Password hashing is used to secure the user passwords.
For PII and IP sensitive data, the hashing algorithm is used secure it permanently. 

Pytest is implemented and it can be checked using the following commands:

#### Add User : pytest .\test\test_add_data.py
#### Login : pytest .\test\test_login.py
#### Upload Data : pytest .\test\test_add_data.py
