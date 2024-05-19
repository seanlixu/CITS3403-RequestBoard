import unittest
from flask import current_app
from app import create_app, db
from app.config import TestConfig
from app.models import User
from werkzeug.security import generate_password_hash



class BasicTests(unittest.TestCase):

    def setUp(self):
        testApp = create_app(TestConfig)
        self.app_context = testApp.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)
        
    def test_user_creation(self):
        testUser = User(username='test', email='test@test.com', password=generate_password_hash('Testing123'))
        db.session.add(testUser)
        db.session.commit()
        self.assertIsNotNone(User.query.filter_by(username='test').first())
        db.session.delete(testUser)
        db.session.commit()
        self.assertIsNone(User.query.filter_by(username='test').first())
        
    def test_user_creation_duplicate(self):
        from sqlalchemy.exc import IntegrityError
        testUser1 = User(username='test', email='test@test.com', password=generate_password_hash('Testing123'))
        db.session.add(testUser1)
        db.session.commit()
        self.assertIsNotNone(User.query.filter_by(username='test').first())
        testUser2 = User(username='test', email='test2@test.com' , password=generate_password_hash('Testing123'))
        db.session.add(testUser2)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
        self.assertIsNone(User.query.filter_by(username='test2').first())
        
        
        
    def test_password_hashing(self):
        testUser = User(username='test', email='test@test.com', password=generate_password_hash('Testing123'))
        db.session.add(testUser)
        db.session.commit()
        self.assertFalse(testUser.check_password('testing123'))
        self.assertFalse(testUser.check_password('Testing1234'))
        self.assertTrue(testUser.check_password('Testing123'))
        db.session.delete(testUser)
        db.session.commit()
        self.assertIsNone(User.query.filter_by(username='test').first())
        
        
    
        
   
        
        
        