from google.appengine.ext import db

from food import Food

class SnackBar:

  @staticmethod 
  def add_food(self, b_name, b_quantity):

    b = Food(name= b_name, quantity= int(b_quantity))

    self.response.write("> A quantidade de " + b.name +  " eh: " + str(b.quantity))

    b.put()

  @staticmethod 
  def get_foods(self):
    foods = db.GqlQuery("SELECT * FROM Food")

    for b in foods:
      self.response.write("<br /> > A quantidade de " + b.name +  " eh: " + str(b.quantity))

  @staticmethod
  def sell_food(self, food_name, quantity):
    foods = db.GqlQuery("SELECT * FROM Food")

    for b in foods:
      b.quantity = int( int(b.quantity) - int(quantity) )
      b.put()
      self.response.write("> A quantidade de " + b.name +  " eh: " + str(b.quantity))

  @staticmethod
  def delete_all(self):
    self.response.write("> Voce apagou o banco!")
    foods = db.GqlQuery("SELECT * FROM Food")
    for b in foods:
      b.delete()