import arcpy
import pythonaddins
import os
import functools
import threading

class ButtonClass1(object):
    """Implementation for Arc_QSI_Error_Patch_Toolbar_addin.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        def run_in_other_thread(function):
            @functools.wraps(function)
            def fn_(*args, **kwargs):
                thread = threading.Thread(target=function, args=args, kwargs=kwargs)
                thread.start()
                thread.join()
            return fn_
        startfile = run_in_other_thread(os.startfile)

        fields = ['Path', 'Error_Path']
        fc = arcpy.mapping.Layer("Error_Patch")
        cursor = arcpy.da.SearchCursor(fc, fields)

        layout_fc = arcpy.mapping.Layer("Tile_Layout")
        cursor2=arcpy.da.SearchCursor(layout_fc,'Path')

        for row in cursor2:
          for e_row in cursor:
            tile_path=str(row[0].replace("\\","/"))
            e_tile_path=str(e_row[0].replace("\\","/"))
            if tile_path==e_tile_path:
              path=str(e_row[1].replace("\\","/"))
              startfile(path)

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
              del path
            del tile_path

        ext = targetGroupLayer.getExtent()
        df.extent=ext

        arcpy.RefreshActiveView()
        arcpy.RefreshTOC()

        del mxd, df

