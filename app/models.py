from app import db
# from sqlalchemy.orm import relationship


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    ratings = db.Column(db.Float(5.0), default=0.0)
    ratings_count = db.Column(db.Integer(), default=0)
    # author = db.relationship('Post', backref='posts', lazy='dyanmic')

    def is_authenticated(self):
        return self.is_authenticated
    
    def is_active(self):
        return self.is_active

    def get_id(self):
        return str(self.id)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(255))

    
class Response:
    def __init__(self, status: str, message: str):
        self.status = status
        self.message = message
    
    def to_dictionary(self):
        return {
            'status': self.status,
            'message': self.message,
        }

class SuccessResponse(Response):
    def __init__(self, message: str = 'Success'):
        super().__init__('success', message)

class ErrorResponse(Response):
    def __init__(self, message: str = 'Error'):
        super().__init__('error', message)
    