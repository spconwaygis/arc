# arc
Python scripts for ArcGIS

Button implementation by group and broken out to individual scripts.

arcmap_full_button_implementation:

  toggle_tile_layout_seams - Toggles specifically named layers on and off
  
  toggle_rasters - Toggles all loaded rasters (TIFs) on and off
  
  rgb_layer - Changes band setup for all rasters (TIFs) to RGB - requires layer file
  
  cir_layer - Changes band setup for all rasters (TIFs) to CIR - requires layer file
  
  nir_layer - Changes band setup for all rasters (TIFs) to grayscale NIR - requires layer file
  
  black_transparent - Makes any black (void data) areas of a raster transparent - requires layer file
  
  white_transparent - Makes any white (void data) areas of a raster transparent - requires layer file
  
  ps_button - Traverses attribute field structure of tile layout to get path associated with selected shapefile and opens it in  Photoshop
  
  load_from_timer - Imports tiles that have been checked out in the QSI production timer into ArcMap
  

arcmap_patch_button_implementation:


  error_patch_ps - Traverses attribute field structure of tile layout and patch layout to get path associated with selected shapefile and opens all associated patch tiles in Photoshop
  
  load_error_patch_from_timer - Imports only the error patches associated with the tiles checked out in the QSI production timer
  
  
