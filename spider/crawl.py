# -*- utf-8 -*-
from requests_html import HTMLSession
import json
import os
import time


class Crawl:
    def __init__(self):
        self.session = HTMLSession()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        }
        # 阅读器url
        self.read = 'https://read.qidian.com/chapter/'
        # 章节json
        self.chapter = 'https://book.qidian.com/ajax/book/category?\
_csrfToken=eHrOc0c7EL0iwX1IEIGDTgGlWflB4xrxIZKZf7Fv\
&bookId='
        pass

    def __str__(self):
        return "Crawl spider for QiDian"

    # noinspection PyShadowingNames
    def get_page(self, url):
        return self.session.get(url, headers=self.headers)

    @staticmethod
    def get_chapter_title(read):
        return read.html.find('.j_chapterName')[0].text

    @staticmethod
    def get_content(read):
        return read.html.find('.read-content')[0].text

    # noinspection PyShadowingNames
    def get_book_urls(self, url):
        r = self.session.get(url, headers=self.headers)
        # noinspection PyUnresolvedReferences
        ul = r.html.find('.all-img-list', first=True)
        lis = ul.find('li')
        # noinspection PyShadowingNames
        urls = []
        for li in lis:
            base_url = li.find('a', first=True).attrs['href']
            base_url = 'https:' + base_url
            urls.append(base_url)
        return urls

    @staticmethod
    def get_book_title(html):
        div = html.html.find('.book-info', first=True)
        em = div.find('em', first=True)
        return em.text

    # noinspection PyShadowingNames
    @staticmethod
    def get_book_url_num(url):  # no used at present
        return url[29:]

    # noinspection PyShadowingNames
    def get_book_category_urls(self, url):
        url_num = url[29:]
        chapter_url = self.chapter + url_num
        return chapter_url

    def get_read_url(self, base_url):
        return self.read + base_url


test = Crawl()
cat_crawl = Crawl()
# noinspection PyListCreation
urls = []

urls.append('https://read.qidian.com/chapter/_AaqI-dPJJ4uTkiRw_sFYA2/eSlFKP1Chzg1')
urls.append('https://book.qidian.com/info/1004608738')
urls.append('https://book.qidian.com/ajax/book/category?\
_csrfToken=eHrOc0c7EL0iwX1IEIGDTgGlWflB4xrxIZKZf7Fv&bookId=1004608738')
urls.append('https://www.qidian.com/all?\
orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=1')
urls.append('https://www.qidian.com/all?\
chanId=21&orderId=&page=1&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0')

print(test)
# print(test.get_page(urls[2]).text)
# print(urls[2])
book_urls = test.get_book_urls(urls[3])  # 获取整个页面书籍url后无法通过test对象获取章节json
for book_url in book_urls:
    # noinspection PyTypeChecker
    book_name = test.get_book_title(test.get_page(book_url))

    # print(book_name) 创建小说文件夹
    if not os.path.exists('novels/'+book_name):
        os.makedirs('novels/'+book_name)

    # 获取章节
    pre_url = 'CrawlSpider'
    category_url = test.get_book_category_urls(book_url)
    chapter_json = json.loads(cat_crawl.get_page(category_url).text)
    vs = chapter_json['data']['vs']
    for v in vs:  # category包中0 1 参考圣墟
        cs = v['cs']
        for c in cs:  # 0中的0-99 99-100
            # print(c['cU'])
            if pre_url == c['cU']:
                break
            else:
                pre_url = c['cU']
                read_url = test.get_read_url(c['cU'])
                chapter_html = test.get_page(read_url)
                # noinspection PyTypeChecker
                chapter_name = test.get_chapter_title(chapter_html)
                # noinspection PyTypeChecker
                chapter_content = test.get_content(chapter_html)
                print(chapter_name)
                chapter_path = 'novels/' + book_name + '/' + chapter_name + '.txt'
                if not os.path.exists(chapter_path):
                    f = open(chapter_path, 'w')
                    f.write(chapter_content)
                    f.close()
                    print('[*] Crawl successful! ', chapter_name)
            # 防止IP被封
            time.sleep(1)
    break
# acquire book chapter
# print(json.loads(test.get_page(urls[2]).text)['data']['firstChapterJumpurl'])
# chapter_json = json.loads(test.get_page(urls[2]).text)
# firstChapterJumpurl = chapter_json['data']['firstChapterJumpurl']
# vs = chapter_json['data']['vs']
# i = 1
# for v in vs:
#    cs = v['cs']
#    for c in cs:
#        print('[*]', i, c['cU'])
#        i = i + 1

# book_urls = test.get_book_urls(urls[3])
# for url in book_urls:
#    print(url, test.get_book_url_num(url))
# acquire book name
# for book_url in book_urls:
#    res = test.get_page(book_url)
#    # noinspection PyTypeChecker
#    print(test.get_book_title(res))

# noinspection PyTypeChecker
# print(res.html.find('.all-img-list', first=True).find('li')[0].find('a', first=True).attrs['href'])

# noinspection PyTypeChecker
# print(test.get_title(res))
# noinspection PyTypeChecker
# print(test.get_content(res))

# print(test.get_page(url).html.find('.read-content')[0].text)
# 获取章节内容
# print(test.get_page(url).html.find('.j_chapterName')[0].text)
# 获取章节标题
