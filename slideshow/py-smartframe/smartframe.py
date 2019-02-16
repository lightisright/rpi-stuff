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
                photodirs.append({"dirID": dirname, "dirname": dirname})

        return photodirs


    def imgIndex(self, dirname):

        # List subdirectories
        imglst = []
        dirpath = os.path.join(self.imgPath, dirname)
        if os.path.isdir(dirpath):
            for f in os.listdir(dirpath):
                if os.path.isfile(os.path.join(dirpath, f)):
                    imglst.append({"imgID": f, "filename": "image/" + dirname + "/" + f})

        return imglst


    def getImage(self, dirname, filename):
        """ Dumps image file content for display """
        imgpath = os.path.join(self.imgPath, dirname, filename)
        if os.path.isfile(imgpath):
            file = open(imgpath, 'rb') 
            return file.read()
        return "File doesn't exist"


    def _getRandomDir(self):

        photodirs = self.dirIndex()

        # find a random photo directory to show
        randDir = photodirs[random.randint(0, len(photodirs)-1)]

        print("Selected random directory: %s" % randDir['dirname'])
        return randDir['dirname']


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
            os.system("fbi -T 2 -noverbose --autodown -t 6 %s/* > /dev/null" % dirpath)
            # other fbi test with os.call
            ##call(["nohup", "fbi", "-T 2", "", "", "", "",])

        return msg


    def displayRandomDir(self):
        slideshowDir = self._getRandomDir()
        self.display(slideshowDir)
        return slideshowDir
