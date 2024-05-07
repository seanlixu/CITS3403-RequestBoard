from app import db
# from sqlalchemy.orm import relationship


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    ratings = db.Column(db.Float(5.0), default=0.0)
    ratings_count = db.Column(db.Integer(), default=0)

    # posts = relationship('Post', backref='author', lazy='dyanmic')


    
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
    
        