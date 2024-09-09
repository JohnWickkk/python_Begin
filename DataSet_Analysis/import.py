import numpy as np  # linear algebra

import pandas as pd  # data processing
import seaborn as sns
from matplotlib.pyplot import style
import os

# Setting Style for Plotting
style.use('fivethirtyeight')

import content
from google.colab import drive

drive.mount('/content/drive', force_remount=True)
local_dir = os.path.abspath(os.getcwd())
if local_dir != 'drive/My Drive/Colab Notebooks/data':
    os.chdir('drive/My Drive/Colab Notebooks/data')


class Mounted:
    pass


Mounted
var = at / content / drive

import os

import content
from google.colab import drive

drive.mount('/content/drive', force_remount=True)
local_dir = os.path.abspath(os.getcwd())
if local_dir != 'drive/My Drive/Colab Notebooks/data':
    os.chdir('drive/My Drive/Colab Notebooks/data')
Mounted
var = at / content / drive

df = pd.read_csv('winequality-red.csv')
print('Dataset dimentions' + str(df.shape))
df.head()
