# DJANGO_EMAIL_AUTOMATION
This website is hosted on heroku and integrates sendgrid(twillio) to send emails to users containing the current temperature of selected city
heroku app - [https://django-gmail-app.herokuapp.com/admin](https://django-gmail-app.herokuapp.com/admin)

### credentials:
username - patkar<br>
password - patkar

## set up the project locally
```sh
py manage.py makemigrations
py manage.py migrate
py manage.py collectstatic
py manage.py runserver
```

* create an account on sendgrid and create a new api_key
* create a secrets.py file in email_app.env folder, in it store the api credentials like

```py
EMAIL_HOST_USER = # email id linked with sendgrid account
SENDGRID_API_KEY = # sendgrid api key after validating user
API_KEY = # secret key of created api_key
```