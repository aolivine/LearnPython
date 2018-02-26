__author__ = 'aolivine'
import json
import random
import time
import os
# import pymongo
import requests
from urllib import request
from bs4 import BeautifulSoup
from lxml import etree
from tkinter import Tk,Button,Entry,Label,Text,END,Variable
import cx_Freeze


class FileHelper(object):
    def __init__(self):
        pass
    def write(self,content):
        filepath="download/log.txt"
        p, f = os.path.split(filepath)
        if os.path.exists(p) == False:
            os.makedirs(p)
        # if os.path.exists(filepath) == False:
        #     os.makedirs(p)
        file = open(filepath, "a", encoding="utf-8")
        file.write(content)
        file.write('\n')
        file.close()

class ximalaya(object):

    def __init__(self):
        self.file = FileHelper()
        self.UA_LIST = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]
        self.headers1 = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
            'Cache-Control': 'max-age=0',
            'Proxy-Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': random.choice(self.UA_LIST)
        }
        self.headers2 = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
            'Cache-Control': 'max-age=0',
            'Proxy-Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': random.choice(self.UA_LIST)
        }



    #获取专辑列表 http://www.ximalaya.com/67241256/album/10352095/
    def get_url(self,urlraw):
        start_urls = [urlraw]
        for url in start_urls:
            # print(url)
            self.another(url)
            time.sleep(1)
        # file.write("取专辑列表")
        # file.write(start_urls)

    #声音列表
    def another(self,url):
        # print(url)
        html = requests.get(url, headers=self.headers2).text
        # print(html)
        self.file.write('\n')
        self.file.write("声音列表")
        self.file.write(url)
        self.get_sound(url)


        ifanother = etree.HTML(html).xpath('//div[@class="pagingBar_wrapper"]/a[last()-1]/@data-page')
        if len(ifanother):
            num = ifanother[0]
            print('本频道资源存在' + num + '个页面')
            for n in range(1, int(num)):
                print('开始解析{}个中的第{}个页面'.format(num, n))
                url2 = url + '?page={}'.format(n)
                self.get_sound(url2)

    #声音
    # def get_m4a(self,url):
    #     time.sleep(1)
    #     html = requests.get(url, headers=self.headers2).text
    #     numlist = etree.HTML(html).xpath('//div[@class="personal_body"]/@sound_ids')[0].split(',')
    #     for i in numlist:
    #         murl = 'http://www.ximalaya.com/tracks/{}.json'.format(i)
    #         html = requests.get(murl, headers=self.headers1).text
    #         dic = json.loads(html)
            # col2.insert(dic)
            # print(murl + '中的数据已被成功插入mongodb')

    def get_sound(self,url):
        time.sleep(1)
        html = requests.get(url, headers=self.headers1).text

        soup = BeautifulSoup(html, 'lxml')
        div_list = soup.find_all('div', attrs={'class': 'miniPlayer3'})

        for div_content in div_list:
            # print(div_content)
            # print("=================")

            item_list = div_content.find_all('a', attrs={'class': 'title'})
            for i, item in enumerate(item_list):
                sound_id=item['href'].split('/')[3]
                murl='http://www.ximalaya.com/tracks/{}.json'.format(sound_id)
                html = requests.get(murl, headers=self.headers1).text
                dic = json.loads(html)
                # self.file.write("声音")
                self.file.write(str(dic))
                self.download(dic)
                self.file.write("完成")

    def download(self,dic):
        url = dic['play_path_64']
        r = requests.get(url, stream=True)
        spath="download/"+dic['album_title']+"_"+dic['nickname']+"/"+dic['title']+".m4a"
        p, f = os.path.split(spath)
        if os.path.exists(p) == False:
            os.makedirs(p)
        # print(spath)
        # print(p)

        f = open((spath), "wb")
        for chunk in r.iter_content(chunk_size=512):
            if chunk:
                f.write(chunk)

class Application(object):

    def __init__(self):
        self.xmly = ximalaya()
        self.window = Tk()
        self.window.title("下载")
        self.window.geometry("670x600+700+300")
        # width x height + left + top
        var = Variable()
        var.set("http://www.ximalaya.com/67241256/album/10352095/")  # 设置文本框中的值
        self.entry = Entry(self.window, textvariable=var)
        self.entry.place(x=10, y=10, width=600, height=25)
        # self.entry.pack()

        self.submit_btn = Button(self.window, text="下载", command=self.submit)
        self.submit_btn.place(x=610, y=10, width=50, height=25)

        self.title_label = Label(self.window, text="结果：")
        self.title_label.place(x=10, y=55)

        self.result_text = Text(self.window, background="#ccc")
        self.result_text.place(x=10, y=75, width=650, height=500)






    def submit(self):
        content = self.entry.get()
        self.result_text.delete(1.0,END)
        self.result_text.insert(END,"开始下载，请稍候")
        self.result_text.insert(END, '\n')
        if len(content):
            self.result_text.insert(END, content)
            self.result_text.insert(END, '\n')
            self.xmly.get_url(content)
        # self.result_text.insert("\n"+os.path.dirname(os.path.realpath(__file__)))
        self.result_text.insert(END,"完成")

    def run(self):
        self.window.mainloop()
        # print("ok")

if __name__ ==  '__main__':
    app = Application()
    app.run()


