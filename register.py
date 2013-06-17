from google.appengine.api import urlfetch
import urllib

class Register():

	@staticmethod
	def register(self):
		self.response.write('Service Available!')
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