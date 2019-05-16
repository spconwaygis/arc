import arcpy
import pythonaddins

class ButtonClass6(object):
    """Implementation for black_transparent.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        mxd = arcpy.mapping.MapDocument("current")
        df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
        layers = arcpy.mapping.ListLayers(mxd, "*.tif", df)
        sourceLayer = arcpy.mapping.Layer(r"P:\Projects\__ArcMap_Master_GDB_LYR\black_transparent.lyr")

        for layer in layers:
          arcpy.mapping.UpdateLayer(df,layer,sourceLayer, symbology_only = True)

        arcpy.RefreshTOC()
        arcpy.RefreshActiveView()

        del mxd, df, layers
