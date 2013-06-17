from google.appengine.ext import db

class Food(db.Model):

  name = db.StringProperty(required=True)
  quantity = db.IntegerProperty(required=True)


  def list_foods(self):
    books = db.GqlQuery("SELECT * FROM Food")

    for e in books:
      self.response.write(e.name + e.quantity)