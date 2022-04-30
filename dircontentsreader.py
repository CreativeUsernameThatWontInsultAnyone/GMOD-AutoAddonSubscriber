from pathlib import Path
from time import sleep ;import webbrowser 

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
    #new = 2     # open in a new tab, if possible
    #browser = str(input("Which browser are you using: \n mozilla \n opera \n google-chrome \n chrome \n"))
    print("If succesful, this will open the required workshop mod in your browser \n")
    with open('savedlist.txt' , 'r') as savedlist:
        for url in savedlist:
            webbrowser.open_new_tab(url)
            #webbrowser.get(using=str(browser)).open(line,new=new) # open a public URL
            sleep(4)
            print(url, "*" * 20)
def main():
    try:
        choice = int(input("Which program do you wanna use? \n 1. Dirreader - if this is your first time use this first \n Read README.md \n 2. Autosubber \n"))
        if choice == 1:
            dirreader()
        if choice == 2:
            autosubber()
    except ValueError:
        print("Wrong input buddy")
        main()
main()
