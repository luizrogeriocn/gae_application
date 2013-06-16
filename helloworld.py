from google.appengine.api import users
from google.appengine.api import mail
from google.appengine.api import capabilities
from google.appengine.api import urlfetch

from mailer import Mailer
import urllib

import cgi

import webapp2

class MainPage(webapp2.RequestHandler):

    def register(self):
        #cadastro bolado no lookup
        form_fields = {
        "endpoint": "roger-pd-app.appspot.com",
        "id": "roger-pd-app"
        }

        url = "http://lookuppd.appspot.com/objects/add"
            
        form_data = urllib.urlencode(form_fields)

        result= urlfetch.fetch(url=url,
        payload=form_data,
        method=urlfetch.POST,
        headers={'Content-Type': 'application/x-www-form-urlencoded'})

    def get(self):
        user = users.get_current_user()
        if user:

            Mailer.mail(self, user)

            self.register()

        else:
            self.redirect(users.create_login_url(self.request.uri))





application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
