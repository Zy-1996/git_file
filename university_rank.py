import requests
from bs4 import BeautifulSoup
import bs4
from xpinyin import Pinyin


def get_data(url):
    # 爬取数据
    try:
        r = requests.get ( url )
        r.raise_for_status ()
        r.encoding = r.apparent_encoding
        return r.text

    except:

        return None


def sort_data(univ_list, html):
    # 处理数据
    soup = BeautifulSoup ( html, 'html.parser' )
    name = soup ( 'title' )
    print ( name[0].string )
    for tr in soup.find ( 'tbody' ).children:
        if isinstance ( tr, bs4.element.Tag ):
            tds = tr ( 'td' )
            if tds[0].string == None:
                continue
            univ_list[0].append ( tds[0].string )
            univ_list[1].append ( tds[1].string )
            univ_list[2].append ( tds[2].string )
            univ_list[3].append ( tds[3].string )


def print_data(univ_list, num):
    # 按格式打印数据
    len_data = len ( univ_list[0] )
    print ( '{:^10}\t{:^6}\t{:^10}\t{:^10}'.format ( '2019排名', '2018排名', '百分位段', '院校名称' ) )
    if len_data > num:
        for i in range ( num ):
            print ( '{:^10}\t\t{:^6}\t\t{:^10}\t\t{:^10}'.format ( univ_list[0][i], univ_list[1][i], univ_list[2][i],
                                                                   univ_list[3][i] ) )
    else:
        for i in range ( len_data ):
            print ( '{:^10}\t\t{:^6}\t\t{:^10}\t\t{:^10}'.format ( univ_list[0][i], univ_list[1][i], univ_list[2][i],
                                                                   univ_list[3][i] ) )


def main():
    univ_list = [[], [], [], []]
    url1 = 'http://www.zuihaodaxue.com/BCSR/'
    url2 = '2019.html'
    tip = input ( '请输入专业' )
    P = Pinyin ()
    url = P.get_pinyin ( tip, u'' )
    html = get_data ( url1 + url + url2 )
    if html == None:
        print ( '并没有这个专业' )
        return
    num = int ( input ( '请输入要查询前多少名' ) )
    sort_data ( univ_list, html )
    print_data ( univ_list, num )


main ()
