import arcpy
import pythonaddins

class ButtonClass2(object):
    """Implementation for raster_toggle.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        mxd = arcpy.mapping.MapDocument("current")
        df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
        layers = arcpy.mapping.ListLayers(mxd, "*.tif", df)

        for layer in layers:
          if layer.visible:
            layer.visible = False
          else:
            layer.visible = True

        arcpy.RefreshTOC()
        arcpy.RefreshActiveView()

        del mxd, df, layer
