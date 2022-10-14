import pandas as pd
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="myApp")

df2 = pd.DataFrame({'Location':
            ['2094 Valentine Avenue,Bronx,NY,10457',
             '1123 East Tremont Avenue,Bronx,NY,10460',
             '412 Macon Street,Brooklyn,NY,11233']})

df2[['location_lat', 'location_long']] = df2['Location'].apply(
    geolocator.geocode).apply(lambda x: pd.Series(
        [x.latitude, x.longitude], index=['location_lat', 'location_long']))