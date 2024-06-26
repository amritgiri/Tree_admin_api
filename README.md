## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/amritgiri/Tree_admin_api.git
$ cd sample-django-app
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python3 -m venv .venv
$ source .venv/bin/activate
```

Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment.

Once `pip` has finished downloading the dependencies:
```sh
(venv)$ cd project
(venv)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.