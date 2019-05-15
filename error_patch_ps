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
