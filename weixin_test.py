import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from threading import Thread


class GrabVotes ():

    def __init__(self, date, User_agent, url, stu_name, stu_id, proxy):
        self.date = date
        self.User_agent = 'User-Agent='+User_agent
        self.url = url
        self.name = stu_name
        self.id = stu_id
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


class mul_spider(Thread):

    def __init__(self,grab_v):
        super().__init__()
        self.grab_v = grab_v

    def run(self) :
        self.grab_v.grab_votes()


def main():

    url = 'http://dihuwfjvktlugpin.mikecrm.com/eLALQn0'
    User_agent = ('Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0Chrome/33.0.0.0 Mobile Safari/537.36 MicroMessenger/6.0.0.54_r849063.501 NetType/WIFI ','mozilla/5.0 (iphone; cpu iphone os 5_1_1 like mac os x) applewebkit/534.46 (khtml, like gecko) mobile/9b206 micromessenger/5.0')
    date = '2019-12-24 20:33:00'
    name = ('黄凯','李新旺')
    id = ('2111904371','2111904123')
    proxy = ''

    spider_list = []

    for i in range(len(name)) :
        A = GrabVotes(date, User_agent[i], url, name[i], id[i], proxy)
        t = mul_spider(A)
        t.start()
        spider_list.append(t)





if __name__ == '__main__':
    main()




