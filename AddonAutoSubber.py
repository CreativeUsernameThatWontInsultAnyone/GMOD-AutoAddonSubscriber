from pathlib import Path; 
from selenium import webdriver;from selenium.common.exceptions import NoSuchElementException
import subprocess 

def dirreader():
    path = str(input("Example: D:\Program Files (x86)\Steam\steamapps\common\GarrysMod \nInput a path to 'GarrysMod' folder with the folder included in the path: "))
    
    #list reset
    
    try:
        with open('urllist.txt', 'w') as f:
            f.write("")
        with open('addonlist.txt' , 'w') as f:
            f.write("")
    except FileNotFoundError:
        print("Text files missing. Add the required text files manually in the same directory as this program: \n addonlist.txt \n savedlist.txt \ urllist.txt")

    #actual code

    print("@" * 20)
    entries = Path(path + '\\garrysmod\\addons')
    print("Path loaded succesfully!")
    for entry in entries.iterdir():
        splitentry = (str(entry.name).split('_')[-1])
        print(splitentry)
        fin_entry = str(splitentry.strip(".gma"))
        print(fin_entry)
        print("*" * 20)
        try:
            fin_entry = int(fin_entry)
            url = "https://steamcommunity.com/sharedfiles/filedetails/?id=" + str(fin_entry) + "\n"
            with open('urllist.txt', 'a') as f:
                f.write(url)
            with open('addonlist.txt' , 'a') as f:
                f.write(str(fin_entry) + "\n")
        except ValueError:
            print(fin_entry)
            print("*" * 20)
            return url
    if str(input("Do you wanna save the generated list? \n It's required in order to use the autosub program \n y/n \n ")) == 'y':
        with open('savedlist.txt', 'w') as f:
            f.write("")
        with open('urllist.txt','r') as urllist, open('savedlist.txt','a') as savedlist:
            for line in urllist:
                savedlist.write(line)
    else:
        exit()

    #instructions

def autosubber():
    try:
        first_run_check = int(input("Is this your first time running this? This software requires selenium and a proper webbrowser driver. \n I'll guide you through the process. \n y/n \n"))
    except ValueError:
        print("Wrong input homie.\n")
        autosubber()
    if first_run_check == "y":
        print("First, let us download selenium. \n")
        subprocess.call(['C:\\windows\\system32\\cmd.exe', '/C', 'pip install -U selenium && exit'])
        try:
            chrome_check = str(input("Do you have chrome installed? Autosubber requires chrome in order to work \n y/n \n"))
        except ValueError:
            print("Wrong input \n")
        if chrome_check == "y":
            print("Great, we shall now proceed with installing a Chrome driver for selenium. I suggest you put it into an easily accesible folder \n Here's the link: https://chromedriver.chromium.org/downloads \n")
        else:
            input("Please install Chrome and rerun this program \n Press a key to exit")
            exit()
        PATH = str(input("Example: C:\Folder\chromedriver.exe \n Provide me the full path to the Chrome webdriver:  "))
        driver = webdriver.Chrome(PATH)

        #steamlogin check using inspect for login button

        input("If succesful, this will open the required workshop mod in your browser and download it \n Also please login to steam on Chrome then continue \n Press a key to continue \n")
        with open('savedlist.txt' , 'r') as savedlist:
            for line in savedlist:
                try:
                    driver.get(line)
                    button = driver.find_element_by_class_name("subscribeOption subscribe selected")
                    button.click()
                except NoSuchElementException:
                    continue
def main():
    try:
        print("I strongly insist you make a seperate folder for this program. Don't ever try running this from Downloads folder.\n")
        choice = int(input("Which program do you wanna use? \n 1. Dirreader - if this is your first time use this first \n Read README.md \n 2. Autosubber \n"))
        if choice == 1:
            dirreader()
        if choice == 2:
            autosubber()
    except ValueError:
        print("Wrong input buddy")
        main()
main()