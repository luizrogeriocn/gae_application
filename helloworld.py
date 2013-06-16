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

class MainPage(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()
        if user:

            Register.register(self)

            Mailer.mail(self, user)

        else:
            self.redirect(users.create_login_url(self.request.uri))





application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
