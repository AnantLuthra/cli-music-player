# CLI Music Player

## Features
- It is used for quickly playing music through terminal command
- I highly recommend you to set an alias of this in your windows 
- You can also download and play song which is not even before present in your computer.

## Requirements 
- Python 3.10 or higher

## Clone this repository

```git clone https://github.com/AnantLuthra/cli-music-player.git```

### Module used (External)
- rich = 11.1.0
- playsound = 1.2.2
- youtube_dl = 2021.12.17
- requests = 2.27.1
- os
- random
- argparse
- time
- multiprocessing
- urllib.request

---

## Commands

|Argument |      Description                                     |
| ------- |--------------------------------------------------    |
| `--help`| ->  For help                                         | 
| `--h`   | ->  For help                                         |  
| `--d`   | ->  To play music from default directory             | 
| `--dv`  | ->  Value of default directory                       | 
| `--s`   | ->  For playing specific song                        | 
| `--r`   | ->  For playing random song from chosen directory    | 
| `--t`   | ->  For playing music in terminal                    | 
| `--g`   | ->  For playing music through windows music player   | 
| `--c`   | ->  For playing songs from the current directory     |

---
### Usage

- `--d --g` = Just for playing song from default directory with using windows media player
- `--d --t` = For playing from default directory in terminal.
- `--d --t --r` = For playing random song from default directory in terminal
- `--c --g --r` = For playing random song from current directory using windows media player
![sample_gif](./previews/1.gif)

---
#### Using --s argument

- `play --s faded_alan_walker --g` = For downloading and playing song from youtube. Remember to search it by passing --s argument and value having `_` instead of space.
- And use `--g` argument for playing song while using `--s` argument instead of `--t` as it often time gives this error - _A problem occurred in initializing MCI_

![sample_gif2](./previews/2.gif)

---

#### Some other previews

![sample1](./previews/1.png)

---

- Using `--c --t --r` arguments.

![sample2](./previews/2.png)