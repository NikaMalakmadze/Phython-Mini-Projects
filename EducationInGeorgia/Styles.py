
'''         '''          '''
        Style Module
'''         '''          '''

__all__ = [
    'hightlight_function',
    'Children_Circle_Radius',
    'Children_Circle_Color',
    'School_Circle_Radius',
    'School_Circle_Color',
    'Map_Styles',
    'border_style'
]

#Map Styles

Map_Styles = {
    'OPNVKarte': 'OPNVKarte',
    'CyclOSM': 'CyclOSM',
    'Esri.NatGeoWorldMap': 'Esri.NatGeoWorldMap',
    'USGS.USTopo': 'USGS.USTopo'
}

#Style Function

border_style = {
    'color': '#000000',
    'weight': '3',
    'fillOpacity': '0'
}

#Hightlight Function

def hightlight_function(feature):
    return {
        'weight': '7',
        'color': '#000000',
        'fillColor': 'transparent',
        'dashArray': '7, 7'
}

#Circle Functions

def Children_Circle_Radius(value):
    return value**0.31

def Children_Circle_Color(value):
     if value < 2000:
        return "#9e0142"
     elif value < 10000:
        return "#d53e4f"
     elif value < 20000:
        return "#f46d43"
     elif value < 50000:
        return "#f46d43"
     elif value < 80000:
        return "#fdae61"
     elif value < 101000:
        return "#fee08b"
     elif value < 140000:
        return "#ffffbf"
     elif value < 170000:
        return "#e6f598"
     elif value < 200000:
        return "#abdda4"
     elif value < 230000:
        return "#66c2a5"

def School_Circle_Radius(value):
    return value**0.71

def School_Circle_Color(value):
    if value < 10:
        return"#ffffe5"
    if value < 20:
        return"#f7fcb9"
    if value < 30:
        return"#d9f0a3"
    if value < 40:
        return"#addd8e"
    if value < 50:
        return"#78c679"
    if value < 60:
        return"#41ab5d"
    if value < 70:
        return"#238443"
    if value < 80:
        return"#006837"
    if value < 300:
        return"#004529"

