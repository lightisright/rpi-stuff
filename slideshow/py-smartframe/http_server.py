from bottle import route, run
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
    return "Display random dir"

@route('/display/<dirname>')
def display(dirname):
    sf.display(dirname)
    return "Display dirname " + dirname

@route('/http/<filename>')
def return_res(filename):
    if os.path.isfile("./http-res/" + filename):
        file = open("./http-res/" + filename, 'r') 
        return file.read() 
    return error404(filename)

@route('/dirlst/')
def dirlst():
    return json.dumps(sf.dirIndex)

@route('/imglst/<dir>')
def imglst():
    return ""

@route('/delete/<dir>')
def delete():
    return ""

@route('/print/<dir>')
def print():
    return ""

@route('/showonphotoframe/<dir>')
def showonphotoframe(dir):
    return display(dir)

@app.error(404)  # changed from OP
def error404(error):
    return 'Nothing here, sorry'