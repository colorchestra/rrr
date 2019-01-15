#!/usr/bin/python3
# encoding: utf-8

import feedparser
import time
import sys
import os

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

timenow = time.time()
timelimit = 24    # number of hours before posts expire
cachepath = "cache.txt"
feedspath = "feeds.txt"
versionsOnly = False    # debug tool to show only names and rss/atom versions of feeds

if time.strftime("%w") == "1":
        print("montag fick ja")
        timelimit = 72

if not os.path.isfile(feedspath):
        feedspath = "feeds.txt.example"

with open(feedspath, "r") as feedsfile:
        feeds = feedsfile.readlines()

def formatOutput(index, mediumtitle, article):
    output = color.BOLD + str(index).ljust(5) + color.END + article.published + "\n     " + mediumtitle + "\n     " + article.title + "\n     " 
    if not article.description.startswith("<"):         # don't print html descriptions
            output = output + article.description + "\n"
    print(output)

def handleArguments():
        if len(sys.argv) == 2:
                if sys.argv[1] == "-h" or sys.argv[1] == "--help":
                        printHelp()
                        exit()


        with open(cachepath, "r") as cachefile:
            lines = cachefile.readlines()
            for arg in range(1, len(sys.argv)):
                if not sys.argv[arg].isdigit():
                    print(sys.argv[arg] + " is not a number!")
                else:
                    print("Opening article " + sys.argv[arg] + "...")
                    os.system("xdg-open " + lines[int(sys.argv[arg])])
        exit()

def printHelp():
        print("You are using rrr.")
        print("Use no arguments to update your feeds")
        print("Use the numbers next to the articles as arguments to open them in your favourite browser")
        print("Put your feeds (line by line, only the URL) into your feeds file")
        print("More features (maybe) to come.")

def updateFeeds():
        cachestring = ""
        index = 0
        for f in feeds:
            d = feedparser.parse(f)
            if not versionsOnly:        # see versionsOnly above. if condition can be removed once all rss and atom versions work
                print(color.BOLD + d['feed']['title'] + color.END)
                for e in d.entries:
                    published_time = time.mktime(e.published_parsed)
                    if int(time.time() - published_time) < int(timelimit * 60 * 60):
                        formatOutput(index, d['feed']['title'], e)
                        cachestring = cachestring + e.link + "\n"
                        index += 1
            else:
                print(color.BOLD + d['feed']['title'] + color.END + d.version)

        with open(cachepath, "w") as cachefile:
                cachefile.write(cachestring)

# main

# check if arguments are present. if not, do the usual feed update thing
if len(sys.argv) > 1:
        handleArguments()

# cache file should be deleted upon each update
try:
        os.remove(cachepath)
#        print("DEBUG Cache file deleted")
except:
        print("DEBUG No cache file found")

updateFeeds()

exit()