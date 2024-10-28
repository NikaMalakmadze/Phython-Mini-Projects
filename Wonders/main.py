#importing libraries
import folium
import folium.map
import folium.features
import folium.vector_layers
import pandas
import json

border_style = {                            #adjusting border style of 7 wonder countries
    'color' : '#EFEFE8FF' ,                   #border color
    'weight' : '5' ,                            #size of border line
    'opacity' : '1',                                #opacity
    'fillColor' : '#F7B32BFF',                          #color of background
    'fillOpacity' : '0.7'                                   #BackGround Opacity
}

else_border_style = {                       #adjusting border style of else countries
    'color' : '#0A5E2AFF' ,                   #border color
    'weight' : '5' ,                            #size of border line
    'opacity' : '1',                                #opacity
    'fillColor' : '#6DAC4FFF',                          #color of background
    'fillOpacity' : '0.7'                                   #BackGround Opacity
}

Data = pandas.read_csv("./Wonders/Coordinates.csv")                     #reading coordinates of wonders with pandas

Name = list(Data["name"])                                               #getting name of wonder
Latitude = list(Data["latitude"])                                       #getting wonder's Latitude
Longitude = list(Data["longitude"])                                     #getting wonder's Longitude
Images= list(Data["images"])                                            #getting path to wonder's icon images

with open("Wonders/world-countries.json") as handle:                    #opening json file with border lines of all the countries
    country_geo = json.loads(handle.read())                                 #storing everything in variable

Country_Names = ["Jordan", "China", "Mexico", "Peru", "Brazil", "Italy", "India"]       #list of countries i need

Country_Geo_Json = []                           
Else_Countries_Json = []

for i in country_geo["features"]:                                   #finding borders of countries that i need
    if i["properties"]["name"] in Country_Names:                    
        Country_Geo_Json.append(i)                                  #storing it in variable
    else:
        Else_Countries_Json.append(i)                               #storing else countries in other variable

#creating map and setting it styles and zoom parameters
map = folium.Map(
        location= [22.268764039073968 , 5.097656250000001] ,                     #some random start location
        #setting map style and zoom parameters
        tiles = "https://watercolormaps.collection.cooperhewitt.org/tile/watercolor/{z}/{x}/{y}.jpg" ,        
        attr = "Tiles &copy; Esri &mdash; National Geographic, Esri, DeLorme, NAVTEQ, UNEP-WCMC, USGS, NASA, ESA, METI, NRCAN, GEBCO, NOAA, iPC" ,
        min_zoom = 3 ,
        max_zoom = 13 , 
        zoom_start = 3,
        max_lon= 240,
        max_bounds=True
)

else_json_group = folium.FeatureGroup(name="Else_Country_Json")             #creating group for borders of else countries

for e_c_json in Else_Countries_Json:
    else_json_group.add_child(folium.GeoJson(e_c_json,                                  #data of else countries borders
                                             name = e_c_json["properties"]["name"],         #name of else country
                                             style_function=lambda x:else_border_style))    #giving it style

json_group = folium.FeatureGroup(name="Country_Json")                   #creating group for borders of countries that i need

for c_json in Country_Geo_Json:
    json_group.add_child(folium.GeoJson(c_json,                                 #data of countries borders that i need
                                        name = c_json["properties"]["name"],        #name of country that i need
                                        style_function=lambda x:border_style))      #giving it style

marker_group = folium.FeatureGroup(name="Wonders")                          #creating group for borders of countries that i need

#adding markers of 7 new wonders on the map
for nm , lat , lon , img, c_name in zip(Name, Latitude , Longitude, Images, Country_Names):
    marker_group.add_child(folium.Marker(
            location = [lat , lon] ,                                    #location of marker       
            popup = c_name + "\n" + nm ,                                    #popup(text) of marker
            icon= folium.features.CustomIcon(img, icon_size=(60,60))))          #setting icon of marker

#adding all the groups on the map    
map.add_child(marker_group)                                             

map.add_child(else_json_group)

map.add_child(json_group)

#saving map
map.save("./Wonders/Wonder.html")
