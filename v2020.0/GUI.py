#!/usr/bin/env python

__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__company__ = "Robotic Beverage Technologies, Inc"
__status__  = "Development"
__date__    = "Late Updated: 2020-03-02"
__doc__     = "Logic to run Flask based GUI front-end for CoCoTaps"

# Useful system jazz
import sys, traceback, argparse, string

#TODO REMOVE? from time import sleep

# Allows for the creation of a GUI web app that communicates with python backend code
# Saves HTML files in a folder called "templates" in the same folder as your Flask code
# Saves user state / data across page refreshes and crashes, by using browser cookies
from flask import Flask, render_template, session

# Robotic Beverage Technologies code for custom data logging and terminal debugging output
from Debug import *
#TODO import Drink

# Make a Flask application and start running code from __main__
app = Flask(__name__)
app.secret_key = 'FreshCoConuts@42'			# TODO Select STRONG key for production code
app.config['SESSION_TYPE'] = 'filesystem'	# TODO Fix Image URL filepath code in welcome.html

@app.route('/')
def WelcomeScreen():
	HTMLtoDisplay = "welcome.html"
	return render_template(HTMLtoDisplay)

def WaitingScreen():
	HTMLtoDisplay = "waiting.html"
	return render_template(HTMLtoDisplay)

def CompleteScreen():
	HTMLtoDisplay = "complete.html"
	return render_template(HTMLtoDisplay)

if __name__ == '__main__':
    d = Debug(True)
    if(d.GetMode == True):
	    # Allow URLs to be refreshed (F5) without restarting web server after code changes
	    app.run(debug=True) # check_call("export FLASK_DEBUG=1", shell=True)
    else:
	    app.run(debug=False) # check_call("export FLASK_DEBUG=0", shell=True)
	    app.run(host='0.0.0.0')

    WelcomeScreen()
    #TODO IF BUTTON PRESSED
    #WaitingScreen()
    #CompleteScreen()
