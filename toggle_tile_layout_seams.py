import arcpy
import pythonaddins

class ButtonClass1(object):
    """Implementation for layer_toggle.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        names = ["Grid_Lines", "Tile_Layout", "Seamlines"]

        mxd = arcpy.mapping.MapDocument("current")
        df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
        layers = arcpy.mapping.ListLayers(mxd, "*", df)

        for layer in layers:
          if layer.name in names:
            if layer.visible:
              layer.visible = False
            else: 
              layer.visible = True
          
        arcpy.RefreshTOC()
        arcpy.RefreshActiveView()

        del mxd,df,layer
