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


#rename_FIR(5, 5)


def rename_Game_of_Thrones(paddingseason, paddingepisode):
    # GOT rename Logic
    path = r'./Subtitles/Game of Thrones'
    seasonno = ''
    episodeno = ''
    episodename = ''
    for filename in os.listdir(path):
        lis = filename.split(' - ')
        seasonno = lis[1][0:lis[1].index('x')]
        episodeno = lis[1][lis[1].index('x')+1:]
        episodename = lis[2][0:lis[2].index('.')]
        while len(seasonno) < paddingseason:
            seasonno = '0'+seasonno
        if len(seasonno) > paddingseason:
            seasonno = seasonno[-1*paddingseason:]
        while len(episodeno) < paddingepisode:
            episodeno = '0'+episodeno
        if len(episodeno) > paddingepisode:
            episodeno = episodeno[-1*paddingepisode:]
        if filename.endswith(".mp4"):
            os.rename(path+'/'+filename, path+'/' +
                      lis[0]+' - Season '+seasonno+' Episode '+episodeno+' - '+episodename+'.mp4')
        if filename.endswith('.srt'):
            os.rename(path+'/'+filename, path+'/' +
                      lis[0]+' - Season '+seasonno+' Episode '+episodeno+' - '+episodename+'.srt')
    pass


#rename_Game_of_Thrones(2, 3)


def rename_Sherlock(paddingseason, paddingepisode):
    # sherlock rename Logic
    path = r'./Subtitles/Sherlock'
    seasonno = ''
    episodeno = ''
    for filename in os.listdir(path):
        temp = filename[filename.index('.')+1:]
        seasonno = temp[1]+temp[2]
        temp2 = temp[temp.index('E')+1:]
        episodeno = temp2[0]+temp2[1]
        while len(seasonno) < paddingseason:
            seasonno = '0'+seasonno
        if len(seasonno) > paddingseason:
            seasonno = seasonno[-1*paddingseason:]
        while len(episodeno) < paddingepisode:
            episodeno = '0'+episodeno
        if len(episodeno) > paddingepisode:
            episodeno = episodeno[-1*paddingepisode:]
        if filename.endswith(".mp4"):
            os.rename(path+'/'+filename, path+'/'+'Sherlock' +
                      ' - Season '+seasonno+' Episode '+episodeno+'.mp4')
        if filename.endswith('.srt'):
            os.rename(path+'/'+filename, path+'/'+'Sherlock' +
                      ' - Season '+seasonno+' Episode '+episodeno+'.srt')
    pass


rename_Sherlock(2, 4)
