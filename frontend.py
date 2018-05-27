import os, logging
import datetime as dt

from flask import Flask, Response, request
from requests import get
from helpers import fail, set_headers

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

MIDDLEWARE_SERVICE = os.getenv("MIDDLEWARE_SERVICE")

@app.route("/")
def hello():
	return "<h3>Hello<h3>"

@app.route("/time")
def get_time():
	h = set_headers(request.headers)
	t = get(MIDDLEWARE_SERVICE + "/time", headers=h)
	f = h.get('fail')

	if t.ok:
		if fail(f):
			return "Frontend service unavailable", 503
		else:
			return "<pre>Frontend --> {}</pre>".format(t.text)
	else:
		logging.error("{} {}".format(t.status_code, t.text))
		return "<p>Error {} : {} </p>".format(t.status_code, t.text)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=os.getenv("PORT", 8080))
	
