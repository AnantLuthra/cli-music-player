"""
Author - Anant Luthra
Date - 19/4/22
Purpose - To make a CLI music player.
"""

import multiprocessing
import os
import argparse, sys
from playsound import playsound

def read_help():
    path = os.getcwd()
    os.chdir(r"E:\Python\Python projects\CLI Music player")
    with open("help.txt", 'r') as f:
        os.chdir(path)
        return f.read()

def handle_arg(args):
    """This function will handle case according to the argument passed by user"""

    if args.h == True:
        print(read_help())

    elif args.d and args.t:
        play_music("d")

def play_music(type):
    """This function will play music as per type, from default directory or current one"""

    if type == "d":
        
        os.chdir(r"C:\Users\anant luthra")
        p = multiprocessing.Process(target=playsound, args=(r"Downloads\Adam Oh - Trapped In My Mind (Lyrics _ Lyric Video).mp3",))
        p.start()
        # playsound.playsound(r"Downloads\Adam Oh - Trapped In My Mind (Lyrics _ Lyric Video).mp3")
        input("")
        p.terminate()

def stop_music():
    """This function will stop music"""

def get_arg():
    """This function gets the argument from cli"""

    os.chdir(r"E:\Python\Python projects\CLI Music player")
    with open("help.txt", 'r') as f:
        HELP = f.read()

    parser = argparse.ArgumentParser()
    parser.add_argument("--h", type=bool)
    parser.add_argument("--d", type=bool, help=HELP, default = False)
    parser.add_argument("--s", type=str, help=HELP)
    parser.add_argument("--t", type=bool, help=HELP, default=True)
    parser.add_argument("--g", type=bool, default=False, help=HELP)

    args = parser.parse_args()
    handle_arg(args)

if __name__ == "__main__":
    try:
        get_arg()
    except Exception as e:
        print(e)

    print(os.getcwd())

