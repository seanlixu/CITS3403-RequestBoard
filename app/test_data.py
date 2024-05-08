from app import db
from app.models import *
from werkzeug.security import generate_password_hash


john = User(username='John', email='john@john.com', password=generate_password_hash('Password1'))
jane = User(username='Jane', email='jane@jane.com', password=generate_password_hash('Password2'))
bob = User(username='Bob', email='bob@bob.com', password=generate_password_hash('Password3'))
alice = User(username='Alice', email='alice@alice.com', password=generate_password_hash('Password4'))

post1 = Post(title='John post 1', content='Iamjohn', author=john)
post2 = Post(title='John post 2', content='Iamjohn', author=john)
post3 = Post(title='Jane post 1', content='Iamjane', author=jane)

db.session.add_all([john, jane, bob, alice, post1, post2, post3])
db.session.commit()