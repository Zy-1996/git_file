import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from multiprocessing import  Process


class GrabVotes ():

    def __init__(self, date, User_agent, url, name, id, proxy):
        self.date = date
        self.User_agent = 'User-Agent='+User_agent
        self.url = url
        self.name = name
        self.id = id
        self.proxy = proxy
        self.browser = self.browser_start ()

    def browser_start(self):
        options = webdriver.ChromeOptions ()
        options.add_argument ( self.User_agent )
        if self.proxy != '':
            options.add_argument ( '--proxy-server=http://%s' % self.proxy )
        browser = webdriver.Chrome ( options=options )
        browser.get ( self.url )

        return browser

    def grab_votes(self):

        while True:
            locate_time = time.strftime ( '%Y-%m-%d %H:%M:%S', time.localtime () )

            if locate_time >= self.date:

                try:
                    tag1 = self.browser.find_elements_by_class_name('fbi_input')[0]
                    tag2 = self.browser.find_elements_by_class_name ( 'fbi_input' )[1]
                    button = self.browser.find_element_by_id ( 'form_submit' )
                    a = True
                except NoSuchElementException:
                    a = False
                    print ( '时间设置错误' )
                    self.browser.close ()

                if a:

                    tag1.clear ()
                    tag2.clear ()
                    tag1.send_keys ( self.name )
                    tag2.send_keys ( self.id )
                    button.click ()
                    print ( 'ok' )
                    time.sleep ( 5 )
                    self.browser.close ()

                break

def main():

    url = 'http://ndgiam1lsekpes40.mikecrm.com/EjwsjIi'
    User_agent = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0Chrome/33.0.0.0 Mobile Safari/537.36 MicroMessenger/6.0.0.54_r849063.501 NetType/WIFI '
    date = '2019-12-19 23:00:04'
    name = '黄凯'
    id = '2111904371'
    proxy = ''
    A = GrabVotes ( date, User_agent, url, name, id, proxy )
    A.grab_votes ()

if __name__ == '__main__':
    main()




"""过程"""
# options = webdriver.ChromeOptions()
# options.add_argument('User-Agent= mozilla/5.0 (linux; u; android 4.1.2; zh-cn; mi-one plus build/jzo54k) applewebkit/534.30 (khtml, like gecko) version/4.0 mobile safari/534.30 micromessenger/5.0.1.352  ')
# browser = webdriver.Chrome(options = options)
# browser.get('http://ndgiam1lsekpes40.mikecrm.com/EjwsjIi')
#
#
# while True :
#     locate_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
#
#     if locate_time == '2019-12-17 12:33:00':
#         tag1 = browser.find_element_by_xpath ( '//div[@class="fbc_content fbc_widthCp"]/div/input' )
#         tag2 = browser.find_element_by_xpath ( '//div[@class="fbc_imItem"]/div/input' )
#         button = browser.find_element_by_id ( 'form_submit' )
#         tag1.send_keys ( '李为撒' )
#         tag2.send_keys ( '12321' )
#         button.click ()
#         print ( 'ok' )
#         break
#
# browser.close ()