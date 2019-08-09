import os
from gdrive_util import download_file_from_google_drive
from zip_util import extractZip


print('Downloading models.zip ...')
download_file_from_google_drive('1_UMmb0Lit70hpCS1OwLLOXFQ0D__HcnX', 'models.zip')

print('Extracting zip file ...')
extractZip('models.zip', '.')

os.remove('models.zip')
