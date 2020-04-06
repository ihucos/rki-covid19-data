from arcgis.gis import GIS
anon_gis = GIS()
features = anon_gis.content.get('dd4580c810204019a7b8eb3e0b329dd6').tables[0].query()
features.save(save_location='.', out_name="data.csv")
