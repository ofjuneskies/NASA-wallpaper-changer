import requests
import ctypes
import os
import ast
import shutil
from PIL import Image
import wget
import urllib
import subprocess

#Remove previous image and description if they exist
if os.path.exists("./nasa_wallpaper.jpg"):
    os.remove("./nasa_wallpaper.jpg")

if os.path.exists("./desc.txt"):
    os.remove("./desc.txt")

#Retrieve image and description from API
#and download them into their respective files
r = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
data = ast.literal_eval(r.content.decode('utf-8'))
url = data["hdurl"]
desc = data["explanation"]
note_file = open("./desc.txt", "w")
desc_split_str = ''
desc_list = desc.split(" ")
for i in range(len(desc_list)):
    desc_split_str += desc_list[i] + " "
    if i % 10 == 0 and i != 0:
        desc_split_str += "\n"
note_file.write(desc_split_str)
note_file.close()
wget.download(url, "./nasa_wallpaper.jpg")
#image = Image.open("./nasa_wallpaper.jpg")
#image.show()

#Open description of image
if os.path.isfile("./desc.txt"):
    subprocess.Popen([os.path.abspath("./desc.txt")], shell=True)
    print("Description opened")
else:
    print("Description failed to be opened")

#Set image as wallpaper
if os.path.isfile("./nasa_wallpaper.jpg"):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath("./nasa_wallpaper.jpg"), 1)
    print("Wallpaper set")
    print(url)
else:
    print("Wallpaper failed to be set")
    print(url)