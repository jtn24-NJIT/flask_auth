"""
This file is to test the users table
"""
import logging
from app import db
from app.db.models import User, Song

def test_adding_user(application):
    """ Adding a test user to db """
    log = logging.getLogger("myApp")
    with application.app_context():
        assert db.session.query(User).count() == 0
        assert db.session.query(Song).count() == 0
        #showing how to add a record
        #create a record
        user = User('keith@webizly.com', 'testtest', 1)
        #add it to get ready to be committed
        db.session.add(user)
        #finding one user record by email
        user = User.query.filter_by(email='keith@webizly.com').first()
        log.info(user)
        #asserting that the user retrieved is correct
        assert user.email == 'keith@webizly.com'
        #this is how you get a related record ready for insert
        user.songs= [Song("test","smap", 2000, "Random Genre1"),
                     Song("test2","te", 2014, "Testing Music")]
        #commit is what saves the songs
        db.session.commit()
        assert db.session.query(Song).count() == 2
        song1 = Song.query.filter_by(title='test').first()
        assert song1.title == "test"
        #changing the title of the song
        song1.title = "SuperSongTitle"
        #saving the new title of the song
        db.session.commit()
        song2 = Song.query.filter_by(title='SuperSongTitle').first()
        assert song2.title == "SuperSongTitle"
        #checking cascade delete
        db.session.delete(user)
        assert db.session.query(User).count() == 0
        assert db.session.query(Song).count() == 2
