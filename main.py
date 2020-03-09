import config
from tracker import Tracker
import time
import threading
import sys
import json
import os

"""JSON and Thread for Tracker"""

def track():
    tracker = Tracker(config.to_track, config.RECIPIENT)
    while(True):
        tracker.check()
        time.sleep(config.TRACK_TIME)

def add_to_track(url, price):
    config.to_track[url] = price
    print('URL added')

def remove_from_track(url):
    if url in config.to_track.keys():
        del config.to_track[url]
        print("URL deleted")
    else:
        print("URL couldn't be deleted")

def write_json():
    with open(config.JSON_FILE, 'w+') as outfile:
        json.dump(config.to_track, outfile)

def load_json():
    with open(config.JSON_FILE, 'a+') as json_file:
        try:
            data = json.load(json_file)
            config.to_track = data
            print(f"Data loaded from {config.JSON_FILE}")
        except json.JSONDecodeError:
            pass

#Start

load_json()

thread = threading.Thread(target=track)
thread.daemon = True
thread.start()

while True:
    print("Waiting for Input...")
    userinput = input()
    command = userinput.split()
    if len(command) > 0:
        if command[0] == "trackeradd":
            print("Trackeraddcommand")
            try:
                add_to_track(command[1], command[2])
            except:
                pass
        elif command[0] == "trackerremove":
            try:
                remove_from_track(command[1])
            except:
                pass
        elif command[0] == "print":
            try:
                print(config.to_track)
            except:
                pass
        elif command[0] == "help":
            try:
                print()
                print("HELP:")
                print("trackeradd {url} {price}")
                print("trackerremove {url}")
                print("trackerend")
            except:
                pass
        elif command[0] == "end":
            write_json()
            break

    print()