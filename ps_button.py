import arcpy
import pythonaddins
import os
import functools
import threading

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
