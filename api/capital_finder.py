from http.server import BaseHTTPRequestHandler
from urllib import parse
 
class handler(BaseHTTPRequestHandler):
 
  def do_GET(self):
    url_path = self.path
    # print(1111,url_path)
    url_components = parse.urlsplit(url_path)
    # print(2222,url_components)
    query_list = parse.parse_qsl(url_components.query)
    # print(33333,query_list)
    my_dict = dict(query_list)
    # print(44444,my_dict)
    # name = my_dict['name']
    name = my_dict.get('name')

    if name :
      message = f'welcome {name}'
    else: 
        message = f'welcome stranger'
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()

    self.wfile.write(message.encode())
    return