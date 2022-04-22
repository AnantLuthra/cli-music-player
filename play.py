"""
Author - Anant Luthra
Date - 19/4/22
Purpose - To make a CLI music player.
"""

import multiprocessing
import os
import argparse, sys
from playsound import playsound

with open("help.txt", 'r') as f:
    HELP = f.read()

def handle_arg(args):
    """This function will handle case according to the argument passed by user"""


def play_music(type):
    """This function will play music as per type, from default directory or current one"""

def stop_music():
    """This function will stop music"""

def get_arg():
    """This function gets the argument from cli"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-h", type=bool, default=True, )
    parser.add_argument("-d", type=bool, default=True, help=HELP)
    parser.add_argument("-s", type=str, help=HELP)
    parser.add_argument("-t", type=bool, default=True, help=HELP)
    parser.add_argument("-g", type=bool, default=True, help=HELP)

    args = parser.parse_args()
    handle_arg(args)

if __name__ == "__main__":
    
    os.chdir(r"C:\Users\anant luthra")
    p = multiprocessing.Process(target=playsound, args=(r"Downloads\Adam Oh - Trapped In My Mind (Lyrics _ Lyric Video).mp3",))
    p.start()
    # playsound.playsound(r"Downloads\Adam Oh - Trapped In My Mind (Lyrics _ Lyric Video).mp3")
    input("")
    p.terminate()

