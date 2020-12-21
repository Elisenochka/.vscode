import os
import os.path

file_list = os.listdir(r"C:\Users\elili\Documents\IntelligenceRetail\Nestle\productShots")
path = r"C:\Users\elili\Documents\IntelligenceRetail\Nestle\productShots"

for file_name in file_list:
    print(file_name)

for filename in file_list:
    if filename.startswith("producto - "):
        os.rename(os.path.join(path, filename), os.path.join(path, filename[11:]))

for file_name in file_list:
    print(file_name)