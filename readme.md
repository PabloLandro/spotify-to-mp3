# Spotify Playlist Downloader

![Spotify Playlist Downloader](https://img.shields.io/badge/Spotify-Playlist%20Downloader-green)

## Overview

`Spotify Playlist Downloader` is a Python application that downloads songs from a public Spotify playlist and saves them as MP3 files in a specified directory. This tool is useful for creating local copies of your favorite playlists for offline listening.

## Features

- Download songs from any public Spotify playlist.
- Save downloaded songs as MP3 files.
- Specify the output directory for downloaded files.

## Prerequisites

- Python 3.6 or higher

## Installation

    ```sh
    git clone https://github.com/yourusername/spotify-playlist-downloader.git
    cd spotify-playlist-downloader
    ```

## Configuration

    ```env
    OUTPUT_FOLDER=/path/to/your/output/directory
    URL=https://open.spotify.com/playlist/your_playlist_id
    ```

    Set `OUTPUT_FOLDER` to the path where you want the MP3 files to be saved. Set `URL` to the URL of the public Spotify playlist you want to download.

## Usage

Run the script to start downloading the playlist:

```sh
python main.py