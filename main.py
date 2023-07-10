__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os, re, os.path
import os 
from zipfile import ZipFile
import shutil

os.chdir('files')

base_path = os.getcwd()
cache_path = os.path.join(base_path, "cache")
data_path = os.path.join(base_path, "data.zip")

print(base_path)
print(cache_path)
print(data_path)
###############################################

def clean_cache():
   if os.path.exists(cache_path):
      shutil.rmtree(cache_path)
   os.mkdir(cache_path)

clean_cache()
#################################################

def cache_zip(zip_file_path,cache_path):
  with ZipFile(zip_file_path, 'r') as zObject:
   zObject.extractall(path=cache_path)  
            
zip_path = os.path.join(base_path,'data.zip')
target_path = os.path.join(base_path,'cache')

print(target_path)

cache_zip(data_path,cache_path)
list_unzipped =os.listdir(target_path)

def cached_files():
    global cached_files_list
    cached_files_list = []
    for path in os.listdir(cache_path):
        full_path = os.path.join(cache_path, path)
        cached_files_list.append(full_path)
    print(cached_files_list)




cached_files()


def find_password(password):
   for text in password:
      with open(text) as f:
       mylist = list(f)
       for i in mylist:
         if "password" in i:
           return i 
         else:
             continue
         

print(find_password(cached_files_list))

