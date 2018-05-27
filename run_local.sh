#!/bin/bash

PORT=8082 python backend.py &
PORT=8081 BACKEND_SERVICE=http://localhost:8082 python middleware.py &
PORT=8080 MIDDLEWARE_SERVICE=http://localhost:8081 python frontend.py &

if [ -t 0 ]; then stty -echo -icanon -icrnl time 0 min 0; fi

count=0
keypress=''
echo Press 'q' to close all apps
while [ "x$keypress" != "xq" ]; do
  keypress="`cat -v`"
done

if [ -t 0 ]; then stty sane; fi

echo "You pressed '$keypress'"
echo "Closing all apps."
trap 'kill $(jobs -p)' EXIT

exit 0