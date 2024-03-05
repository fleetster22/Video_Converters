from moviepy.editor import *

def convert_to_avi(mp4_file, avi_file):
    try:
        video = VideoFileClip(mp4_file)
        video.write_videofile(avi_file, codec='rawvideo', audio_codec='pcm_s16le')
        video.close()
        print("Conversion successful!")
    except Exception as e:
        print("Error:", e)

# Replace 'QueenBee.mp4' and 'QueenBee.avi' with your input and output file paths
convert_to_avi('QueenBee.mp4', 'QueenBee.avi')
