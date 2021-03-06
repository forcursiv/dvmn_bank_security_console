# Bank security console

Security console to monitor employees and their operations.

### How to install

Create .env file with following consts to be able to connect to database
```
DB_HOST=<database host>
DB_PORT=<database port>
DB_NAME=<database name>
DB_USER=<database user>
DB_PASSWORD=<databse password>
SECRET_KEY=<website secret key>
DJANGO_DEBUG=<debug flag>
ALLOWED_HOSTS=<list of allowed hosts>
```

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### How to run

Run command
```
python manage.py runserver 8000
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
