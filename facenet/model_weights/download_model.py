import os
from gdrive_util import download_file_from_google_drive
from zip_util import extractZip


print('Downloading 20180402-114759.zip ...')
download_file_from_google_drive('1EXPBSXwTaqrSC0OhUdXNmKSh9qJUQ55-', '20180402-114759.zip')

print('Extracting zip file ...')
extractZip('20180402-114759.zip', '.')

os.remove('20180402-114759.zip')
