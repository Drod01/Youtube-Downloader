from pytube import YouTube
import os
import tqdm

url = input("Enter YouTube video URL: ")
yt = YouTube(url)

# Get video title 
print("Downloading video: ", yt.title)

# Get video streams
videos = yt.streams.filter(progressive=True).order_by('resolution')

# Select highest resolution stream
video = videos.last()

# Show download progress
print("Downloading...", end='') 
output = video.download(output_path='.', filename=yt.title)

with tqdm.tqdm(total=video.filesize) as pbar:
    for chunk in output:
        pbar.update(len(chunk))
print()

# Get audio streams
audios = yt.streams.filter(only_audio=True).order_by('bitrate')

# Select highest bitrate audio
audio = audios.last() 

# Download audio
print("Downloading audio...")
output = audio.download(output_path='.', filename=yt.title+'.mp3') 

for chunk in output:
    pbar.update(len(chunk))

print('\nDownload completed!')