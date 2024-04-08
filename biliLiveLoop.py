#! /bin/python3 

import os
import subprocess
import time

video_path=input('输入视频完整路径:\n')
live_key=input('shift+insert复制串流秘钥:\n')
fps=input('设置推流帧率:(推荐30)\n')
live_title=input('直播画面文字说明:(没有就回车)\n')

filepathlist=[]
def getpathlist(dirpath):
    global filepathlist
    if not os.path.exists(dirpath):
        print ("file or directory isn't exist")
        return
    if os.path.isfile(dirpath):
        filepathlist.append(dirpath)
        return
    resultList = os.listdir(dirpath)
    for fileOrDir in resultList:
        getpathlist(dirpath + "/" +fileOrDir)   #recursion
    return filepathlist


def getfilename(filepath):
    splitter1 = filepath.rfind('/')
    splitter2 = filepath.rfind('.')
    filename = filepath[splitter1 + 1 : splitter2]
    return filename


filepathlist = getpathlist(video_path)
print(filepathlist)
with open(video_path+'/video_path_list.txt','w+',encoding='utf-8') as fs:
    for filepath in filepathlist:
        fs.write("file  '"+filepath+"'\n")

with open(video_path+'/live_log.txt','a+',encoding='utf-8') as fs:
    fs.write('live on:---') 
    fs.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    fs.write('---\n')
    for filepath in filepathlist:
        fs.write(getfilename(filepath))
        fs.write('\n')

video_path_tmp=video_path + '/video_path_list.txt'
res=subprocess.Popen('ffmpeg -re -stream_loop -1 -f concat -safe 0 -i ' + video_path_tmp + ' -c copy -vcodec libx264 -acodec copy -b:a 192k -r '+ fps+ ' -vf "drawtext=fontsize=24:fontfile=FreeSerif.ttf:text=\'' + live_title + '\':x=10:y=main_h-30:fontcolor=LightGrey:alpha=0.6" -f flv "rtmp://live-push.bilivideo.com/live-bvc/'+live_key+'"',stdout=subprocess.PIPE,shell=True)


        


