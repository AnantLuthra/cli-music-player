"""
Author - Anant Luthra
Date - 19/4/22
Purpose - To make a CLI music player.
"""

import multiprocessing
import argparse
import random
import os
from time import sleep
from rich import print
from rich.console import Console
from playsound import playsound
from rich.table import Table

class player:
    
    def __init__(self) -> None:
        self.console = Console()
        self.default_dir = r"C:\Users\anant luthra\Desktop\Important\Relax songs"
        self.table = Table(show_lines=True, show_header=True, title="LIST OF SONGS", style="bold")
        
    def animation(self):
        tasks = [i for i in range(1, 3)]

        with self.console.status("[bold green]Playing...") as status:
            while tasks:
                task = tasks.pop(0)
                sleep(1)

    def play_song(self, songname):
        """This function will play music as per type, from default directory or current one"""

        p = multiprocessing.Process(target=playsound, args=(songname,))
        p.start()
        self.console.input("press ENTER to stop playback")
        p.terminate()


    def present_table(self, songs) -> None:
        """This function will print beautiful table of songs"""
        
        self.table.add_column("S.No.", style="cyan", justify="center", width=5, footer_style="-")
        self.table.add_column("Song names", style="green")
            
        for i in range(len(songs)):
            self.table.add_row(str(i+1), songs[i])

        print(self.table)
        answer = int(self.console.input("Enter the S.No. of song which do you want to play: "))
        print()

    def play_terminal(self, path:str, option:bool):
        """For playing song in terminal from the given path."""

        a = [i for i in os.listdir(path) if i.endswith(".mp3")]
        os.chdir(path)
        if option: 
            self.present_table(a)


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

            elif songs == []:
                style = "bold red on black"
                self.console.print("\n--------------------Error---------------------",style = style, justify="center")
                self.console.print("\n:x: No available music files in the repository :x:", style=style, justify="center")
                return
            
            elif args.g and args.t:
                # If both GUI one and Terminal argument is passed.
                self.console.print("\n Both options can't be used select one 't' or 'g'", style=style)
                return

            elif args.g:
                self.animation()
                # Playing with GUI
                os.startfile(random.choice(songs))

            elif args.t:
                # Playing in terminal
                self.animation()
                if args.r: self.play_terminal(os.getcwd(), True)
                else: self.play_terminal(os.getcwd(), False)

        elif args.d:

            if args.t:
                self.animation()
                if args.r: self.play_terminal(self.default_dir, True)
                else: self.play_terminal(self.default_dir, False)
            else:
                self.animation()
                os.startfile(os.path.join(self.default_dir, random.choice([i for i in os.listdir(self.default_dir) if i.endswith(".mp3")])))
                
            
        elif not args.c and not args.d and not args.s:
            self.console.print(self.read_help(), style="bold green")


    def stop_music(self):
        """This function will stop music"""

    def get_arg(self):
        """This function gets the argument from cli"""

        parser = argparse.ArgumentParser(description="A Tool that play music from your system", exit_on_error=False)
        parser.add_argument("--h", action="store_true", default=False)
        parser.add_argument("--d", action="store_true", help="This argument is for playing songs for default directory.", default = False)
        parser.add_argument("--s", type=str, help="This argument is for playing a specific song through passing it name.")
        parser.add_argument("--t", action="store_true", help="Set this true for playing song in terminal", default=False)
        parser.add_argument("--r", action="store_true", help="Pass this argument for playing random song from chosen directory", default=False)
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