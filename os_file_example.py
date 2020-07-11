import os
import json
from shutil import copyfile

print("Show me da weh")
#osPATH=input()
path="/home/vgeorga/docker/complex/complex/worker"
file1=""
for root, dirs, files in os.walk(path):
    for i in files:
        if i.endswith(".json"):
            print("file :", i)
            print("path :",os.path.join(root, i))
            file1 = os.path.join(root, i)

print("Changing directory to /tmp: ")
os.chdir('/tmp')
print("cwd: ", os.getcwd())
print("contents of /tmp: \n", os.listdir())
print("fspath:", os.fspath('/tmp'))

copyfile(file1, "./package.json")
if "package.json" in os.listdir():
    print("contents of /tmp after copy: \n", os.listdir())

with open('package.json') as f:
    data=json.load(f)

print('JSON data :', data)

print('redis version:', data['dependencies']['redis'])

data['dependencies']['redis']='3.2.0'

print('redis version after change:', data['dependencies']['redis'])

print('JSON data :', data)

# write changes to file
with open('package.json', 'w') as writefile:
    json.dump(data, writefile)