import arcpy
import pythonaddins
import os
import functools
import threading

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

class ButtonClass3(object):
    """Implementation for RGB.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        mxd = arcpy.mapping.MapDocument("current")
        df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
        layers = arcpy.mapping.ListLayers(mxd, "*.tif", df)
        sourceLayer = arcpy.mapping.Layer(r"P:\Projects\__ArcMap_Master_GDB_LYR\RGB.lyr")

        for layer in layers:
          if layer.visible:
            arcpy.mapping.UpdateLayer(df,layer,sourceLayer, symbology_only = True)

        arcpy.RefreshTOC()
        arcpy.RefreshActiveView()

        del mxd, df, layers

class ButtonClass4(object):
    """Implementation for CIR.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        mxd = arcpy.mapping.MapDocument("current")
        df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
        layers = arcpy.mapping.ListLayers(mxd, "*.tif", df)
        sourceLayer = arcpy.mapping.Layer(r"P:\Projects\__ArcMap_Master_GDB_LYR\CIR.lyr")

        for layer in layers:
          if layer.visible:
            arcpy.mapping.UpdateLayer(df,layer,sourceLayer, symbology_only = True)

        arcpy.RefreshTOC()
        arcpy.RefreshActiveView()

        del mxd, df, layers

class ButtonClass5(object):
    """Implementation for NIR.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        mxd = arcpy.mapping.MapDocument("current")
        df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
        layers = arcpy.mapping.ListLayers(mxd, "*.tif", df)
        sourceLayer = arcpy.mapping.Layer(r"P:\Projects\__ArcMap_Master_GDB_LYR\NIR.lyr")

        for layer in layers:
          if layer.visible:
            arcpy.mapping.UpdateLayer(df,layer,sourceLayer, symbology_only = True)

        arcpy.RefreshTOC()
        arcpy.RefreshActiveView()

        del mxd, df, layers

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

class ButtonClass7(object):
    """Implementation for white_transparent.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        mxd = arcpy.mapping.MapDocument("current")
        df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
        layers = arcpy.mapping.ListLayers(mxd, "*.tif", df)
        sourceLayer = arcpy.mapping.Layer(r"P:\Projects\__ArcMap_Master_GDB_LYR\white_transparent.lyr")

        for layer in layers:
          arcpy.mapping.UpdateLayer(df,layer,sourceLayer, symbology_only = True)

        arcpy.RefreshTOC()
        arcpy.RefreshActiveView()

        del mxd, df, layers

class ButtonClass8(object):
    """Implementation for open_in_ps.button (Button)"""
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
        
        fc = arcpy.mapping.Layer("Tile_Layout")

        cursor = arcpy.da.SearchCursor(fc, 'Path')
        
        for row in cursor:
            path = str(row[0].replace("\\","/"))
        startfile(path) 
        
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
