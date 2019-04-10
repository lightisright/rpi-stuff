from bottle import Bottle, route, run, error, static_file
import os.path
import json
import smartframe

app = application = Bottle()

class HttpServer:

    def __init__(self, smartframe: smartframe.SmartFrame, hostname, port, debug):
        self.hostname = hostname
        self.port = port
        self.debug = debug
        global sf
        sf = smartframe

    def start(self):     
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
    return "Current album: " + sf.getCurrentAlbum()

@route('/random/')
def random():
    sf.displayRandomDir()
    return "Display random album"

@route('/display/<album>')
def display(album):
    sf.display(album)
    return "Currently displaying album: " + album

@route('/res/<filename>')
def return_res(filename):
    return display_resource("res/" + filename)

def display_resource(filename):
    return static_file(filename, root='./http-res/')

@route('/albums/')
def albums():
    return json.dumps(sf.dirIndex())

@route('/albums/<album>/index/')
def album_index(album):
    return json.dumps(sf.imgIndex(album))

@route('/image/<album>/<filename>')
def display_image(album, filename):
    return static_file(filename, sf.getAlbumPath(album))

@route('/print/<album>/<filename>')
def print(album, filename):
    if sf.printImage(album, filename):
        return "Image added to print file list"
    return "Error"

@route('/delete/<album>/<filename>')
def delete(album, filename):
    if sf.deleteImage(album, filename):
        return "Image deleted & added to delete file list"
    return "Error"

@app.error(404)  # changed from OP
def error404(error):
    return 'Nothing here, sorry'
