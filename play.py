"""
Author - Anant Luthra
Date - 19/4/22
Purpose - To make a CLI music player.
"""

import multiprocessing, os, argparse, sys, rich
from playsound import playsound

def read_help() -> str:
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

    elif args.c:

        for i in os.listdir(os.getcwd()):
            if i.endswith(".mp3"): break           
        else:
            print("No available music files in the repository.")
            return
        
        

    elif not args.c and not args.d and not args.s:
        print(read_help())

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

    parser = argparse.ArgumentParser(description="A Tool that play music from you system", exit_on_error=False)
    parser.add_argument("--h", action="store_true")
    parser.add_argument("--d", action="store_true", help="This argument is for playing songs for default directory.", default = False)
    parser.add_argument("--s", type=str, help="This argument is for playing a specific song through passing it name.")
    parser.add_argument("--t", action="store_true", help="Set this true for playing song in terminal", default=True)
    parser.add_argument("--g", action="store_true", default=False, help="Set this true for playing song through windows gui")
    parser.add_argument("--c", action="store_true", default=False, help="For playing songs from the current directory.")

    args = parser.parse_args()
    handle_arg(args)


if __name__ == "__main__":
    try:
        get_arg()
    except Exception as e:
        print(e)