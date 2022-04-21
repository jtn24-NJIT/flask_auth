"""
SQL Alchemy database test file
"""

def test_development_config(application):
    """ Assert the application configuration to the DEVELOPMENT (Debug, testing) of SQL lite"""
    application.config.from_object('app.config.DevelopmentConfig')
    assert application.config['DEBUG']
    assert not application.config['TESTING']
    # Use line 10 for github, line 11 for local/pycharm
    #assert application.config['SQLALCHEMY_DATABASE_URI'] ==
    # 'sqlite:////home/runner/work/flask_auth/flask_auth/database/db.sqlite'
    assert application.config['SQLALCHEMY_DATABASE_URI']\
           == 'sqlite:////home/myuser/database/db.sqlite'


def test_testing_config(application):
    """ Assert the application configuration to the development (Debug, testing) of SQL lite,
    but also not preserving on exception"""
    application.config.from_object('app.config.TestingConfig')
    assert application.config['DEBUG']
    assert application.config['TESTING']
    assert not application.config['PRESERVE_CONTEXT_ON_EXCEPTION']
    assert application.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///'

def test_production_config(application):
    """ Assert the application configuration to the PRODUCTION (Debug, testing) of SQL lite,
    but also not preserving on exception"""
    application.config.from_object('app.config.ProductionConfig')
    assert not application.config['DEBUG']
    assert not application.config['TESTING']
    # Use line 26 for github, 27 for local/pycharm
    #assert application.config['SQLALCHEMY_DATABASE_URI'] ==
    # 'sqlite:////home/runner/work/flask_auth/flask_auth/database/db.sqlite'
    assert application.config['SQLALCHEMY_DATABASE_URI'] ==\
           'sqlite:////home/myuser/database/db.sqlite'
