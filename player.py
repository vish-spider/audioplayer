import sys
import os
import PyQt5.QtCore as QtCore
import PyQt5.QtMultimedia as MultiMedia
from mutagen.easyid3 import EasyID3
import xml.etree.ElementTree as ET
import pycurl
from pyPodcastParser.Podcast import Podcast
import requests
from urllib.request import urlretrieve

class podCastDownloader(object):
    def __init__(self):
        self.file = os.path.join(os.getcwd(),"podcastlist.xml")
        print (self.file)
        self.listPodCasts() 
        
        
        
    def listPodCasts(self):

        tree = ET.parse(self.file)
        root = tree.getroot()    
        self.podcastList = []
        for podcasts in root.findall('pod'):
            name = podcasts.get('name')
            url = podcasts.get('url')
            self.podcastList.append(str(name) + "#@!" + str(url))
        i=1 
        for rows in self.podcastList:
            name,url = rows.split("#@!")
            print (str(i) + ":" +name + " : URL == " + url)
            i=i+1
        sel = int(input("Enter Podcast Number : "))
        print (len(self.podcastList))
        if int(sel) in range (1, len(self.podcastList)+1):
            self.getPodcastEpisodes(self.podcastList[sel-1])
        else:
            print ("incorrect range")


    def getPodcastEpisodes(self,pod):
        name,loc = pod.split("#@!")
        response = requests.get(loc)
        podcast = Podcast(response.content)
        os.system('cls')
        print ("-------------------------------------------------------------")
        print (podcast.title)
        print ("-------------------------------------------------------------")
        i = 1
        for episodes in podcast.items:
            print (str(i) + ": " + episodes.title)
            i = i+1
        selection = int(input("Enter Podcast No. : "))
        os.system("cls")
        print ("-------------------------------------------------------------")
        print (podcast.items[selection-1].title)
        print ("-------------------------------------------------------------")
        print (podcast.items[selection-1].itunes_subtitle)
        remoteurl = podcast.items[selection-1].enclosure_url
        print (remoteurl)
        print ("downloading")
        urlretrieve (remoteurl)
        print ("downloadComplete")

        

podCastDownloader()

