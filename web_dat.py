import multiprocessing
import urllib.request
import re
import youtube_dl
import os
from playsound import playsound
from rich.console import Console
from rich import print

class WebDat:

    def __init__(self) -> None:
        self.console = Console()


    def __play_song(self, songname:str) -> None:
        """This function will play music as per type, from default directory or current one"""

        print(f"[bold green]Playing[/bold green] - ([bold blue]{songname}[/bold blue])..")
        try:
            p = multiprocessing.Process(target=playsound, args=(songname,))
            p.start()
            self.console.input("\n[bold red]ENTER[/bold red] to stop playback.")
            p.terminate()
        except Exception as e:
            self.console.print(e)
            self.console.print("Internal module [bold red]error[/bold red] :sweat:")


    def __search_input_constructor(self, search:str) -> int:
        """This function takes no argument and returns a search string."""

        if len(search.split("_")) != 1:
            search = search.split("_")
            return "+".join(search)
        
        else: return search


    def __search_yt(self, query:str) -> str:
        """This function searches that query on youtube and returns the url of top result"""
        if query != "":
            html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={query}")
            video_ids = re.findall(r"watch\?v=(\S{11})",html.read().decode())
            return f"https://youtube.com/watch?v={video_ids[0]}" # Returning top resulted video.


    def __download_mp_file(self, link:str) -> str:
        """This functin downloads the given videos's youtube link in .mp3 format"""

        video_info = youtube_dl.YoutubeDL().extract_info(
            url = link, download = False
        )
        ydl_opts = {
                'format': 'bestaudio/best',
                'keepvideo': False,
                'outtmpl': f"{video_info['title']}.mp3"
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_info['webpage_url']])

        return f"{video_info['title']}.mp3"


    def __play_down_music(self, a:str, type:str, filename:str) -> None:
        """This function plays the song which is downloaded from youtube as per user's search"""

        if type == 'g': os.startfile(f"{filename}")
        else:
            self.__play_song(filename)


    def search_n_play_song(self, type:str, search:str):
        """This function searches the song name and download and play it in terminal or through windows music player
        as per the type argument."""

        a = self.__search_input_constructor(search)         # Preparing input for search.

        song = self.__download_mp_file(self.__search_yt(a)) # Downloading song.

        # Playing that song.
        if type == 't' or type == 'g':
            self.__play_down_music(a, type, song)
        else:
            raise Exception("type argument must be 't' or 'g'")

