import requests
import json
from bs4 import BeautifulSoup
import bs4

url = 'https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100505&is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page=1&pagebar=0&pl_name=Pl_Official_MyProfileFeed__20&id=1005055671157420&script_uri=/p/1005055671157420/home&feed_type=0&pre_page=1&domain_op=100505&__rnd=1575367757269'
url1 = 'https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100505&is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page=1&pagebar=1&pl_name=Pl_Official_MyProfileFeed__20&id=1005055671157420&script_uri=/p/1005055671157420/home&feed_type=0&pre_page=1&domain_op=100505&__rnd=1575367762153'
url2 = 'https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100505&is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page=2&pagebar=0&pl_name=Pl_Official_MyProfileFeed__20&id=1005055671157420&script_uri=/p/1005055671157420/home&feed_type=0&pre_page=2&domain_op=100505&__rnd=1575367771954'
url4 = 'https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100505&is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page=2&pagebar=1&pl_name=Pl_Official_MyProfileFeed__20&id=1005055671157420&script_uri=/p/1005055671157420/home&feed_type=0&pre_page=2&domain_op=100505&__rnd=1575367776634'
url5 = 'https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100505&is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page=2&pagebar=0&pl_name=Pl_Official_MyProfileFeed__20&id=1005055671157420&script_uri=/p/1005055671157420/home&feed_type=0&pre_page=2&domain_op=100505&__rnd=1575368187531'
url6 = 'https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100505&is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page=2&pagebar=1&pl_name=Pl_Official_MyProfileFeed__20&id=1005055671157420&script_uri=/p/1005055671157420/home&feed_type=0&pre_page=2&domain_op=100505&__rnd=1575368194088'
url7 = 'https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100505&profile_ftype=1&is_ori=1&pagebar=0&pl_name=Pl_Official_MyProfileFeed__21&id=1005053201013460&script_uri=/u/3201013460&feed_type=0&page=1&pre_page=1&domain_op=100505&__rnd=1575371342198'

headers = {
    'Host':'weibo.com',
    'Referer':'https://weibo.com/u/3201013460?profile_ftype=1&is_ori=1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie':'Ugrow-G0=9ec894e3c5cc0435786b4ee8ec8a55cc; SUB=_2A25w4kdFDeRhGeNI7FMQ9SnIyTyIHXVTlj-NrDV8PUNbmtANLXXzkW9NSC_Z8TuoZ4ND_438cMwUQR8qzl7bCS3f; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWuEIsH4eMsp2503gUpFSux5JpX5KzhUgL.Fo-cS02pSKMXeo52dJLoI79Nwr.4TKBt; login_sid_t=d8227da1c47bc00729731b3af0ad39ae; cross_origin_proto=SSL; YF-V5-G0=27518b2dd3c605fe277ffc0b4f0575b3; _s_tentry=passport.weibo.com; Apache=7588232666326.957.1575368451438; SINAGLOBAL=7588232666326.957.1575368451438; ULV=1575368451442:1:1:1:7588232666326.957.1575368451438:; wb_view_log=1536*8641.25; SUHB=0k1CWKrOFfNEai; ALF=1606904469; SSOLoginState=1575368470; wvr=6; YF-Page-G0=761bd8cde5c9cef594414e10263abf81|1575371341|1575371271; wb_view_log_5671157420=1536*8641.25; webim_unReadCount=%7B%22time%22%3A1575371338360%2C%22dm_pub_total%22%3A3%2C%22chat_group_client%22%3A0%2C%22allcountNum%22%3A3%2C%22msgbox%22%3A0%7D'
}

r = requests.get(url7,headers = headers)
r.encoding = r.apparent_encoding
data = r.json()
soup = BeautifulSoup(data.get('data'),'lxml')
print(soup)
for text in  soup.find_all(attrs={'nick-name':'丈母娘似的爱情','class':"WB_text W_f14"}):
    if isinstance(text,bs4.element.Tag):
        if text.string:
            print(text.string)


