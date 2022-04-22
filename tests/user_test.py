import logging

from app import db
from app.db.models import User, Song

def test_adding_user(application, add_user):
    log = logging.getLogger("myApp")
    with application.app_context():
        assert db.session.query(User).count() == 1
        assert db.session.query(Song).count() == 0
        #showing how to add a record
        #create a record
        user = User('jtn24@njit.edu', 'Admin@admin')
        #add it to get ready to be committed
        db.session.add(user)
        #call the commit
        db.session.commit()
        #assert that we now have a new user
        assert db.session.query(User).count() == 2
        #finding one user record by email
        user = User.query.filter_by(email='jtn24@njit.edu').first()
        log.info(user)
        #asserting that the user retrieved is correct
        assert user.email == 'jtn24@njit.edu'
        #this is how you get a related record ready for insert
        user.songs= [Song("SomeSong"),Song("ArtistName")]
        #commit is what saves the songs
        db.session.commit()
        assert db.session.query(Song).count() == 2
        song1 = Song.query.filter_by(title='SomeSong').first()
        assert song1.title == "SomeSong"
        #changing the title of the song
        song1.title = "RandomSong2"
        #saving the new title of the song
        db.session.commit()
        song2 = Song.query.filter_by(title='RandomSong2').first()
        assert song2.title == "RandomSong2"
        #checking cascade delete
        """
        db.session.delete(user)
        assert db.session.query(User).count() == 1
        assert db.session.query(Song).count() == 0
        """