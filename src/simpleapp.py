from flask import Flask
import sys
import optparse
import time


app = Flask(__name__)

start = int(round(time.time()))

@app.route("/")
def hello_world():

    return "Hello world!!"

if __name__ == '__main__':
    parser = optparse.OptionParser(usage="python simpleapp.py -p ")
    parser.add_option('-p', '--port', action='store', dest='port', help='The port to listen on.')
    app.run(host='0.0.0.0', port=8000, debug=False)
