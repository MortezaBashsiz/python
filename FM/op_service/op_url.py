from BaseHTTPServer import BaseHTTPRequestHandler
from StringIO import StringIO
from django.http import HttpResponse

import op_mysql as db
import op_token as token
import re
import op_logger as log

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

def url_pars(url):
    _SPLITS = re.split('/',url)
    if _SPLITS[1] == "insert" :
        if token.validate_token(_SPLITS[2]) == 200 :
            return db.insert_peers(str(_SPLITS[3]),str(_SPLITS[4]),str(string_parser(_SPLITS[5],"'")[0]))
        else:  
            return 554
    elif _SPLITS[1] == "delete" :
        if token.validate_token(_SPLITS[2]) == 200 :
            return db.delete_peers(str(string_parser(_SPLITS[3],"'")[0]))
        else:  
            return 554

def insert(request):
        result=url_pars(str(request))
        return HttpResponse(status=result)

def delete(request):
        result=url_pars(str(request))
        return HttpResponse(status=result)