import os, logging
import datetime as dt

from flask import Flask, Response, request
from requests import get
from helpers import fail

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

@app.route("/")
def hello():
	return "<h3>Hello<h3>"

@app.route("/today")
def getTime():
	t = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S %z")
	resp = Response("<p>Today's date is {}".format(t))
	f = request.headers.get("fail")

	if fail(f):
		return 503, "Backend service unavailable"
	else:
		return resp

@app.route("/time")
def get_time():
	f = request.headers.get("fail")
	t = get("http://time.jsontest.com")

	if t.ok:
		if fail(f):
			return "Backend service unavailable", 503
		else:
			return "Backend response --> {}".format(t.text)
	else:
		logging.error(t.status_code, t.text)
		return "<p>Error {} : </p>".format(t.status_code, t.text)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=os.getenv("PORT", 8080))
	
