from google.appengine.api import users
from google.appengine.api import mail
from google.appengine.api import capabilities
from google.appengine.api import urlfetch

from register import Register
from mailer import Mailer
import urllib

import cgi

import webapp2

class MainPage(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()
        if user:

            Mailer.mail(self, user)

            Register.register(self)

        else:
            self.redirect(users.create_login_url(self.request.uri))





application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
