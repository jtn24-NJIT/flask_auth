""" Testing the user table of adding a default user """
import logging

from app import db
from app.db.models import User, Song

def test_adding_user(application):
    """Getting a loger and testing adding a user with an example music csv file"""
    log = logging.getLogger("myApp")
    with application.app_context():
        #check that you don't have any users or songs
        assert db.session.query(User).count() == 0
        assert db.session.query(Song).count() == 0
        #showing how to add a record
        #create a record
        user = User('jtn24@njit.edu', 'Admin@admin')
        #add it to get ready to be committed

        db.session.add(user)
        #call the commit
        db.session.commit()
        #assert that we now have a new user
        assert db.session.query(User).count() == 1
        #finding one user record by email
        user = User.query.filter_by(email='jtn24@njit.edu').first()
        #asserting that the user retrieved is correct
        assert user.email == 'jtn24@njit.edu'
        #this is how you get a related record ready for insert
        user.songs= [Song("ExampleTitle","Johnny Green"),Song("Some Random Song","Johnny Green")]
        db.session.commit()
        for song in user.songs:
            log.info(song.title)
        assert db.session.query(Song).count() == 2
        song1 = Song.query.filter_by(title='ExampleTitle').first()
        assert song1.title == "ExampleTitle"
        #changing the title of the song
        song1.title = "Other Song"
        #saving the new title of the song
        db.session.commit()
        song2 = Song.query.filter_by(title='Other Song').first()
        assert song2.title == "Other Song"
        #checking cascade delete
        db.session.delete(user)
        assert db.session.query(User).count() == 0
        assert db.session.query(Song).count() == 0
