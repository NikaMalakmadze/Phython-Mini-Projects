import folium
import folium.map
import folium.vector_layers
import folium.features
import pandas
import pandas as pd
import json
from Styles import *                    #importing styles from Styles module

#working with csv file using pandas

Data = pandas.read_csv("EducationInGeorgia/Education.csv")

Location = Data["Location"]
School_Number = pd.to_numeric(Data["SchoolNumber"])
Municipality_Name = Data["Name"]
Children = pd.to_numeric(Data["Children"])
Latitudes = Data["Latitude"] 
Longitudes = Data["Longitude"]

#opening JSON file of Georgia SubRegions

with open("EducationInGeorgia/SubRegions_High_Quality.json" , encoding="utf-8") as f:
    Borders_Json = json.loads(f.read())

#Group of borders

Borders_Group = folium.FeatureGroup(name="Borders",
                                    control = False)        #turned control off, so user can't disable borders of Georgia subregions

#adding borders of eaach subregion in borders group

for feature in Borders_Json["features"]:                            #running through all of the features
   municipality_name = feature["properties"]["NAME_2"]                      #getting municipality name
   Borders_Group.add_child(folium.GeoJson(feature,                                  #adding feature
                                          name = "Municipalities",                          
                                          style_function = lambda x:border_style,           #giving style
                                          popup = folium.Popup(municipality_name),          #municipality name as a popup text
                                          highlight_function = hightlight_function          #giving highlight function
))  

range1 = [0, 10, 20, 30, 40, 50, 60, 70, 80, 300]           #custom range for Choropleth1

#Choropleth of Schools number in every SubRegions of Georgia

Choropleth1 = folium.Choropleth(
    geo_data = Borders_Json,                                #JSON Data
    name = "Schools in Georgia",
    data = Data,                                            #CSV Data
    columns = ["Location","SchoolNumber"],                  #assigning data from csv file with principe: | key : value |  
    key_on = "feature.properties.NAME_2",                   #municipality name from GeoJson as a key
    fill_color ="YlGnBu",                                   #brewing colors style                     
    fill_opacity = 1,                                       
    line_opacity = 1,
    line_weight = 3,
    legend_name = "School Number In Georgia",               #name of legend
    highlight = True,                                       #highlight when hower with cursor
    bins = range1,                                              #setting custom range of legend
    smooth_factor = 0.1,                                            #accuracy of lines when you zoom in. less means more accurate
    show = False                                                #don't show this layer when user opens site
)

#adding tooltip(popup message) for this choropleth(Choropleth1)

Choropleth1.geojson.add_child(
    folium.features.GeoJsonTooltip(
        fields=["NAME_0", "NAME_1", "NAME_2"],                #Information i want to get from JSON file |Country, Region, SubRegion|
        aliases=["Country: ","Region: ",'Municipality: '],          #just titles for them
        sticky=False,                                                   #popup will not follow cursor
        labels=True,                                                        #turn popup massage on
        #some minimal style for popup
        style = """                                                               
                    opacity: 0.7;
                    border: none;
                """
    )
)

range2 = [0,2000,10000, 20000, 50000, 80000, 110000, 140000, 170000, 200000,230000]         #custom range for Choropleth2

#Choropleth of students number in every SubRegions of Georgia

Choropleth2 = folium.Choropleth(
    geo_data = Borders_Json,                                    #JSON Data
    name = "Students in Georgia",                               
    data = Data,                                                #CSV Data
    columns = ["Location","Children"],                          #assigning data from csv file with principe: | key : value |
    key_on = "feature.properties.NAME_2",                       #municipality name from GeoJson as a key
    fill_color ="RdYlBu",                                       #brewing colors style
    fill_opacity = 1,
    line_opacity = 1,
    line_weight = 3,
    legend_name = "Student Number In Georgia(k)",               #name of legend
    highlight = True,                                           #highlight when hower with cursor
    bins = range2,                                              #setting custom range of legend
    smooth_factor = 0.1,                                            #accuracy of lines when you zoom in. less means more accurate
    show = False                                                        #don't show this layer when user opens site
)

