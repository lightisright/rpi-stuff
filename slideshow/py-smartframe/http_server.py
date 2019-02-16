from bottle import route, run, app
import os.path
import json
import smartframe

sf = smartframe.SmartFrame("", False)

class HttpServer:

    def __init__(self, hostname, port, smartframe: smartframe.SmartFrame, debug):
        self.hostname = hostname
        self.port = port
        self.debug = debug
        global sf
        sf = smartframe

    def start(self):
        if self.debug:
            print('Slideshow HTTP server started - ', self.hostname, ':', self.port)
            
        run(host=self.hostname, port=self.port, debug=self.debug)



# BOTTLE ROUTES

@route('/')
def index():
    #return "py-smartframe HTTP server index !"
    return return_res("index.html")

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

@route('/http/<filename>')
def return_res(filename):
    if os.path.isfile("./http-res/" + filename):
        file = open("./http-res/" + filename, 'r') 
        return file.read() 
    return error404(filename)

@route('/albums/')
def albums():
    return json.dumps(sf.dirIndex)

@route('/albums/<album>/index/')
def album_index(album):
    return json.dumps(sf.imgIndex(album))

@route('/image/<album>/<filename>')
def display_image(album, filename):
    # TO BE DONE
    return "Display image:" + filename + " (album: " + album + ")"

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
