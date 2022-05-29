from playsound import playsound
import multiprocessing
from rich.console import Console
from time import sleep

class GenFunc:
    """
    This GenFunc class contains functions.

    > play_song
    > animation
    
    """
    def __init__(self):
        self.console = Console()


    def play_song(self, songname:str) -> None:
        """This function will play music as per type, from default directory or current one"""

        self.console.print(f"[bold green]Playing[/bold green] - ([bold blue]{songname}[/bold blue])..")
        try:
            p = multiprocessing.Process(target=playsound, args=(songname,))
            p.start()
            self.console.input("\n[bold red]ENTER[/bold red] to stop playback.")
            p.terminate()
        except Exception as e:
            self.console.print(e)
            self.console.print("Internal module [bold red]error[/bold red] :sweat:")


    def animation(self):
        """This plays a animation of working in progress."""
        tasks = [i for i in range(1, 2)]

        with self.console.status("[bold green]Playing...") as status:
            while tasks:
                tasks.pop(0)
                sleep(1)

