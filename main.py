#delete prev file
#rename curr file as prev file
#create curr file
#compare curr and prev files

from get_from_moodle import main
from compare import compare
import os
import shutil
import getpass

username = input("username: ")
password = getpass.getpass("password : ", stream=None)

main(username, password)
while(True):
    os.system("rm -r prev.txt")
    os.rename("curr.txt", "prev.txt")
    main(username, password)
    curr = open("curr.txt", "r")
    prev = open("prev.txt", "r")
    compare(curr, prev)