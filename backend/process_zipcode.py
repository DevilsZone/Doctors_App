import requests
import pgeocode
from .fake_user_agent import give_fake_headers
MAX_THREADS = 30

def download_data(zip_code, radius):
    nomi = pgeocode.Nominatim('us')
    api_key = "ade07974-778f-8441-a98a-2888b073fa32"
    zip_code = str(zip_code)
    xy = nomi.query_postal_code(zip_code)
    lat = str(xy['latitude'])
    lon = str(xy['longitude'])
    url = "https://galdermahcprestservice.intouchsol.net/api/PhysicianLocator/Search?apikey={}&latitude={" \
          "}&longitude={}&skip=0&take=100&CarriesDysport=true&radius={" \
          "}&specialty=&doctorName=&sortBy=default&password=&input-cityStateOrZip={}".format(api_key, lat, lon, radius,
                                                                                             zip_code)
    session = requests.session()
    r = session.get(url, headers=give_fake_headers())
    x = r.json()
    n_results = x['TotalCount']
    if n_results > 0:
        return x['Results']
    else:
        return None
