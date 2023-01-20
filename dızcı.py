# d-zc-bazıdosyaları dızlıyor

import os
import shutil
extension=(".doc",".pdf",".jpg",".gif")
print("dızlancaklar: ",extension)
temp_folder= os.path.join(os.environ["LOCALAPPDATA"],"temp")
for subdir,dirs,files in os.walk("."):
    for file in files:
        if file.endswith(extension):
            source_paht=os.path.join(subdir,file)
            destion_pah=os.path.join(temp_folder, file)
            shutil.copy2(source_paht,destion_pah)
            print("end")
