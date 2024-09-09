import os

import content
from google.colab import drive
drive.mount('/content/drive', force_remount=True)
local_dir = os.path.abspath(os.getcwd())
if local_dir != 'drive/My Drive/Colab Notebooks/data':
  os.chdir('drive/My Drive/Colab Notebooks/data')
Mounted at /content/drive