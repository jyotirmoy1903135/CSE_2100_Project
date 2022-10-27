# #(Paste in main for playing video)
#
# #Intro Video
import cv2
import numpy as np
#ffpyplayer for playing audio
from ffpyplayer.player import MediaPlayer

video_path = r"D:\Academic Study\2-1\CSE 2100\Login_project\Videos\AI_Intro.mp4"

def PlayVideo(video_path):
    video=cv2.VideoCapture(video_path)
    player = MediaPlayer(video_path)
    while True:
        grabbed, frame = video.read()
        audio_frame, val = player.get_frame()
        frame = cv2.resize(frame, (1550, 800))
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord(" "):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame

    video.release()
    cv2.destroyAllWindows()

PlayVideo(video_path)


# import pyglet
# #ffpyplayer for playing audio
# from ffpyplayer.player import MediaPlayer
#
#
# vidPath = r"D:\Academic Study\2-1\CSE 2100\Login_project\Videos\AI_Intro.mp4"
# window = pyglet.window.Window()
# player = pyglet.media.Player()
# source = pyglet.media.StreamingSource()
# MediaLoad = pyglet.media.load(vidPath)
#
# player.queue(MediaLoad)
# player.play()
#
# @window.event
# def on_draw():
#     window.clear()
#     if player.source and player.source.video_format:
#         player.get_texture().blit(50, 50)
#
#
# pyglet.app.run()



