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

#for file_idx in range(0, len(R_files)):
for file_idx in range(60, 71):  # Se ha dividido el bucle for principal por los problemas de tamaño de las tablas generadas

    print('Fichero', file_idx, 'de 72')

    R     = rioxarray.open_rasterio(os.path.join(dir_R, R_files[file_idx]), masked=True)
    G     = rioxarray.open_rasterio(os.path.join(dir_G, G_files[file_idx]), masked=True)
    B     = rioxarray.open_rasterio(os.path.join(dir_B, B_files[file_idx]), masked=True)
    NIR     = rioxarray.open_rasterio(os.path.join(dir_NIR, NIR_files[file_idx]), masked=True)
    NDVI     = rioxarray.open_rasterio(os.path.join(dir_NDVI, NDVI_files[file_idx]), masked=True)
    SWIR     = rioxarray.open_rasterio(os.path.join(dir_SWIR, SWIR_files[file_idx]), masked=True)
    W     = rioxarray.open_rasterio(os.path.join(dir_W, W_files[file_idx]), masked=True)
    THETA = rioxarray.open_rasterio(os.path.join(dir_THETA, THETA_files[file_idx]), masked=True)

    R = np.ravel(R)
    G = np.ravel(G)
    B = np.ravel(B)
    NIR = np.ravel(NIR)
    NDVI = np.ravel(NDVI)
    SWIR = np.ravel(SWIR)
    W = np.ravel(W)
    THETA = np.ravel(THETA)
    
    r = r + R[~np.isnan(R)].tolist()
    g = g + G[~np.isnan(G)].tolist()
    b = b + B[~np.isnan(B)].tolist()
    nir = nir + NIR[~np.isnan(NIR)].tolist()
    ndvi = ndvi + NDVI[~np.isnan(NDVI)].tolist()
    swir = swir + SWIR[~np.isnan(SWIR)].tolist()
    w = w + W[~np.isnan(W)].tolist()
    theta = theta + THETA[~np.isnan(THETA)].tolist()

print('Heree 1')

# initialize data of lists.
data = {'R': r, 'G': g, 'B': b, 'NIR': nir, 'NDVI': ndvi, 'SWIR': swir, 'W': w, 'THETA': theta}
  
# Create DataFrame
df = pd.DataFrame(data)
#df.drop_duplicates(keep='first')

print('Heree 2')

print(df.head())

df.to_csv('./salida5.csv', index=False)

print('Finishhhhh')

