from google.appengine.api import mail
from google.appengine.api import users
from google.appengine.api import capabilities

class Mailer():

	@staticmethod
	def mail(self):
		self.response.headers['Content-Type'] = 'text/plain'
		sender_address = "luizrogeriocn@gmail.com"          
		subject = "Snack Bar"
		body = "Hello, something is happenning at your SnackBar! :D"

		if capabilities.CapabilitySet('mail').is_enabled():
			mail.send_mail(sender_address, sender_address, subject, body)
			
		else:
			self.response.write('We are sorry, but the service is unavailable')