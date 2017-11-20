
# import socket

from BaseHTTPServer import BaseHTTPRequestHandler
from StringIO import StringIO
from django.http import HttpResponse , HttpResponseNotFound , Http404

import op_mysql as db
import op_token as token
import re


class HTTPRequest(BaseHTTPRequestHandler):
    def __init__(self, request_text):
        self.rfile = StringIO(request_text)
        self.raw_requestline = self.rfile.readline()
        self.error_code = self.error_message = None
        self.parse_request()

    def send_error(self, code, message):
        self.error_code = code
        self.error_message = message

def string_parser(string,delimiter):
    _SPLITS = re.split(delimiter,string)
    return _SPLITS

ARR_INSERT=[1,1,1,1]
ARR_S_D=[1,1]

def url_pars(url):
    _SPLITS = re.split('/',url)
    if _SPLITS[1] == "insert" :
        if token.validate_token(_SPLITS[2]) == "success" :
            db.insert_peers(str(_SPLITS[3]),str(_SPLITS[4]),str(string_parser(_SPLITS[5],"'")[0]))
            return "success"
        else:  
            return "failed"
    elif _SPLITS[1] == "delete" :
        if token.validate_token(_SPLITS[2]) == "success" :
            db.delete_peers(str(string_parser(_SPLITS[3],"'")[0]))
            return "success"
        else:  
            return "failed"

def insert(request):
        result=url_pars(str(request))
        if result == "success":
            return HttpResponse(status=200)
        elif result == "failed":
            return HttpResponse(status=404)

def delete(request):
        result=url_pars(str(request))
        if result == "success":
            return HttpResponse(status=200)
        elif result == "failed":
            return HttpResponse(status=404)