import time
import os

from dotenv import load_dotenv

from moviepy.editor import VideoFileClip

from progress_bar import Progress_bar

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from pytube import Search

URL = "https://open.spotify.com/playlist/1KXjpX2gpUy9Peap7wTSgu?si=82adfdac3c4540e0"

TRACKLIST_CSS = 'div[role=grid][data-testid=playlist-tracklist].oIeuP60w1eYpFaXESRSg.oYS_3GP9pvVjqbFlh9tq > div[role=presentation].JUa6JJNj7R_Y3i4P8YUX > div[role=presentation][style="transform: translateY(0px);"]'

songs = []
size = 0

output_path = "./Songs"

def init_driver():
    options = Options()

    # Opciones de ventana
    #options.add_argument("--start-maximized")

    # Ignorar errores de certificados
    options.add_argument('--ignore-certificate-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.accept_insecure_certs = True

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    driver.minimize_window()

    driver.implicitly_wait(2)
    return driver

def get_songs():
    # Find the tracklist element
    song_container = driver.find_element(By.CSS_SELECTOR, TRACKLIST_CSS)
    song_rows = song_container.find_elements(By.CSS_SELECTOR, 'div[role=row]')
    
    # Iterate over every song on the playlist
    for row in song_rows:
        song = {}
        song = {
            "title": row.find_element(By.CSS_SELECTOR, 'div[data-encore-id=text]').text,
            "artist": row.find_element(By.CSS_SELECTOR, 'a[draggable=true][dir=auto]').text
        }
        songs.append(song)

def file_name(song):
    return song["title"] + ' - ' + song["artist"]

def download_songs():
    bar = Progress_bar(total=len(songs), text="songs downloaded")
    for song in songs:
        s = Search(song["title"] + ' ' + song["artist"])

        # Select the stream with highest bitrate
        stream = s.results[0].streams.get_audio_only()

        # We can convert it directly to mp3 as it's audio-only
        stream.download(output_path=output_path, filename=file_name(song)+'.mp3')
        bar.increment()

def mp4_to_mp3():
    for song in songs:
        song_path = os.path.join(output_path, file_name(song))

        # Load the video file
        video = AudioFileClip(song_path+'.mp4')

        # Extract the audio
        audio = video.audio
        
        # Write the audio to an mp3 file
        #audio.write_audiofile(song_path+'.mp3')
        
        # Close the video and audio objects
        audio.close()
        video.close()


try:
    driver = init_driver()

    driver.get(URL)

    # We wait for the page to load as it's a web application
    time.sleep(10)

    get_songs()

    driver.close()

    download_songs()

    #mp4_to_mp3()

except Exception as e:
    print()
    print("ERROR: ", e)

finally:
    driver.quit()

    

    
