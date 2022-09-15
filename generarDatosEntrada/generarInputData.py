import matplotlib.pyplot as plt                      
import datetime                                     
import glob                                         
import rioxarray                                    
import pickle                                       
import os                                            
from pathlib import Path                                                                 #
import shutil
import re
import numpy as np
import glob
from matplotlib.colors import LinearSegmentedColormap
import pandas as pd


BASE_DIR = "./"

BASE_DIR_R     = os.path.join(BASE_DIR,"R/masked")
BASE_DIR_G     = os.path.join(BASE_DIR,"G/masked")
BASE_DIR_B     = os.path.join(BASE_DIR,"B/masked")
BASE_DIR_NIR   = os.path.join(BASE_DIR,"NIR/masked")
BASE_DIR_NDVI  = os.path.join(BASE_DIR,"NDVI/masked")
BASE_DIR_SWIR  = os.path.join(BASE_DIR,"SWIR/masked")
BASE_DIR_W     = os.path.join(BASE_DIR,"W/masked")
BASE_DIR_THETA = os.path.join(BASE_DIR,"THETA/masked")

band_dirs = [
 BASE_DIR_R,    
 BASE_DIR_G,   
 BASE_DIR_B,
 BASE_DIR_NIR,  
 BASE_DIR_NDVI,
 BASE_DIR_SWIR ,
 BASE_DIR_W , 
 BASE_DIR_THETA
]

bands_dict = dict(zip(["R","G","B","NIR","NDVI","SWIR","W","THETA"], band_dirs))

bands_dict


dir_R    = bands_dict["R"]
dir_G    = bands_dict["G"]
dir_B    = bands_dict["B"]
dir_NIR    = bands_dict["NIR"]
dir_NDVI    = bands_dict["NDVI"]
dir_SWIR    = bands_dict["SWIR"]
dir_W    = bands_dict["W"]
dir_THETA = bands_dict["THETA"]


R_files = [f for f in os.listdir(dir_R) if os.path.isfile(os.path.join(dir_R, f))]
G_files = [f for f in os.listdir(dir_G) if os.path.isfile(os.path.join(dir_G, f))]
B_files = [f for f in os.listdir(dir_B) if os.path.isfile(os.path.join(dir_B, f))]
NIR_files = [f for f in os.listdir(dir_NIR) if os.path.isfile(os.path.join(dir_NIR, f))]
NDVI_files = [f for f in os.listdir(dir_NDVI) if os.path.isfile(os.path.join(dir_NDVI, f))]
SWIR_files = [f for f in os.listdir(dir_SWIR) if os.path.isfile(os.path.join(dir_SWIR, f))]
W_files = [f for f in os.listdir(dir_W) if os.path.isfile(os.path.join(dir_W, f))]
THETA_files = [f for f in os.listdir(dir_THETA) if os.path.isfile(os.path.join(dir_THETA, f))]

R_files.sort()
G_files.sort()
B_files.sort()
NIR_files.sort()
NDVI_files.sort()
SWIR_files.sort()
W_files.sort()
THETA_files.sort()

r = []
g = []
b = []
nir = []
ndvi = []
swir = []
w = []
theta = []
for file_idx in range(1, len(R_files)+1):

    print('Fichero', file_idx, 'de 72')
 
    R     = rioxarray.open_rasterio(os.path.join(dir_R, R_files[file_idx]), masked=True)
    G     = rioxarray.open_rasterio(os.path.join(dir_G, G_files[file_idx]), masked=True)
    B     = rioxarray.open_rasterio(os.path.join(dir_B, B_files[file_idx]), masked=True)
    NIR     = rioxarray.open_rasterio(os.path.join(dir_NIR, NIR_files[file_idx]), masked=True)
    NDVI     = rioxarray.open_rasterio(os.path.join(dir_NDVI, NDVI_files[file_idx]), masked=True)
    SWIR     = rioxarray.open_rasterio(os.path.join(dir_SWIR, SWIR_files[file_idx]), masked=True)
    W     = rioxarray.open_rasterio(os.path.join(dir_W, W_files[file_idx]), masked=True)
    THETA = rioxarray.open_rasterio(os.path.join(dir_THETA, THETA_files[file_idx]), masked=True)

    rows = R.shape[1]
    cols = R.shape[2]
    for i in range(rows):
        for j in range(cols):
            if(~np.isnan(R[0][i,j])):
                r.append(R[0][i,j])
                g.append(G[0][i,j])
                b.append(B[0][i,j])
                nir.append(NIR[0][i,j])
                ndvi.append(NDVI[0][i,j])
                swir.append(SWIR[0][i,j])
                w.append(W[0][i,j])
                theta.append(THETA[0][i,j])

  
# initialize data of lists.
data = {'R': r, 'G': g, 'B': b, 'NIR': nir, 'NDVI': ndvi, 'SWIR': swir, 'W': w, 'THETA': theta}
  
# Create DataFrame
df = pd.DataFrame(data)

df.to_csv('./salida.csv', index=False)

print('Finishhhhh')
