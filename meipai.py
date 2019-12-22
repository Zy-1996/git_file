import requests
import bs4
from bs4 import BeautifulSoup
import time
import re
import json
import random


def get_html(url):
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'Referer':'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
            'Cookie':'tt_webid=6766547418156205576; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6766547418156205576; __tasessionId=q0o7kkhh41575459605022; csrftoken=fc3a2483fb7f06747f68cb493a1de237; s_v_web_id=1fc961500d7f8d88a4c5ed1c629a1ceb',
            'x-requested-with':'XMLHttpRequest'
        }
    try:
        S = requests.Session()
        r = S.get(url,headers = headers)
        r.raise_for_status()
        if r.status_code ==200:
            return r.json()
    except:
        return None

def get_data(html,url_list,image_name):



    data = html.get('data')

    for str in data :
        if str.get('title'):

            url_list.append(str.get('image_list'))
            image_name.append(str.get('title'))

def get_image(url_list,image_name):

    urls = []
    for url_liss in url_list :

        for url_lis in url_liss:

            for key,value in url_lis.items():

                urls.append(value)

    for url,i in zip(urls,range(len(urls))):
        delay = random.randint(0,3)
        name = str(i+50)+'.jpg'
        with open(name,'wb') as f :
            r = requests.get((url))
            time.sleep(delay)
            f.write(r.content)
        i += 1
        print('完成图片'+str(i))















if __name__ == '__main__':
    url = 'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=20&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1575460396138'
    url_list = []
    image_name = []
    html = get_html(url)
    if html :
        get_data(html,url_list,image_name)
        get_image(url_list,image_name)
    else:
        print('获取错误')




