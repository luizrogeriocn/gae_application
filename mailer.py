from google.appengine.api import mail
from google.appengine.api import users

class Mailer():

	@staticmethod
	def mail(self, user):
		#mandando email para usuario logado
		self.response.headers['Content-Type'] = 'text/plain'
		sender_address = "luizrogeriocn@gmail.com"
		user_address = user.email()           
		subject = "Snack Bar"
		body = "Hello, you just bought a snack at my Snack Bar!"
		mail.send_mail(sender_address, user_address, subject, body)
		self.response.write('We just sent an e-mail to '+ user_address)