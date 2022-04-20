import logging

from app import db
from app.db.models import User, Song

def test_adding_user(application):
    log = logging.getLogger("myApp")
    with application.app_context():
        #check that you don't have any users or songs
        assert db.session.query(User).count() == 0
        assert db.session.query(Song).count() == 0
        #showing how to add a record
        #create a record
        user = User('keith@webizly.com', 'testtest')
        #add it to get ready to be committed

        db.session.add(user)
        #call the commit
        db.session.commit()
        #assert that we now have a new user
        assert db.session.query(User).count() == 1
        #finding one user record by email
        user = User.query.filter_by(email='keith@webizly.com').first()
        #asserting that the user retrieved is correct
        assert user.email == 'keith@webizly.com'
        #this is how you get a related record ready for insert
        user.songs= [Song("MyTitle","Joe Joe"),Song("Terrible Song","Joe Joe")]
        db.session.commit()
        for song in user.songs:
            log.info(song.title)
        assert db.session.query(Song).count() == 2
        song1 = Song.query.filter_by(title='MyTitle').first()
        assert song1.title == "MyTitle"
        #changing the title of the song
        song1.title = "spam"
        #saving the new title of the song
        db.session.commit()
        song2 = Song.query.filter_by(title='spam').first()
        assert song2.title == "spam"
        #checking cascade delete
        db.session.delete(user)
        assert db.session.query(User).count() == 0
        assert db.session.query(Song).count() == 0
