from os import listdir
from os.path import isfile, join
mypath = "./"
onlyfiles = [f for f in listdir(mypath) if not isfile(join(mypath, f)) and f[0] != "."]

print(onlyfiles)