from http.server import BaseHTTPRequestHandler
from urllib import parse
 
class handler(BaseHTTPRequestHandler):
 
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    my_URL_path = self.path
    my_URL_components = parse.urlsplit(my_URL_path)
    print(my_URL_components)
    query_list = parse.parse_qsl(my_URL_components.query)
    my_dict = dict(query_list)
    if my_dict.get('country'):
        country= my_dict.get('country')
    elif my_dict.get('capital'):
        capital =  my_dict.get('capital')
    
    
    respons = f"The capital of {country} is {capital}."
    self.wfile.write(respons.encode())
    return