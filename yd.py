import os


print ("Welcome to Youtube Downloader\n")

def download():
    print ("Enter the Url")
    string = input().strip()
    string1 = "youtube-dl -F %s" % (string)
    os.system(string1) 
    print ("Enter the format")
    formatt = int(input().strip())
    print ("Enter the path for Download")
    print ("1.Current dir\n2.Downloads\n3.Other")
    choice = int(input().strip())
    if (choice==1) :
        path="'%(title)s.%(ext)s'"
    elif choice==2:
        path="'/home/rahulsharma/Downloads/%(title)s.%(ext)s'"
    else:
        path=input("Enter the path> ").strip()
        path = "'"+path+"%(title)s.%(ext)s'"
    if(len(path)!=0):
        string2 = "youtube-dl -f %d %s -o %s"  % (formatt, string,path )
        os.system(string2) 
        return
    else:
        string2 = "youtube-dl -f %d %s"  % (formatt, string )
        os.system(string2) 
        return

while(True):
    print ("1.Download\n2.Exit")
    choice = int(input(">"))
    if(choice!=1 and choice!=2):
        print ("invalide choice!!!!")
    if(choice==1):
        download()
    elif(choice==2):
        print ("GoodBye! :)")
        break



