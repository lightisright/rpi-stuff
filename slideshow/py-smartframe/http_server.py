from bottle import route, run
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
    return "py-smartframe HTTP server index !"

@route('/current/')
def current():
    return "Current album: " + sf.getCurrentAlbum()

@route('/random/')
def random():
    sf.displayRandomDir()
    return "Display random dir"

@route('/display/<dirname>')
def greet(dirname):
    sf.display(dirname)
    return "Display dirname " + dirname

