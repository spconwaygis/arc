import arcpy
import pythonaddins

class ButtonClass2(object):
    """Implementation for Arc_QSI_Error_Patch_Toolbar_addin.button_1 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        sourceLayer = arcpy.mapping.Layer(r"P:\Projects\__ArcMap_Master_GDB_LYR\CIR.lyr")
        groupLayer = arcpy.mapping.Layer(r"P:\Projects\__ArcMap_Master_GDB_LYR\TIF_Group.lyr")
        mxd = arcpy.mapping.MapDocument("Current")
        df = arcpy.mapping.ListDataFrames(mxd,"*")[0]

        try:
          targetGroupLayer = arcpy.mapping.ListLayers(mxd, "TIF_Group", df)[0]
          arcpy.mapping.RemoveLayer(df, targetGroupLayer)
        except:
          pass
          
        arcpy.mapping.AddLayer(df, groupLayer, "BOTTOM")

        targetGroupLayer = arcpy.mapping.ListLayers(mxd, "TIF_Group", df)[0]

        text_file = open("C:/timer_tiles/tile_list.txt", "r")
        lines = text_file.readlines()
        text_file.close()

        fields = ['Path', 'Error_Path']
        fc = arcpy.mapping.Layer("Error_Patch")
        cursor = arcpy.da.SearchCursor(fc, fields)
        for row in cursor:
          for i in range(0,len(lines)):
            tile_path=str(lines[i].replace("\\","/"))
            tile_path=tile_path.replace("\n","")
            if str(row[0].replace("\\","/"))==tile_path:
              path = str(row[1].replace("\\","/"))
              newlayer = arcpy.mapping.Layer(path)
              arcpy.mapping.UpdateLayer(df,newlayer,sourceLayer, symbology_only = True)
              arcpy.mapping.AddLayerToGroup(df, targetGroupLayer, newlayer, "Bottom")
              del newlayer
