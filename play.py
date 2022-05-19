"""
Author - Anant Luthra
Date - 19/4/22
Purpose - To make a CLI music player.
"""

import multiprocessing
import argparse
import random
import os
from rich import print
from rich.console import Console
import playsound

class player:
    
    def __init__(self) -> None:
        self.console = Console()
        self.default_dir = r"C:\Users\anant luthra\Desktop\Important\Relax songs"
        
    def play_terminal(self, path):
        # For playing song in terminal.
        print("done in play_terminal")
        songs = [i for i in os.listdir(path) if i.endswith(".mp3")]
        a = f"({os.path.join(path,random.choice(songs))})"
        # print(a)

        print(os.path.isfile(a))
        p = multiprocessing.Process(target=playsound.playsound, args=(a),)
        p.start()
        # playsound.playsound(r"Downloads\Adam Oh - Trapped In My Mind (Lyrics _ Lyric Video).mp3")
        input("")
        p.terminate()
        return

    def play_gui(self, ):
        ...

    def read_help(self):
        path = os.getcwd()
        os.chdir(r"E:\Python\Python projects\CLI Music player")
        with open("help.txt", 'r') as f:
            os.chdir(path)
            return f.read()

    def handle_arg(self, args):
        """This function will handle case according to the argument passed by user"""

        if args.h:
            self.console.print(self.read_help(), style="bold green")

        elif args.c:

            songs = [i for i in os.listdir(os.getcwd()) if i.endswith(".mp3")]
            
            if not args.g and not args.t:
                self.console.print("Error: Argument missing '--g' or '--t'")
                return

            if songs == []:
                style = "bold red on black"
                self.console.print("\n--------------------Error---------------------",style = style, justify="center")
                self.console.print("\nNo available music files in the repository !!", style=style, justify="center")
                return
            
            if args.g and args.t:
                # If both GUI one and Terminal argument is passed.
                self.console.print("\n Both options can't be used select one 't' or 'g'", style=style)
                return

            if args.g:
                # Playing with GUI
                os.startfile(random.choice(songs))
                return

            elif args.t:
                # Playing in terminal
                self.play_terminal(os.getcwd())

        elif args.d:

            if args.t:
                self.play_terminal(self.default_dir)
            else:
                os.startfile([i for i in os.listdir(self.default_dir) if i.endswith(".mp3")][0])
                
            
        elif not args.c and not args.d and not args.s:
            self.console.print(self.read_help(), style="green")

    def play_music(self, type):
        """This function will play music as per type, from default directory or current one"""
        ...

    def stop_music(self):
        """This function will stop music"""

    def get_arg(self):
        """This function gets the argument from cli"""

        parser = argparse.ArgumentParser(description="A Tool that play music from you system", exit_on_error=False)
        parser.add_argument("--h", action="store_true", default=False)
        parser.add_argument("--d", action="store_true", help="This argument is for playing songs for default directory.", default = False)
        parser.add_argument("--s", type=str, help="This argument is for playing a specific song through passing it name.")
        parser.add_argument("--t", action="store_true", help="Set this true for playing song in terminal", default=False)
        parser.add_argument("--g", action="store_true", default=False, help="Set this true for playing song through windows gui")
        parser.add_argument("--c", action="store_true", default=False, help="For playing songs from the current directory.")

        args = parser.parse_args()
        self.handle_arg(args)


if __name__ == "__main__":

    cli_player = player()

    try:
        cli_player.get_arg()
    except Exception as e:
        print(e)

    # a = "Main Rang Sharbaton Ka [Slowed+Reverb] - Arijit Singh _ Music lovers _ Textaudio.mp3"
    # b = [i for i in os.listdir(os.getcwd()) if i.endswith(".mp3")]
    # # print(a, "\n", b[0])
    # # playsound.playsound(a)

    # p = multiprocessing.Process(target=playsound.playsound, args=(b[0],))
    # p.start()
    # # playsound.playsound(r"Downloads\Adam Oh - Trapped In My Mind (Lyrics _ Lyric Video).mp3")
    # input("")
    # p.terminate()