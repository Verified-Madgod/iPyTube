from pytube import YouTube
from pytube import Playlist
import platform
import os

def clear():
    if platform.system().lower() == "windows":
        os.system('cls')
    else:
        os.system('clear')

def download_video(URL):
    yt = YouTube(URL)
    print("Downloading %s...\n" % yt.title)
    yt.streams.first().download()
    print("Done! Exiting...")

def download_playlist(URL):
    playlist = Playlist(URL)
    print("Downloading '%s' playlist...\n" % playlist.title())
    playlist.download_all()
    print("Done! Exiting...")

def header():
    clear()
    print("-"*60)
    print("--------          YouTube Video Downloader          --------")
    print("-"*60)

if __name__ == '__main__':
    header()
    print("\t1. Download Video")
    print("\t2. Download Playlist")
    print("\t3. Quit")
    c = input("> ")

    if c == "1":
        header()
        URL = input("Please Enter the Video URL: ")
        download_video(URL)

    elif c == "2":
        header()
        URL = input("Please Enter the Playlist URL: ")
        download_playlist(URL)

    else:
        Quit()
