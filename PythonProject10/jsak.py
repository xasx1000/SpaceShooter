from operator import truediv

import os
from subprocess import list2cmdline
from urllib.parse import clear_cache

list0 = ["a", "b", "c", "d", "e", "f", "g", "h"]
list2 = list()

# Search for index within defined list
item = list0.pop(0)
print (item)
item = list0.pop(-1)
print (item)
# A H gets generated

for item in list0:
    print ('z')
if "A" in list0:
    print ('b')
else:
    print ("no A")
    list0.insert(1,"A")
    print (list0.pop(1))
    print ("A has been succesfully implemented")
    digress1 = input ("do you want to get rid of A?")
    if digress1 == ["yes", "Yes", "YES"]:
        item = list0.pop(0)
        print (item)
        print ("A has been removed successfully")
    else:

        os.system("clear")

