from bottle import Bottle, route, run, error, static_file
import os.path
import json
import smartframe
from threading import Thread

app = application = Bottle()

class HttpServer(Thread):

    def __init__(self, smartframe: smartframe.SmartFrame, hostname, port, debug):
        Thread.__init__(self)
        self.hostname = hostname
        self.port = port
        self.debug = debug
        global sf
        sf = smartframe

    def run(self):     
        run(host=self.hostname, port=self.port, debug=self.debug)



# BOTTLE ROUTES

@route('/')
@route('/index/')
@route('/home/')
def index():
    #return "py-smartframe HTTP server index !"
    return display_resource("index.html")

@route('/current/')
def current():
    global sf
    return "Current album: " + sf.getCurrentAlbum()

@route('/random/')
def random():
    global sf
    sf.displayRandomDir()
    return "Display random album"

@route('/display/<album>')
def display(album):
    global sf
    sf.display(album)
    return "Currently displaying album: " + album

@route('/res/<filename>')
def return_res(filename):
    return display_resource("res/" + filename)

def display_resource(filename):
    path = os.path.abspath(__file__)
    dir_path = os.path.dirname(path)
    return static_file(filename, root=dir_path+'/http-res/')

@route('/albums/')
def albums():
    global sf
    return json.dumps(sf.dirIndex())

@route('/albums/<album>/index/')
def album_index(album):
    global sf
    return json.dumps(sf.imgIndex(album))

@route('/image/<album>/<filename>')
def display_image(album, filename):
    global sf
    return static_file(filename, sf.getAlbumPath(album))

@route('/print/<album>/<filename>')
def print(album, filename):
    global sf
    if sf.printImage(album, filename):
        return "Image added to print file list"
    return "Error"

@route('/delete/<album>/<filename>')
def delete(album, filename):
    global sf
    if sf.deleteImage(album, filename):
        return "Image deleted & added to delete file list"
    return "Error"

@app.error(404)  # changed from OP
def error404(error):
    return 'Nothing here, sorry'
