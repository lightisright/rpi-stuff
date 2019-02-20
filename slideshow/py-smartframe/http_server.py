from bottle import Bottle, route, run, error, static_file
import os.path
import json
import smartframe

sf = smartframe.SmartFrame("", False)

app = application = Bottle()

class HttpServer:

    def __init__(self, hostname, port, smartframe: smartframe.SmartFrame, debug):
        self.hostname = hostname
        self.port = port
        self.debug = debug
        global sf
        sf = smartframe

    def start(self):     
        run(host=self.hostname, port=self.port, debug=self.debug)



# BOTTLE ROUTES

@route('')
@route('/')
@route('/index')
@route('/home')
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
    # TO BE DONE
    return sf.getImage(album, filename)

@route('/print/<album>/<filename>')
def print(album, filename):
    # TO BE DONE
    return "Add image to print list:" + filename + " (album: " + album + ")"

@route('/delete/<album>/<filename>')
def delete(album, filename):
    # TO BE DONE
    return "Add image to delete list:" + filename + " (album: " + album + ")"

@app.error(404)  # changed from OP
def error404(error):
    return 'Nothing here, sorry'
