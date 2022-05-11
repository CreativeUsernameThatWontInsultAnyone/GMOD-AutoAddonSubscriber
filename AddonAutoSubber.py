#imports
from contextlib import nullcontext
from pathlib import Path
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.ui import WebDriverWait
import subprocess
#

def dirreader(): # Option to store the addon path
    path = str(input("Example: D:\Program Files (x86)\Steam\steamapps\common\GarrysMod \nInput a path to 'GarrysMod' folder with the folder included in the path: "))

    # list reset

    try:
        with open('urllist.txt', 'w') as f:
            f.write("")
        with open('addonlist.txt', 'w') as f:
            f.write("")
    except FileNotFoundError:
        print("Text files missing. Add the required text files manually in the same directory as this program: \n addonlist.txt \n savedlist.txt \ urllist.txt")

    # stripping mod.gma's off .gma and '_' to get their id's. Then it stitches them together to create a url

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
            with open('addonlist.txt', 'a') as f:
                f.write(str(fin_entry) + "\n")
        except ValueError:
            print(fin_entry)
            print("*" * 20)
    if str(input("Do you wanna save the generated list? \n It's required in order to use the autosub program \n y/n \n ")) == 'y':
        with open('savedlist.txt', 'w') as f:
            f.write("")
        with open('urllist.txt', 'r') as urllist, open('savedlist.txt', 'a') as savedlist:
            for line in urllist:
                savedlist.write(line)
    else:
        exit()

    # instructions
    # add an option to run this using chrome.

def install_help(): #helps setup the required software. Runs some code in cmd to install selenium and a webdriver-manager
    try:
        first_run_check = str(input("Is this your first time running this? This software requires selenium and a proper webbrowser driver. \n I'll guide you through the process. \n y/n \n"))
    except ValueError:
        print("Wrong input homie.\n")
        install_help()
    if first_run_check == "y":
        print("First, let us download selenium. \n")
        subprocess.call(['''C:\\windows\\system32\\cmd.exe','/C', 
        pip install -U selenium &&
        pip3 install webdriver-manager && exit'''])
        try:
            browser_check = str(input("Do you have Firefox installed? As of right now autosubber requires Firefox in order to work \n y/n \n"))
        except ValueError:
            print("Wrong input! \n")
        if browser_check == "y":
            print("Great, we shall now proceed with installing a Firefox driver for selenium. I suggest you put it into an easily accesible folder \n Here's the link: https://github.com/mozilla/geckodriver/releases/tag/v0.31.0 \n")
            with open('driverpath.txt' ,'w') as driverpath:
                PATH = input("Example: C:\Folder\geckodriver.exe \n Provide me the full path to the browser webdriver: ")
                driverpath.write(PATH)
        else:
            input("Please install Firefox and rerun this program \n Press key to exit")
            exit()
    else:
        mod_install()
                
def mod_install(): #opens new tabs in the browser and uses .click to click on the subscribe button located via By.ID feature
    print("Give it a few moments to start up \n")
    with open('driverpath.txt' , 'r') as driverlist:
        PATH = driverlist.read()
        print(PATH)
        service = Service(PATH)
    with webdriver.Firefox(service=service) as driver: #creates the driver using the provided path and handles closing    
        try:    
            driver.get('https://steamcommunity.com/login')
            
            username = str(input("Steam username: "))
            print("\n\n\n\n\n\n\n\n\n\n\n\n")
            password = str(input("Steam password: "))
            print("\n\n\n\n\n\n\n\n\n\n\n\n")

            # Maybe search for the 3rd party mods on google?
    
            page_username = driver.find_element(By.NAME, 'username')    # Store sensitive data as enviroment variables  
            page_password = driver.find_element(By.NAME, 'password')    # Or at least make it so input is invisible to the user.
            
            page_username.clear()
            page_password.clear()

            page_username.send_keys(username + Keys.ENTER)
            page_password.send_keys(password + Keys.ENTER)

            steam_guard = str(input("Steam guard: ")).upper()
            print("\n\n\n\n\n\n\n\n\n\n\n\n")
            driver.find_element(By.ID, 'twofactorcode_entry').send_keys(steam_guard, Keys.ENTER)
            # Just as a precaution. I'm paranoid about user safety 
            username = ""
            password = ""
            steam_guard = ""

            # Safer way to pass creds?
            sleep(10)
            #print(driver.get_cookies()[0]) # Gets sessionid cookie
        except ElementNotInteractableException:
            print("If you login too many times in a short period of time or fail to login correctly,")

        with open('savedlist.txt', 'r') as savedlist:
            for line in savedlist:
                try:
                    #Open one tab before the loop and then tab in for each iteration after the respective mod page has loaded?
                    driver.get(line)
                    driver.find_element(By.ID, "SubscribeItemOptionAdd").click() #triggers the onclick() function
                    #wait.until(EC.invisibility_of_element())
                    sleep(3)
                    print(line," : INSTALLED JUST NOW", "\n", "*" * 20)
                except ElementNotInteractableException:
                    print(line,"INSTALLED BEFORE THIS RUN", "\n", "*" * 20)
                    continue
    print("Done!")

def driver_change_path():
    with open('driverpath.txt' ,'w') as f:
        PATH = str(input("Provide the path \n"))
        f.write(PATH)

def driver_read_path():
    with open('driverpath.txt' , 'r') as f:
        p = f.read()
        print(p)

#D:\_addonlinkfinder\chromedriver.exe - that's just my path. Nothing for you to use 

def main(): #main menu function that asks the user what he wants to do and calls the choosen function(s)
    try:
        print("I strongly insist you make a seperate folder for this program. Don't ever try running this from Downloads folder.\n")
        choice = int(input("Which program do you wanna use? \n 1. Dirreader - If this is your first time use this first \n Read README.md - It's in the zip file \n 2. Autosubber \n 3. Driver Path Change \n"))
        if choice == 1:
            dirreader()
        if choice == 2:
            install_help() #Calls mod install if first time check = n
        if choice == 3:
            driver_change_path()
            driver_read_path()    
    except ValueError:
        print("Wrong input buddy!")
        main()
__name__ == '__main__'
main()

# To do

# Handle wrong ID's
# Save foldernames for mods installed externally
