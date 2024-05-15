# My Chitter project 

## Setup

```shell
# Clone the repository to your local machine
; git clone git@github.com:makersacademy/web-applications-in-python-project-starter-html.git YOUR_PROJECT_NAME

# Or, if you don't have SSH keys set up
; git clone https://github.com/makersacademy/web-applications-in-python-project-starter-html.git YOUR_PROJECT_NAME

# Enter the directory
; cd YOUR_PROJECT_NAME

# Set up the virtual environment
; python -m venv html-application-starter-venv

# Activate the virtual environment
; .\venv-name\Scripts\activate

# Install dependencies
(html-application-starter-venv); pip install -r requirements.txt
# Read below if you see an error with `python_full_version`

# Create a test and development database
(html-application-starter-venv); createdb YOUR_PROJECT_NAME
(html-application-starter-venv); createdb YOUR_PROJECT_NAME_test

# add .env
DB_USERNAME="postgres"
DB_PASSWORD="<your password"

# Open lib/database_connection.py and change the database name to YOUR_PROJECT_NAME
(html-application-starter-venv); open lib/database_connection.py

# Seed the development database
(html-application-starter-venv); python seed_dev_database.py

# Run the tests (with extra logging)
(html-application-starter-venv); pytest -sv

# Run the app
(html-application-starter-venv); python app.py
# Now visit http://localhost:5001/
```


