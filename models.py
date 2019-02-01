from werkzeug.security import generate_password_hash, check_password_hash
from hashlib import md5
from app import db

# ...

class User(UserMixin,db.Model):

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(45), unique = True)
	email = db.Column(db.String(100, unique=True))
	password_hash = db.column(db.String(45))
    # ...
	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)
		
	def avatar(self, size):
		digest = md5(self.email.lower().encode('utf-8')).hexdigest()
		return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
			digest, size)
	def __repr__(self):
		return '<User {}>'.format(self.username)    