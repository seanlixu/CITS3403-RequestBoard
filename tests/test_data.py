from app import db
from app.models import *
from werkzeug.security import generate_password_hash


john = User(username='John', email='john@john.com', password=generate_password_hash('Password1'))
jane = User(username='Jane', email='jane@jane.com', password=generate_password_hash('Password2'))
bob = User(username='Bobby', email='bob@bob.com', password=generate_password_hash('Password3'))
alice = User(username='Alice', email='alice@alice.com', password=generate_password_hash('Password4'))
charlie = User(username='Charlie', email='charlie@charlie.com', password=generate_password_hash('Password5'))
dave = User(username='Dave', email='dave@dave.com', password=generate_password_hash('Password6'))

post1 = Post(title='John post 1', content='Iamjohn', author=john)
post2 = Post(title='John post 2', content='Iamjohn', author=john)
post3 = Post(title='Jane post 1', content='Iamjane', author=jane)
post4 = Post(title='Charlie post 1', content='Iamcharlie', author=charlie)
post5 = Post(title='Dave post 1', content='Iamdave', author=dave)

post1.assigned = True
post1.assigned_user = bob

post3.assigned = True
post3.assigned_user = alice

post4.assigned = True
post4.assigned_user = dave

post5.assigned = True
post5.assigned_user = charlie

db.session.add_all([john, jane, bob, alice, charlie, dave, post1, post2, post3, post4, post5])
db.session.commit()

