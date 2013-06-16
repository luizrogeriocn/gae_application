from google.appengine.ext import db
from google.appengine.api import users

class SnackBar(db.Model):
	name = db.StringProperty(required=True)
	resources = db.StringProperty(required=True)
	email = db.StringProperty()


e = SnackBar(name="Cantina do Setor 3", resources="10", email="luizrogeriocn@gmail.com")
e.put()