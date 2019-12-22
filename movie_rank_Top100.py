import re
import requests
import time
import json

'''爬取猫眼Top100榜单'''


def get_html(url, headers):
    # 爬取网页源码
    try:
        r = requests.get ( url, headers=headers )
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print ( '发生错误' )


def get_data(html, data_dit):
    '''处理网页源码，为获取有用的信息'''
    # 正则表达式
    pattern1 = re.compile (
        '<p class="name".*?}">(.*?)</a></p>.*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>.*?<i class="integer">(.*?)</i><i class="fraction">(.)</i>',
        re.S )
    # 返回的是列表，里面有对应括号个元组
    result1 = re.findall ( pattern1, html )
    for item in result1:
        data_dit['电影名称'].append ( item[0] )
        data_dit['主演'].append ( item[1].strip () )
        data_dit['上映时间'].append ( item[2] )
        data_dit['评分'].append ( item[3] + item[4] )


def display_list(data_dit):
    # 控制台遍历爬取的信息
    for i in range ( 10 ):
        print ( data_dit['电影名称'][i] )
        print ( data_dit['主演'][i] )
        print ( data_dit['上映时间'][i] )
        print ( data_dit['评分'][i] + '\n' )


def write_file(data_dit):
    # 以json格式写入文件
    with open ( 'movie_rank.txt', 'a', encoding='utf-8' ) as f:
        f.write ( json.dumps ( data_dit, ensure_ascii=False ) + '\n' )


def main(i):
    # 拼接url，为爬取每个页面
    url = 'https://maoyan.com/board/4?offset=' + str ( i )
    # 请求头信息中的cookie是在浏览器中打开该网页验证后的，如果会话超时，通过浏览器再访问网页验证一次
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0',
        'Connection': 'keep-alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Cache-Control': 'max-age=0',
        'Accept-Encoding': 'gzip, deflate, br',
        'Cookie': '__mta=87339431.1573875038519.1573881700231.1573889887794.8; uuid_n_v=v1; uuid=7655AA10082111EAAF06F56460C86D72812485D271D84F1F9432D5BD53093FBA; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1573875038,1573875106,1573889888; _lxsdk_cuid=16e724338fa62-0d6f6730d96345-4c302b7a-144000-16e724338fbc8; _lxsdk=7655AA10082111EAAF06F56460C86D72812485D271D84F1F9432D5BD53093FBA; _csrf=b488ec687469e96b2669c24a3dcb3dfe1b9eca4aa23a77c4a7100061cb107342; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1573889888; _lxsdk_s=16e7325cdf5-49f-1-7d3%7C%7C2'
    }

    data_dit = {
        '电影名称': [],
        '主演': [],
        '上映时间': [],
        '评分': []
    }

    html = get_html ( url, headers )
    get_data ( html, data_dit )
    display_list ( data_dit )
    write_file ( data_dit )


if __name__ == '__main__':
    for i in range ( 10 ):
        main ( i * 10 )
        # 延时1s
        time.sleep ( 1 )
