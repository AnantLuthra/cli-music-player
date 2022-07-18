"""
Author - Anant Luthra
Date - 19/4/22
Purpose - To make a CLI music player.
"""

import argparse
import random
import os
import difflib
from rich import print
from rich.console import Console
from rich.table import Table
from web_dat import WebDat
from pl_song import GenFunc


class Player:
    """
    This is a CLI tool for playing song from your system.

    Arguments available :-

    --help :For help
    --h    :For help
    --d    :To play music from default directory
    --dv   :Value of default directory
    --s    :For playing specific song
    --r    :For playing random song from chosen directory
    --t    :For playing music in terminal
    --g    :For playing music through windows music player
    --c    :For playing songs from the current directory

    """

    def __init__(self) -> None:
        self.console = Console()
        self.webdat = WebDat()
        self.__default_dir = [r"C:\Users\anant luthra\Desktop\Important\Relax songs", r"D:\d data\New songs", r"D:\d data\NCS music"]
        self.__table = Table(show_lines=True, show_header=True, title="LIST OF SONGS", style="bold")
        self.main_funcs = GenFunc()
        

    def __present_table(self, songs:list) -> str:
        """This function will print beautiful table of songs"""
        
        self.__table.add_column("ID", style="cyan", justify="center", width=5, footer_style="-")
        self.__table.add_column("Song names", style="green")
            
        for i in range(len(songs)):
            self.__table.add_row(str(i+1), songs[i])

        print(self.__table)
        answer = self.console.input("Enter the [bold green]ID[/bold green] of song which do you want to play: ")
        self.main_funcs.animation()
        if answer == "":
            self.console.print("[bold red]ID[/bold red] can't be [bold red]empty[/bold red] :expressionless:")
            exit()

        if int(answer) > len(songs) or int(answer) < 1:
            self.console.print("[bold red]Invalid[/bold red] ID entered :expressionless:")
            exit()

        return songs[int(answer) -1]

    
    def __search_local(self, word:str) -> dict:
        """
        This function searches the song passed as word argument across all the default
        directories one by one.
        """
        
        all_matches = {}
        word = word.split()

        # Todo: Solve bugs.
        # Use another approach for searching song in directories.
        for i in self.__default_dir:

            for j in word:
                matches = difflib.get_close_matches([j.lower()], 
                        [j.lower() for j in os.listdir(i) if j.endswith(".mp3")], n=10, cutoff=0.20)
                        
                print(matches)
                if matches != []:

                    all_matches[i] = matches
                    # Then you have to just play the song.

        print(all_matches)
        


    def __play_terminal(self, path:str, option:bool):
        """For playing song in terminal from the given path."""

        a = [i for i in os.listdir(path) if i.endswith(".mp3")]
        os.chdir(path)

        ## Playing song according to --r argument 'random or not' ##
        if option:
            self.main_funcs.play_song(random.choice(a))
        else:
            self.main_funcs.play_song(self.__present_table(a))

    def __read_help(self) -> str:
        path = os.getcwd()
        os.chdir(r"E:\Python\Python projects\CLI Music player")
        with open("help.txt", 'r') as f:
            os.chdir(path)
            return f.read()

    def __handle_arg(self, args):
        """This function will handle case according to the argument passed by user"""

        if args.h:
            self.console.print(self.__read_help(), style="bold green")
            return
        
        if args.dv > len(self.__default_dir) - 1 or args.dv < 0:
            print("[bold red]Wrong[/bold red] default path [bold red]value[/bold red] entered :x:")
            exit()

        if not args.c and not args.d and not args.s:
            self.console.print(self.__read_help(), style="bold green")

        elif args.c:
            ## Playing song from current directory ##
            songs = [i for i in os.listdir(os.getcwd()) if i.endswith(".mp3")]
            
            if not args.g and not args.t:
                self.console.print("Error: Argument missing '--g' or '--t'")
                return

            elif songs == []:
                style = "bold red on black"
                self.console.print("\n--------------------Error---------------------",style = style, justify="center")
                self.console.print("\n:x: No available music files in the repository :x:", style=style, justify="center")
                return

            elif args.t:
                # Playing in terminal
                self.main_funcs.animation()
                if args.r: self.__play_terminal(os.getcwd(), True)
                else: self.__play_terminal(os.getcwd(), False)

            
            elif args.g:
                self.main_funcs.animation()
                # Playing with windows music player
                if args.r: os.startfile(random.choice(songs))
                else: os.startfile(self.__present_table(songs))

            

        elif args.d:
            ## Playing song from default directory ##

            if not args.g and not args.t:
                self.console.print("[bold red]Error[/bold red]: Argument [bold red]missing[/bold red] '--g' or '--t'")
                return
            
            if args.t:
                self.main_funcs.animation()
                if args.r: self.__play_terminal(self.__default_dir[args.dv], True)
                else: self.__play_terminal(self.__default_dir[args.dv], False)
            else:

                # Playing through GUI
                self.main_funcs.animation()
                if args.r: os.startfile(os.path.join(self.__default_dir[args.dv], random.choice([i for i in os.listdir(self.__default_dir[args.dv]) if i.endswith(".mp3")])))
                else: os.startfile(os.path.join(self.__default_dir[args.dv], self.__present_table([i for i in os.listdir(self.__default_dir[args.dv]) if i.endswith(".mp3")])))

        elif not args.d and not args.c and args.s:

            ## Checking if both arguments are passed.
            if args.w and args.l:
                self.console.print("[bold red]Error[/bold red]: Using both arguments at once! Use one arguement [bold white]'--w'[/bold white] or [bold white]'--l'[/bold white]")
                return

            ## Searching song online and downloading it and playing it.
            if args.w:          ## Searching on web with --w argument.
                self.main_funcs.animation()
                if args.t: self.webdat.search_n_play_song('t', args.s)                       # Playing through terminal
                else: self.webdat.search_n_play_song('g', args.s)                            # Playing through windows GUI

            elif args.l:
                ## Search and play song
                self.__search_local(args.s)

            else:
                self.console.print("[bold yellow]Warning[/bold yellow]: Atleast use one argument [bold white]'--w'[/bold white] or [bold white]'--l'[/bold white]")

                self.console.print("Searching on local system...", style="italic green")
                self.__search_local((args.s).replace("_", " "))


    def get_arg(self):
        """This function gets the argument from cli"""

        parser = argparse.ArgumentParser(description="A Tool that play music from your system", exit_on_error=False)
        parser.add_argument("--h", action="store_true", default=False)
        parser.add_argument("--d", action="store_true", help="This argument is for playing songs for default directory.", default = False)
        parser.add_argument("--s", type=str, help="This argument is for playing a specific song through passing it name.")
        parser.add_argument("--dv", type=int, help="Value of default directory", default=0)
        parser.add_argument("--t", action="store_true", help="Set this true for playing song in terminal", default=False)
        parser.add_argument("--r", action="store_true", help="Pass this argument for playing random song from chosen directory", default=False)
        parser.add_argument("--g", action="store_true", default=True, help="Set this true for playing song through windows gui")
        parser.add_argument("--c", action="store_true", default=False, help="For playing songs from the current directory.")
        parser.add_argument("--w", action="store_true", default=False, help="For search & play song from web.")
        parser.add_argument("--l", action="store_true", default=False, help="For searching songs in local system.")
        args = parser.parse_args()
        self.__handle_arg(args)


if __name__ == "__main__":

    cli_player = Player()
    try:
        cli_player.get_arg()
    except Exception as e:
        print(e)