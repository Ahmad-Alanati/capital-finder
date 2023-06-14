from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests
 
class handler(BaseHTTPRequestHandler):

  def get_capital(self,country):
    api_URL = f'https://restcountries.com/v3.1/name/{country}'
    res = requests.get(api_URL)
    data = res.json()
    return str(data[0]["capital"][0]).lower()
  
  def get_country(self,capital):
    api_URL = f'https://restcountries.com/v3.1/capital/{capital}'
    res = requests.get(api_URL)
    data = res.json()
    return str(data[0]["name"]["common"]).lower()
 
  def do_GET(self):
    my_URL_path = self.path
    my_URL_components = parse.urlsplit(my_URL_path)
    query_list = parse.parse_qsl(my_URL_components.query)
    my_dict = dict(query_list)

    country = my_dict.get('country')
    capital = my_dict.get('capital')
    
    if country and capital:
      respons_capital = self.get_capital(country)
      respons_country = self.get_country(capital)
      if country == respons_country and capital == respons_capital:
        respons = "Yes, "
      else:
        respons = "No, "
      respons += f"The capital of {respons_country} is {respons_capital}."
    elif my_dict.get('country'):
      respons_capital = self.get_capital(country)
      respons = f"The capital of {country} is {respons_capital}."
    elif my_dict.get('capital'):
      respons_country = self.get_country(capital)
      respons = f"{capital} is the capital of {respons_country}."
    
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()

    self.wfile.write(respons.encode())
    return