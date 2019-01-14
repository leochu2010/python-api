# Installation
`pip3 install gunicorn flask`

# Run web service
## Run flask API with command
`FLASK_APP=app.py flask run`

## Run flask with gunicon
`gunicorn --workers=2 app:app -b localhost:8000`

# APIs
## hello world
GET api/hello
## text rank
POST api/textrank with parameter text

