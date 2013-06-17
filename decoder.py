import webapp2

class Decoder():

	@staticmethod
	def decode(s):
    	vector = s.split("&")
		params = {}

    	for v in vector:
			aux = v.split("=")
			params[aux[0]] = aux[1]

		return params