import arcpy
import pythonaddins

class ButtonClass9(object):
    """Implementation for timer.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        sourceLayer = arcpy.mapping.Layer(r"P:\Projects\__ArcMap_Master_GDB_LYR\CIR.lyr")
        mxd = arcpy.mapping.MapDocument("Current")
        df = arcpy.mapping.ListDataFrames(mxd,"*")[0]

        text_file = open("C:/timer_tiles/tile_list.txt", "r")
        lines = text_file.readlines()
        text_file.close()

        for i in range(0,len(lines)):
          
          newlayer = arcpy.mapping.Layer(lines[i])
          arcpy.mapping.UpdateLayer(df,newlayer,sourceLayer, symbology_only = True)
          arcpy.mapping.AddLayer(df, newlayer,"Bottom")
          del newlayer

        arcpy.RefreshActiveView()
        arcpy.RefreshTOC()

        del mxd, df
