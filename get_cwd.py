import os

print(os.getcwd())

results=print(os.listdir('/home/vgeorga')[0])

print(type(os.listdir()))

print("Give us a path love >")
path=input()

for root, dirs, files in os.walk(path):
    for i in files:
        print(i)