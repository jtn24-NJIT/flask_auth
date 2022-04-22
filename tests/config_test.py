def test_development_config(application):
    application.config.from_object('app.config.DevelopmentConfig')
    assert application.config['DEBUG']
    assert not application.config['TESTING']
    # Use for github
    # assert application.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:////home/runner/work/flask_auth/flask_auth/database/db.sqlite'
    # Use for local/pycharm test
    assert application.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:////home/myuser/database/db.sqlite'


def test_testing_config(application):
    application.config.from_object('app.config.TestingConfig')
    assert application.config['DEBUG']
    assert application.config['TESTING']
    assert not application.config['PRESERVE_CONTEXT_ON_EXCEPTION']
    assert application.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///'

def test_production_config(application):
    application.config.from_object('app.config.ProductionConfig')
    assert not application.config['DEBUG']
    assert not application.config['TESTING']
    # Use for github
    # assert application.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:////home/runner/work/flask_auth/flask_auth/database/db.sqlite'
    # Use for local/pycharm test
    assert application.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:////home/myuser/database/db.sqlite'