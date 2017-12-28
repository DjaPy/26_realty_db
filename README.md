# Real Estate Site

This is a test version of real estate application.
The application receives the data in json format. Writes data to SQLite database

# Run locally

Use Venv or virtualenv for insulation project. Virtualenv example:

```
$ python virtualevn myenv
$ source myenv/bin/activate
```

Install requirements:

```
pip install -r requirements.txt
```

#How to use

Run to create (if it is not created already) and update database with argument -u <pathway to json>
For example:
```
python realty_app.py -u example.json
```
Next, run flask server:
```
python3 server.py
```
And go to site: http://127.0.0.1:5000/

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)


