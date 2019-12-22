import requests
import json
import re
from xpinyin import Pinyin
import time

'''爬取最好大学网的所有学科排名'''

def get_subject_id(url,subject_name):
    try:
        r = requests.get(url)
        r.encoding = r.apparent_encoding
        r.raise_for_status()
        html = r.text
    except:
        return False
    pattern = re.compile(' <a class=subject.*?html">(.*?)</a>',re.S)
    result = re.findall(pattern,html)
    P = Pinyin()
    for name in result:
        subject_name.append(P.get_pinyin(name,u''))
    return result

def get_rank_html(url):

    try:
        r = requests.get ( url )
        r.raise_for_status ()
        r.encoding = r.apparent_encoding
        return r.text

    except:

        return False

def get_html_data(html):
    pattern = re.compile('<td class="ranking">(.*?)</td><td class="ranking">(.*?)</td><td class="align-center" >(.*?)</td><td class="align-left" >(.*?)</td>',re.S)
    data  = re.findall(pattern,html)
    return data


if __name__ == '__main__':
    url_name = 'http://www.zuihaodaxue.com/best_chinese_subjects_rankings.html'
    subject_name = []
    name = get_subject_id( url_name, subject_name )


    for i in range(94):
        if i != 90 :
            url = 'http://www.zuihaodaxue.com/BCSR/'+ subject_name[i]+'2019.html'
        else:
            url = 'http://www.zuihaodaxue.com/BCSR/yinyueyuwudaoxue2019.html'

        html = get_rank_html ( url )
        data = get_html_data ( html )
        with open('uni_rank_all.text','a',encoding='utf-8') as f :
            f.write(name[i]+' : '+json.dumps(data,ensure_ascii=False)+'\n')
        print('完成第%d次' % (i+1))








