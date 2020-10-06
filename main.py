from receive_title_return_url import receive_title_return_url as RTRU
from receive_url_and_name_download import receive_url_and_name_download as RUND
from receive_title_play_music import receive_title_play_music as RTPM
from existTest import existTest

import datetime
import capture, kakaoAPI
date = str(datetime.datetime.today())[:10]
capture.capture(date)
titles = kakaoAPI.recog(date)
# title = "안녕"
# 이미 있는지 없는지 확인


def downloadmusic(title):
    url = RTRU(title)

    print("mp3 파일 다운로드 시도")
    try:
        RUND(url, title)
        print("mp3파일 다운로드 성공")
    except:
        print("다운로드 실패")


def playmusic(title):
    try:
        RTPM(title)
        print("음악끝")
    except:
        print("재생실패")

for title in titles:
    print(title)
    try:
        if existTest(title):
            playmusic(title)
        else:
            downloadmusic(title)
            playmusic(title)
    except:
        print("실패.. 건너뛰기..")