#adding tooltip(popup message) for this choropleth(Choropleth2)

Choropleth2.geojson.add_child(
    folium.features.GeoJsonTooltip(
        fields=["NAME_0", "NAME_1", "NAME_2"],               #Information i want to get from JSON file |Country, Region, SubRegion|
        aliases=["Country: ","Region: ",'Municipality: '],          #just titles for them
        sticky=False,                                                   #popup will not follow cursor
        labels=True,                                                        #turn popup massage on
        #some minimal style for popup
        style = """
                    opacity: 0.7;
                    border: none;
                """
    )
)

#Group of CircleMarkers(Children Number) 

Children_Marker = folium.FeatureGroup(name = "Children Number Marker",
                                      show = False)                         #don't show this layer when user opens site

for lat, lon, municipality_nm, children in zip(Latitudes, Longitudes, Municipality_Name, list(Children)):
        Children_Marker.add_child(folium.vector_layers.CircleMarker(
            location = [lat, lon],                                                   #loaction of marker
            radius = Children_Circle_Radius(children) if children != 0 else 8,       #setting radius of marker with custom function
            popup = municipality_nm + ":" + "\n" +                                  #popup message: |SubRegion name: Children number|
                (str(children) if children != 0 else "No Information"),
            color = "Black",                                                        #color of circle outline
            fill_color = Children_Circle_Color(children),                           #setting fill color of cicle with custom function
            fill_opacity = 1                                                            
    ))

#Group of CircleMarkers(School Number) 

Schools_Marker = folium.FeatureGroup(name = "School Number Marker",
                                     show = False)                          #don't show this layer when user opens site

for lat, lon, municipality_nm, school_num in zip(Latitudes, Longitudes, Municipality_Name, School_Number):
    Schools_Marker.add_child(folium.vector_layers.CircleMarker(
            location = [lat, lon],                                                    #loaction of marker
            radius = School_Circle_Radius(school_num) if school_num != 0 else 8,      #setting radius of marker with custom function
            popup = municipality_nm + ":" + "\n" +                                  #popup message: |SubRegion name: Children number|
                 (str(school_num) if school_num != 0 else "No Information"),
            color = "Black",                                                        #color of circle outline
            fill_color = School_Circle_Color(school_num),                           #setting fill color of cicle with custom function
            fill_opacity = 0.8
    ))  

map = folium.Map(
        location= [42.2937977457207, 43.44543457031251] ,                     #some random start location
        #setting map style and zoom parameters
        tiles = "OPNVKarte" ,        
        attr = "Tiles &copy; Esri &mdash; National Geographic, Esri, DeLorme, NAVTEQ, UNEP-WCMC, USGS, NASA, ESA, METI, NRCAN, GEBCO, NOAA, iPC" ,
        #lock a camera on th borders of Georgia
        min_zoom = 8 ,
        max_zoom = 18 , 
        zoom_start = 8,
        max_bounds = True,
        min_lon = 30.30923457527854,
        max_lon = 60.30923457527854,
        min_lat = 37.0792318147887,
        max_lat = 47.0792318147887,
)

#adding few map styles

for name, style in Map_Styles.items():
    map.add_child(folium.TileLayer(
        tiles = style,
        #lock a camera on th borders of Georgia
        min_zoom = 8,
        max_zoom= 18,
        zoom_start = 8,
        max_bounds = True,
        min_lon = 30.30923457527854,
        max_lon = 60.30923457527854,
        min_lat = 37.0792318147887,
        max_lat = 47.0792318147887,
))

#adding every layer on the map

map.add_child(Borders_Group)

map.add_child(Choropleth1)

map.add_child(Choropleth2)

map.add_child(Children_Marker)

map.add_child(Schools_Marker)

map.add_child(folium.LayerControl())                #window that allows user to turn on/off any layer

map.save("EducationInGeorgia/EducationInGeorgia.html")        #saving map
