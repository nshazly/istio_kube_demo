import os, logging
import datetime as dt

from flask import Flask, Response, request
from requests import get
from helpers import fail, get_forward_headers

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

BACKEND_SERVICE = os.getenv("BACKEND_SERVICE")

@app.route("/time")
def get_time():
	t = get(BACKEND_SERVICE + "/time", headers=get_forward_headers(request))
	f = request.headers.get('fail')

	if t.ok:
		if fail(f):
			return "Middleware service unavailable", 503
		else:
			return "Middleware -> {}".format(t.text)
	else:
		logging.error(t.status_code, t.text)
		return "<p>Error {} : {}</p>".format(t.status_code, t.text)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=os.getenv("PORT", 8080))
	
