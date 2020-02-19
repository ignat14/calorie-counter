# Calorie Counter

  Web application for daily tracking of meals and their calories.

## Backend Project setup
- in the backend folder install requirements and migrate

```
pip install -r requirements.txt
python manage.py migrate
```
- for starting the backend server
```
python manage.py runserver
```
- to create admin user
```
python manage.py createsuperuser
```
- to run tests
```
python manage.py test
```

## Frontend Project setup
- in the frontend folder install requirements

```
npm install
```
- for starting the frontend server
```
npm run serve
```

## Settings files

  - By default the backend server runs on port 8000 and the frontend server runs on port 8080. If the servers run on different port, there are dedicated variables in the settings files in both frontend and backend that need to be change accordingly.
  - In order to be able to send emails through the application (for  signup and password reset) settings_local.py file needs to be created in the main app on the backend that contains the email variables. The file should look like this:
```
"""
Local Settings for development that consist of sensitive data
and should not go to the git repo
"""

# Email Settings
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.sendgrid.com'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
DEFAULT_FROM_EMAIL = 'Calorie Counter <noreply@caloriecaunter.com>'
SERVER_EMAIL = 'noreply@caloriecaunter.com'
```

