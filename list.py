from os import listdir
from os.path import isfile, join
mypath = "/Users/spark/PhpstormProjects/AssessmentProjectLaravel/storage/app/public/profiles/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print("$mans = [")
for img in onlyfiles:
    print("\'/storage/profiles/" + img + "\',")
print("]")