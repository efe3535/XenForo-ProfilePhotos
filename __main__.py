import os
import requests
from colorama import Fore
from requests import status_codes

dirname = input("What should be the name of the folder where the pictures will be saved?\t")
try:
    os.mkdir(dirname)
    os.chdir(dirname)
except FileExistsError:
    print("Directory already exists, rename it.")
    exit()

for member in range(1,5000):
    #404 dönüyorsa üye profil fotoğrafı koymamış demektir.
    #404 dönüyorsa geç, 200 dönüyorsa indir
    if(member>999):
        temp_findmemberfolder = list(str(member))
        temp_findmemberfolder = "".join(temp_findmemberfolder[:len(temp_findmemberfolder)-3])
        image = requests.get(f"https://www.technopat.net/sosyal/data/avatars/o/{temp_findmemberfolder}/{str(member)}.jpg",allow_redirects=True)
        if(image.status_code != 404):
            print(Fore.GREEN + f"Success, {str(member)}. member has got a profile photo! 🥳" + Fore.RESET)
            saveimage=open(str(member)+".jpg","wb")
            saveimage.write(image.content)
        else:
            print(Fore.RED + f"Unfortunately, {str(member)}. member hasn't got a profile photo 🙁" + Fore.RESET)
    else:
        print(f"https://www.technopat.net/sosyal/data/avatars/o/0/{str(member)}.jpg")
        image = requests.get(f"https://www.technopat.net/sosyal/data/avatars/o/0/{str(member)}.jpg",allow_redirects=True)
        if(image.status_code != 404):
            print(Fore.GREEN + f"Success, {str(member)}. member has got a profile photo 🥳" + Fore.RESET)
            saveimage=open(str(member)+".jpg","wb")
            saveimage.write(image.content)
        else:
            print(Fore.RED + f"Unfortunately, {str(member)}. member has not got a profile photo 🙁" + Fore.RESET)