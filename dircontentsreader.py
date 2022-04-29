from pathlib import Path

#list reset

path = str(input("Input a path to 'GarrysMod' folder with the folder included in the path: "))
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
if int(input("Do you wanna save the generate list? \n It's required in order to use the autosub program \n 0/1 \n ")) == 0:
    with open('savedlist.txt', 'w') as f:
        f.write("")
    with open('urllist.txt','r') as urllist, open('savedlist.txt','a') as savedlist:
        for line in urllist:
            savedlist.write(line)
else:
    exit()

#autosubfeature using saved lists
#instructions