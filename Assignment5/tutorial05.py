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


rename_Game_of_Thrones(2, 3)


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


def rename_Suits(paddingseason, paddingepisode):
    # Suits rename Logic
    path = r'./Subtitles/Suits'
    seasonno = ''
    episodeno = ''
    episodename = ''
    for filename in os.listdir(path):
        lis = filename.split(' - ')
        seasonno = lis[1][0:lis[1].index('x')]
        episodeno = lis[1][lis[1].index('x')+1:]
        temp1 = lis[2].split('.480')
        temp2 = temp1[0].split('.720')
        temp3 = temp2[0].split('.1080')
        temp4 = temp3[0].split('.HDTV')
        episodename = temp4[0].split('.en')[0]
        while len(seasonno) < paddingseason:
            seasonno = '0'+seasonno
        if len(seasonno) > paddingseason:
            seasonno = seasonno[-1*paddingseason:]
        while len(episodeno) < paddingepisode:
            episodeno = '0'+episodeno
        if len(episodeno) > paddingepisode:
            episodeno = episodeno[-1*paddingepisode:]
        if filename.endswith(".mp4"):
            if not os.path.isfile(path+'/'+lis[0]+' - Season '+seasonno+' Episode '+episodeno+' - '+episodename+'.mp4'):
                os.rename(path+'/'+filename, path+'/' +
                          lis[0]+' - Season '+seasonno+' Episode '+episodeno+' - '+episodename+'.mp4')
            else:
                os.remove(path+'/'+filename)
        if filename.endswith('.srt'):
            if not os.path.isfile(path+'/'+lis[0]+' - Season '+seasonno+' Episode '+episodeno+' - '+episodename+'.srt'):
                os.rename(path+'/'+filename, path+'/' +
                          lis[0]+' - Season '+seasonno+' Episode '+episodeno+' - '+episodename+'.srt')
            else:
                os.remove(path+'/'+filename)
    pass


rename_Suits(2, 5)


def rename_How_I_Met_Your_Mother(paddingseason, paddingepisode):
    # How I met your mother rename Logic
    path = r'./Subtitles/How I Met Your Mother'
    seasonno = ''
    episodeno = ''
    episodename = ''
    for filename in os.listdir(path):
        lis = filename.split(' - ')
        seasonno = lis[1][0:lis[1].index('x')]
        episodeno = lis[1][lis[1].index('x')+1:]
        temp1 = lis[2].split('.480')
        temp2 = temp1[0].split('.720')
        temp3 = temp2[0].split('.1080')
        temp4 = temp3[0].split('.HDTV')
        temp5 = temp4[0].split('.fov')
        temp6 = temp5[0].split('.FoV')
        episodename = temp6[0].split('.en')[0]
        temp = episodeno.split('-')
        flag = 0
        if len(temp) == 2:
            flag = 1
            while len(temp[0]) < paddingepisode:
                temp[0] = '0'+temp[0]
            if len(temp[0]) > paddingepisode:
                temp[0] = temp[0][-1*paddingepisode:]
            while len(temp[1]) < paddingepisode:
                temp[1] = '0'+temp[1]
            if len(temp[1]) > paddingepisode:
                temp[1] = temp[1][-1*paddingepisode:]
            episodeno = temp[0]+'-'+temp[1]
        while len(seasonno) < paddingseason:
            seasonno = '0'+seasonno
        if len(seasonno) > paddingseason:
            seasonno = seasonno[-1*paddingseason:]
        if flag == 0:
            while len(episodeno) < paddingepisode:
                episodeno = '0'+episodeno
            if len(episodeno) > paddingepisode:
                episodeno = episodeno[-1*paddingepisode:]
        if filename.endswith(".mp4"):
            if not os.path.isfile(path+'/'+lis[0]+' - Season '+seasonno+' Episode '+episodeno+' - '+episodename+'.mp4'):
                os.rename(path+'/'+filename, path+'/' +
                          lis[0]+' - Season '+seasonno+' Episode '+episodeno+' - '+episodename+'.mp4')
            else:
                os.remove(path+'/'+filename)
        if filename.endswith('.srt'):
            if not os.path.isfile(path+'/'+lis[0]+' - Season '+seasonno+' Episode '+episodeno+' - '+episodename+'.srt'):
                os.rename(path+'/'+filename, path+'/' +
                          lis[0]+' - Season '+seasonno+' Episode '+episodeno+' - '+episodename+'.srt')
            else:
                os.remove(path+'/'+filename)
    pass


rename_How_I_Met_Your_Mother(2, 6)
