import sys
import os
import random

class smartframe: 

    def __init__(self, exec_sys_cmd: bool):

        self.exec_sys_commands = exec_sys_cmd

    def dirIndex(self, imgPath):

        # List subdirectories
        photodirs = []
        for dirname in os.listdir(imgPath):
            if os.path.isdir(os.path.join(imgPath, dirname)) and dirname[0]!='.':
                photodirs.append(dirname)

        print(photodirs)

        return photodirs


    def getRandomDir(self, imgPath):

        photodirs = self.dirIndex(imgPath)

        # find a random photo directory to show
        randDir = photodirs[random.randint(0, len(photodirs)-1)]

        print("Selected random directory: %s" % randDir)
        return randDir


    def display(self, dirpath):

        print("Display slideshow: %s" % dirpath)

        if os.path.exists(dirpath):
            msg = "Display slideshow: %s\n" % dirpath
        else:
            msg = "Directory doesn't exist: %s\n" % dirpath

        if self.exec_sys_commands:
            os.system("killall fbi && sleep 5")
            ##os.sleep(5)
            # nohup fbi -T 2 -noverbose --autodown -t 6 $RDMDIR/* > /dev/null
            os.system("nohup fbi -T 2 -noverbose --autodown -t 6 %s/* > /dev/null" % dirpath)
            # other fbi test with os.call
            ##call(["nohup", "fbi", "-T 2", "", "", "", "",])

        return msg


    def displayRandomDir(self, imgPath):
        slideshowDir = self.getRandomDir(imgPath)
        self.display(os.path.join(imgPath, slideshowDir))
        return slideshowDir
