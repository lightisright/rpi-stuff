import sys
import os
import random

class SmartFrame: 

    def __init__(self, imgPath, exec_sys_commands: bool):

        self.exec_sys_commands = exec_sys_commands
        self.imgPath = imgPath
        self.currentAlbum = ""

    def getCurrentAlbum(self):
        return self.currentAlbum

    def dirIndex(self):

        # List subdirectories
        photodirs = []
        for dirname in os.listdir(self.imgPath):
            if os.path.isdir(os.path.join(self.imgPath, dirname)) and dirname[0]!='.':
                photodirs.append(dirname)

        print(photodirs)

        return photodirs


    def _getRandomDir(self):

        photodirs = self.dirIndex()

        # find a random photo directory to show
        randDir = photodirs[random.randint(0, len(photodirs)-1)]

        print("Selected random directory: %s" % randDir)
        return randDir


    def display(self, dirname):

        dirpath = os.path.join(self.imgPath, dirname)

        print("Display slideshow: %s" % dirpath)

        if os.path.exists(dirpath):
            self.currentAlbum = dirname
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


    def displayRandomDir(self):
        slideshowDir = self._getRandomDir()
        self.display(slideshowDir)
        return slideshowDir
