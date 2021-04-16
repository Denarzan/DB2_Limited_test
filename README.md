# DB2 Limited test

### Task

Django application - public chat room(only RESTful API).
Unauthenticated users can post messages via API in chat so others can read them.
Messages need to be saved to the database.

Basic requirements:
- Django, Django REST Framework, PostgreSQL
- The message must contain author(unauthenticated user) email and text, create date and update date.
- Email validation (regex to check if that is real email)
- Message validation (regex to check if message is not empty string, and length < 100)

API methods:
- GET method for getting all messages with pagination by 10 messages per request.
e.g.
/api/messages/list/0 will return first 10 messages
/api/messages/list/1 will return second 10 messages
etc

- GET method for getting single message by unique identifier
e.g.
/api/messages/single/123

- POST method for creating a new message

### Documentation
[Documentation](https://documenter.getpostman.com/view/14768889/TzJrCKXv) generated by Postman.



### Start API
cd chat_room

sudo docker-compose build

sudo docker-compose run web python manage.py makemigrations

sudo docker-compose run web python manage.py migrate

sudo docker-compose up
