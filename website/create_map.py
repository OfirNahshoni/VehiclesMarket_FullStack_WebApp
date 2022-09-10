import folium
from folium import plugins
from folium.plugins import LocateControl
from os.path import join
from .config import PROJECT_NAME

class CreateMap():
    def __init__(self, gdfs, names):
        m = folium.Map(tiles='openstreetmap')
        LocateControl().add_to(m)
        
        for gdf, name in zip(gdfs,names):
            if 'Heat Map' in name: # TODO: set in config file
                plugins.HeatMap(gdf, name=name).add_to(m)
            else:    
                x1,y1,x2,y2 = gdf['geometry'].total_bounds
                m.fit_bounds([[y1, x1], [y2, x2]])
                folium.GeoJson(gdf,name=name).add_to(m)
        folium.LayerControl().add_to(m)
        m.save(join(PROJECT_NAME, 'templates\map.html'))
