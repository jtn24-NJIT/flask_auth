Hello, my name is Jake T. Nhan. I am senior student at NJIT, majoring in Computer Science for a Bachelor's degree. This is the repo for the third project of IS 218, SEC. 004 of Spring 2022. In this project, there is a simple login system that also allows for uploading of csv music files.

# Project Setup

[![Production Workflow 1](https://github.com/jtn24-NJIT/flask_auth/actions/workflows/prod.yml/badge.svg?branch=master)](https://github.com/jtn24-NJIT/flask_auth/actions/workflows/prod.yml)

* [Production Deployment](https://jtn24-prod.herokuapp.com/)


[![Development Workflow 3.8](https://github.com/jtn24-NJIT/flask_auth/actions/workflows/dev.yml/badge.svg?branch=master)](https://github.com/jtn24-NJIT/flask_auth/actions/workflows/dev.yml)

* [Developmental Deployment](https://jtn24-dev.herokuapp.com/)


## Setting up CI/CD

The result of this will be that when you create a pull request to merge a branch to master, it will deploy to your
heroku development app/dyno and when you merge or push to master on github, it will deploy the app to the production heroku
app/dyno.

## Running Locally

1. To Build with docker compose:
   docker compose up --build
2. To run tests, Lint, and Coverage report use this command: pytest --pylint --cov

.pylintrc is the config for pylint, .coveragerc is the config for coverage and setup.py is a config file for pytest


### Future Notes and Resources
* https://flask-user.readthedocs.io/en/latest/basic_app.html
* https://hackersandslackers.com/flask-application-factory/
* https://suryasankar.medium.com/a-basic-app-factory-pattern-for-production-ready-websites-using-flask-and-sqlalchemy-dbb891cdf69f
* https://develie.hashnode.dev/exploring-flask-sqlalchemy-queries
* https://wtforms.readthedocs.io/en/3.0.x/
* https://bootstrap-flask.readthedocs.io/en/stable/
* https://flask-sqlalchemy.palletsprojects.com/en/2.x/
