#!/usr/bin/python3
# encoding: utf-8
import os
import time
import subprocess

inputpath = "file-to-import.opml"
outputpath = "feeds-imported.txt"
backuppath = "empty"
urls = []

with open(inputpath, "r") as input_raw:
    lines = input_raw.readlines()
    for line in lines:
        if "xmlUrl" in line:
            targetUrl = line.split("xmlUrl=\"",1)[1].split("\"")[0]
            urls.append(targetUrl)

print("URLs found:") 
for url in urls:
    print(url)

if os.path.isfile(outputpath):
    now = time.strftime("%Y-%m-%d")
    backuppath = outputpath + ".bak-" + now
    print("Output file already exists and will be moved to " + backuppath)

yn = input("Write to " + outputpath + "? (y/n) ")

if yn.lower() == "y" or yn.lower() == "yes":
    print("okeydokes")
    if backuppath is not "empty":
        print("Making backup...")
        subprocess.run(["mv", outputpath, backuppath])

    print("Saving file...") 
    with open(outputpath, "w") as outfile:
        for url in urls:
            outfile.write(url + "\n")
    print("Done.")

else:
    print("Aborting.")
    exit()