import os
from PIL import Image

f = r'D:\OneDrive - vignanits.ac.in\backup\backup\Bhuv\Attendance Project\output\preethi'      #Enter the location of your Image Folder
    
new_d = 160

for file in os.listdir(f):
    f_img = f+'/'+file
    try:
        img = Image.open(f_img)
        img = img.resize((new_d, new_d))
        img.save(f_img)
    except IOError:
        pass