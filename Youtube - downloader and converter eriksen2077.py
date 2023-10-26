from pytube import YouTube
from moviepy.editor import * 

def Download(link):
    youtube_Obejct = YouTube(link)
    youtube_Obejct = youtube_Obejct.streams.get_highest_resolution()
    try:
        youtube_Obejct.download()
        print("alright alright alright")
    except: 
        print("error")
   

link = input("Enter the YouTube URL: ")
Download(link) 
# You have to paste the same title as it was downloaded from youtube
vid  = input("Paste name of vid (add to the end '.mp4'): ")
music = input("Paste name of vid (add to the end '.mp3' ): ")
VideoClip = VideoFileClip(vid)
audioclip = VideoClip.audio
audioclip.write_audiofile(music)
audioclip.close()
VideoClip.close()








    