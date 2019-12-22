from bs4 import BeautifulSoup
import bs4
import requests
import json
from xpinyin import Pinyin
import time

'''爬取最好大学网的所有学科排名代码重构'''
class Uni_Rank_All_Scrapy:

    def __init__(self,name_url):
        self.name_url = name_url
        self.subject_name = []
        self.data = []

    def get_subject_id(self):
        try:
            r = requests.get ( self.name_url )
            r.encoding = r.apparent_encoding
            r.raise_for_status ()
            html = r.text

        except:
            return '专业信息获取失败'

        soup = BeautifulSoup(html,'lxml')
        for div in soup.find_all(attrs={'class' : 'subject-ranking-content'}):
            for a in div.children :
                if isinstance(a,bs4.element.Tag):
                    P = Pinyin()
                    self.subject_name.append(P.get_pinyin(a.string,u''))

    def  get_html_data(self,rank_url):
        i = 0
        try:
            r = requests.get ( rank_url )
            r.raise_for_status ()
            r.encoding = r.apparent_encoding
            html = r.text

        except:

            return False
        soup = BeautifulSoup(html,'lxml')
        for tr in soup.find('tbody'):
            if isinstance(tr,bs4.element.Tag):
                    for td in tr.children :
                        i += 1
                        if td.string == None:
                            self.data.append('')
                        else:
                            self.data.append(td.string)











if __name__ == '__main__':
    name_url = 'http://www.zuihaodaxue.com/best_chinese_subjects_rankings.html'
    A = Uni_Rank_All_Scrapy(name_url)
    A.get_subject_id()
    for i in range(94):
        if i != 90 :
            rank_url = 'http://www.zuihaodaxue.com/BCSR/'+ A.subject_name[i]+'2019.html'
        else:
            rank_url = 'http://www.zuihaodaxue.com/BCSR/yinyueyuwudaoxue2019.html'
        A.get_html_data(rank_url)
        time.sleep(0.1)
        print ( '完成第%d次' % (i + 1) )
    with open ( 'uni_rank_all.text', 'a', encoding='utf-8' ) as f:
        f.write ( json.dumps ( A.data, ensure_ascii=False ) + '\n' )






