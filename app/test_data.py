from app import db
from app.models import *


john = User(username='John', email='john@john.com', password='Password1')
jane = User(username='Jane', email='jane@jane.com', password='Password2')
bob = User(username='Bob', email='bob@bob.com', password='Password3')
alice = User(username='Alice', email='alice@alice.com', password='Password4')

post1 = Post(title='John post 1', content='Iamjohn', author=john)
post2 = Post(title='John post 2', content='Iamjohn', author=john)
post3 = Post(title='Jane post 1', content='Iamjane', author=jane)

db.session.add_all([john, jane, bob, alice, post1, post2, post3])
db.session.commit()