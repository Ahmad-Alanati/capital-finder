from http.server import BaseHTTPRequestHandler
from urllib import parse
 
class handler(BaseHTTPRequestHandler):
 
  def do_GET(self):
    my_URL_path = self.path
    my_URL_components = parse.urlsplit(my_URL_path)
    query_list = parse.parse_qsl(my_URL_components.query)
    my_dict = dict(query_list)

    country = my_dict.get('country')
    capital = my_dict.get('capital')
    str_test = "hello"
    
    if country and capital:
       respons = f"The capital of {country} is {capital}."
    elif my_dict.get('country'):
        respons = f"The capital of {country} is {str_test}."
    elif my_dict.get('capital'):
        respons = f"{capital} is the capital of {str_test}."
    
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()

    respons = f"The capital of {country} is {capital}."
    self.wfile.write(respons.encode())
    return