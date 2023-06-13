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
    respons = f"The capital of {country} is {capital}."
    self.wfile.write(my_URL_query.encode())
    return