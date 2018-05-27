# helpers.py module
import logging, random

def fail(r):
	try:
		r = float(r)
	except Exception:
		logging.debug("Error casting fail() argument {} to float".format(r))
		return False

	x = random.random()
	logging.info("Fail: {} < {} : ".format(x, r))
	return x < r

def set_headers(headers):
	h = {}
	if headers.get('fail'):
		h['fail'] = headers['fail']
	return h
