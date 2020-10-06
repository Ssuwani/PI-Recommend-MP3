import os
import subprocess
import pytube
def receive_url_and_name_download(url, name):
    url = pytube.YouTube(url)

    vids = url.streams.all()

    vids[0].download('./mp4')

    default_filename = vids[0].default_filename

    subprocess.call(['ffmpeg', '-i', os.path.join('./mp4', default_filename), os.path.join('./mp3', name+'.mp3')])

