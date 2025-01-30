import os


# the script to compress the video from the dir ./input to ./videos
# before running the script, need to put FFMPEG exe file under the current directory
for name in os.listdir('./input'):
    if '.DS_Store' in name:
        continue
    else:
        os.system(f'./ffmpeg -y -i ./input/{name} -b:v 256k -bufsize 256k -an ./videos/{name}')