import os
import re
from pytube import YouTube

cwd = os.getcwd()
yt = YouTube('https://www.youtube.com/watch?v=2rxG8quzCtA')
stream = yt.streams.get_by_itag(139)

def title_scrubber(title):
    bad_characters = ['<', '>', ':', '"', "/" , "\\", '?', '*']
    bad_words = ["CON", "PRN", "AUX", "NUL", "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8",
        "COM9", "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"]
    
    for character in bad_characters:
        title = title.replace(character, '')

    for word in bad_words:
        title = re.sub(word, "", title)

    title = title.replace(' ', '_')

    return title

title = title_scrubber(yt.title)

stream.download(output_path=cwd, filename=title + ".wav")

