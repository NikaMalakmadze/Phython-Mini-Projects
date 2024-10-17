#importing libraries

import folium                       #folium for creating world map        
import folium.map
import folium.vector_layers             #for adding markers on map
import requests                             #requests to get site source
from bs4 import BeautifulSoup                   #bs4 to work with site data
import pandas                                       #pandas to work with csv files

def generate_color():                               #function for generating colors
    if dict[cname] < 1000:
        return "white"
    if dict[cname] < 10000:
        return "blue"
    if dict[cname] < 50000:
        return "green"
    if dict[cname] < 100000:
        return "yellow"
    if dict[cname] < 1000000:
        return "orange"
    if dict[cname] > 1000000:
        return "red"

def generate_radius():                              #function to generate radius of markers for each country
    return dict[cname]**0.21


url = "https://www.worldometers.info/coronavirus/"          #url of worldometer

r = requests.get(url)                                           #sending a request to the site

soup = BeautifulSoup(r.content , features = "html.parser")            #bs4 working as a html parser | P.S getting only html code of site

data = soup.find('tbody')                                                  #finding table of countries and number of infected people

dict = {}

#getting number of infected people and storing it in dictionary
#key --- country name ; value --- number of infected people

for items in data:
    row_cases = items.find_all_next("td")[2].text                                             
    dict[items.find_all_next("td")[1].text] = int(row_cases.replace("," , ""))


#getting coordinates of each country
countries_data = pandas.read_csv("./Covid Map/countries.csv")                   #working with csv file using pandas

#getting the country name, it's latitude and longitude
latitude = list(countries_data["latitude"])
longitude = list(countries_data["longitude"])
country_name = list(countries_data["name"])


#creating world map and adjusting it using folium
map = folium.Map(                                                                                               
     
    location= [45.65 , 34.76] ,                     #some random start location
    #setting map style and zoom parameters
    tiles = "https://server.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer/tile/{z}/{y}/{x}.png" ,        
    attr = "Tiles &copy; Esri &mdash; National Geographic, Esri, DeLorme, NAVTEQ, UNEP-WCMC, USGS, NASA, ESA, METI, NRCAN, GEBCO, NOAA, iPC" ,
    min_zoom = 2 , 
    zoom_start = 5

)

marker_group = folium.FeatureGroup(name = "Countries")                     #creating group of markers

#iterating over each country
for lat, lon, cname in zip(latitude , longitude , country_name):

    if cname in dict.keys():                                        #check if country is in dictionary

        try:
            #adding info markers for each country in the group of markers
            marker_group.add_child(folium.vector_layers.CircleMarker(location = [lat , lon] ,               
                                                                 radius = generate_radius() , 
                                                                 fill_color = generate_color() ,
                                                                 color = "#666666" ,
                                                                 fill_opacity = 0.6 ,
                                                                 popup = cname + ":" + "\n" + str(dict[cname])))
        except:
            pass

map.add_child(marker_group)                                         #adding group of markers on the map

map.save("./Covid Map/CovidMap.html")                               #saving map
