import os
import requests
from colorama import Fore
from requests import status_codes
import sys


help_commands = """
Arguments:
\t--url=<XenForo forum url to fetch profile photos>
\t--dirname=<directory name to save images>
\t--start=<number to start at>
\t--stop=<number to stop at>
\t--help\tDisplay help text 
"""

if(len(sys.argv)==1):
    print(help_commands)
    exit()

for check_help in sys.argv:
    if(check_help.lower()=="--help" or check_help.lower()=="-h"):
        print(help_commands)
        exit()

parse_arguments = sys.argv

url = ""
url_exists = False

start = ""
start_exists = False

stop = ""
stop_exists = False

dirname = ""
dirname_exists = False

argumentdoesntexist_list = []

index = 0

for arg in parse_arguments:
    try:
        if("--dirname" in arg):
            dirname=arg.split("--dirname=")[1]
            dirname_exists = True
        if("--start" in arg):
            start=int(arg.split("--start=")[1])
            start_exists = True
        if("--stop" in arg):
            stop=int(arg.split("--stop=")[1])
            stop_exists = True
        if("--url" in arg):
            url=arg.split("--url=")[1]
            url_exists = True
    
    except IndexError:
        print("Syntax error on arguments:")
        print(help_commands)
        exit()

if(not start_exists or not url_exists or not stop_exists or not dirname_exists):
    print("Aborting, because some argument(s) does not exist.")
    exit()

try:
    os.mkdir(dirname)
    os.chdir(dirname)

except FileExistsError:
    print("Directory already exists, rename it.")
    exit()

# start = input("Which number would you like to start downloading?\t")
# stop = input("Which number would you like to stop downloading?\t")

for member in range(int(start),int(stop) + 1):
    #404 dönüyorsa üye profil fotoğrafı koymamış demektir.
    #404 dönüyorsa geç, 200 dönüyorsa indir
    if(member>999):
        temp_findmemberfolder = list(str(member))
        temp_findmemberfolder = "".join(temp_findmemberfolder[:len(temp_findmemberfolder)-3])
        image = requests.get(f"{url}/data/avatars/o/{temp_findmemberfolder}/{str(member)}.jpg",allow_redirects=True)
        if(image.status_code != 404):
            print(Fore.GREEN + f"Success, {str(member)}. member has got a profile photo! 🥳" + Fore.RESET)
            saveimage=open(str(member)+".jpg","wb")
            saveimage.write(image.content)
        else:
            print(Fore.RED + f"Unfortunately, {str(member)}. member hasn't got a profile photo 🙁" + Fore.RESET)
    else:
        print(f"{url}/data/avatars/o/0/{str(member)}.jpg")
        image = requests.get(f"{url}/data/avatars/o/0/{str(member)}.jpg",allow_redirects=True)
        if(image.status_code != 404):
            print(Fore.GREEN + f"Success, {str(member)}. member has got a profile photo 🥳" + Fore.RESET)
            saveimage=open(str(member)+".jpg","wb")
            saveimage.write(image.content)
        else:
            print(Fore.RED + f"Unfortunately, {str(member)}. member has not got a profile photo 🙁" + Fore.RESET)
