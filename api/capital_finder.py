from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests
 
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
       api_URL = f'https://restcountries.com/v3.1/name/{country}'
       res = requests.get(api_URL)
       data = res.json()
       capital = data[0]["name"][0]
       if country == str(data[0]["name"]["common"]).lower() and capital == str(data[0]["capital"][0]).lower():
          respons = "Yes, "
       else:
          respons = "No, "
          country = data[0]["name"]["common"]
          capital = data[0]["capital"][0]
       respons += f"The capital of {country} is {capital}."
    elif my_dict.get('country'):
        respons = f"The capital of {country} is {str_test}."
    elif my_dict.get('capital'):
        respons = f"{capital} is the capital of {str_test}."
    
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()

    self.wfile.write(respons.encode())
    return