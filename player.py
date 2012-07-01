import os
import subprocess

ROOT = '/media/usbstick'
CMD = 'mpg123 "%s"'


def get_list():
    for file in os.listdir(ROOT):
        if not file.endswith('.mp3'):	
            continue
        yield os.path.join(ROOT, file)



for file in get_list():
    subprocess.call(CMD % file, shell=True)

