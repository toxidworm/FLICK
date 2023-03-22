from colorama import Fore, init
from bottle import *
from art import *
import json
init()

print(Fore.RED)
tprint("flick", font="sub-zero")
print(Fore.RESET)
print("knock knock... who's there? FAILURE!\n")

sourcefile = input(Fore.CYAN + "Source filename (to download) (~) > ")

sourceroot = input(Fore.CYAN + "Source filename root folder (~) > ")

downloadfile = input(Fore.CYAN + "Download filename (~) > ")

errormsg = input(Fore.YELLOW + "Error message (~) > ")

print(Fore.GREEN + "Great! Starting server")

print(Fore.RESET)

app = Bottle()

@app.route("/")
def index():
    return "Online!"

@app.route("/<key>")
def key_handler(key):
    with open("keys.json", "r") as confile:
        config = json.load(confile)
    if key == config['key']:
        return static_file(sourcefile, sourceroot, download=downloadfile)
    return errormsg

run(app, host="0.0.0.0", port="80")