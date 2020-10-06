from bs4 import BeautifulSoup
import requests

def com_crawler(page):
    # print("여기서 안오나??@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    info_s = []
    # print("{}번째 페이지".format(page))
    req = requests.get('https://www.thinkcontest.com/Contest/CateField.html?c='+str(page))
    html = req.text

    soup = BeautifulSoup(html, 'html.parser')
    print(soup)
    for div in soup.select('ul.contest-banner-list'):
        for index, each in enumerate(div.select('a')):
            info = {}
            href = each.get('href')
            if href == '/AdsGuide': continue
            url = 'https://www.thinkcontest.com/m' + href
            info['url'] = url
            info_s.append(info)
        for index, each in enumerate(div.select('h4')):
            title = each.text
            info_s[index]['title'] = title
        for index, each in enumerate(div.select('p.time-limit')):
            date = each.text
            info_s[index]['date'] = date
        for index, each in enumerate(div.select('p.organizer')):
            organizer = each.text
            info_s[index]['organizer'] = organizer
        for index, each in enumerate(div.select('img')):
            img = each.get('src')
            if img == '/assets/img/main_card_banner_blank.png': continue
            img_url = 'https://www.thinkcontest.com' + img
            info_s[index]['img_url'] = img_url
    # print(info_s)
    return info_s
com_crawler(1)
