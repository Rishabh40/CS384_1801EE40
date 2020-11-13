# Importing required Libraries
import os
import re


def rename_FIR(paddingseason, paddingepisode):
    # FIR rename Logic
    path = r'./Subtitles/FIR'
    episodeno = ''
    for filename in os.listdir(path):
        pattern = re.compile(r'\d+')
        list = re.findall(pattern, filename)
        episodeno = list[0]
        while len(episodeno) < paddingepisode:
            episodeno = '0'+episodeno
        if len(episodeno) > paddingepisode:
            episodeno = episodeno[-1*paddingepisode:]
        if filename.endswith(".mp4"):
            if not os.path.isfile(path+'/'+'FIR'+' - Episode '+episodeno+'.mp4'):
                os.rename(path+'/'+filename, path+'/'+'FIR' +
                          ' - Episode '+episodeno+'.mp4')
            else:
                os.remove(path+'/'+filename)
        if filename.endswith('.srt'):
            if not os.path.isfile(path+'/'+'FIR'+' - Episode '+episodeno+'.srt'):
                os.rename(path+'/'+filename, path+'/'+'FIR' +
                          ' - Episode '+episodeno+'.srt')
            else:
                os.remove(path+'/'+filename)
    pass


rename_FIR(5, 5)
