from google.appengine.api import users
from google.appengine.api import mail
from google.appengine.api import capabilities
from google.appengine.api import urlfetch

from snackbar import SnackBar
from register import Register
from mailer import Mailer

import urllib
import cgi
import webapp2

def decode(s):
    vector = s.split("&")
    params = {}

    for v in vector:
        aux = v.split("=")
        params[aux[0]] = aux[1]

    return params


class MainPage(webapp2.RequestHandler):

    def get(self):
        Register.register(self)
        SnackBar.get_foods(self)

    def post(self):
        Mailer.mail(self)
        params = decode(self.request.body)

        if(params ["request"] == "buy"):
            SnackBar.sell_food(self, params["food_name"], params["quantity"])
        else:
            if(params ["request"] == "add"):
                SnackBar.add_food(self, params["food_name"], params["quantity"])
            else:
                self.response.write('nao sei que porra eh essa :P')

    def put(self):
        SnackBar.delete_all(self)

       

application = webapp2.WSGIApplication([
    ('/roger-pd-app/snackbar', MainPage),
], debug=True)
