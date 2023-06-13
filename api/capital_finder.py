from http.server import BaseHTTPRequestHandler
from urllib import parse
 
class handler(BaseHTTPRequestHandler):
 
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    my_URL_path = self.path
    my_URL_query = parse.urlsplit(my_URL_path).query

    country= "Chile"
    capital =  "Santiago"
    respons = str(my_URL_query)
    self.wfile.write(respons.encode())
    return