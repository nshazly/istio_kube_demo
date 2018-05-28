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

def get_forward_headers(request):
    headers = {}

    user_cookie = request.cookies.get("user")
    if user_cookie:
        headers['Cookie'] = 'user=' + user_cookie

    incoming_headers = [ 'x-request-id',
                         'x-b3-traceid',
                         'x-b3-spanid',
                         'x-b3-parentspanid',
                         'x-b3-sampled',
                         'x-b3-flags',
                         'x-ot-span-context',
                         'fail'
    ]

    for ihdr in incoming_headers:
        val = request.headers.get(ihdr)
        if val is not None:
            headers[ihdr] = val
            #print "incoming: "+ihdr+":"+val

    return headers
