__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
from zipfile import ZipFile

cwd = os.getcwd()
print('Current Working Directory is: ', cwd)
absolute_path = 'C:/Users/pA/Documents/Winc/files'
os.chdir(absolute_path)

######PART1############
def clean_cache():
    path = './clean_cache'
    dir_clean_cache = os.mkdir(path)
    return dir_clean_cache

#print(clean_cache())
    
######PART2############
def cache_zip(path_zip,target_dir):
  with ZipFile(path_zip, 'r') as zObject:
   zObject.extractall(path=target_dir)  
            
path_zip = 'C:/Users/pA/Documents/Winc/files/data.zip'
path_dir = 'C:/Users/pA/Documents/winc/files/clean_cache'

cache_zip(path_zip,path_dir)

#####PART3############

def cached_files():
   global list_unzipped
   list_unzipped =os.listdir(path='C:/Users/pA/Documents/winc/files/clean_cache')
   return list_unzipped

print(cached_files())


os.chdir('C:/Users/pA/Documents/winc/files/clean_cache')
cwd1 = os.getcwd()
print('Current Working Directory is: ', cwd1)

directory =('C:/Users/pA/Documents/winc/files/clean_cache')

def find_password(password):
   for text in password:
      with open(text) as f:
       mylist = list(f)
       for i in mylist:
         if "password" in i:
           return i 
         else:
             continue
         

print(find_password(list_unzipped))

