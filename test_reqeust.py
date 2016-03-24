# coding=utf-8
# __author__ = 'Mio'

import requests
from bs4 import BeautifulSoup
import re
from tornado.escape import utf8

download_dir = "/Users/mio/Downloads/renren_blog/"
url = "http://blog.renren.com/blog/408842825/938039669"
cookie = {"Cookie": "_nologin_sid=09a6d5d47520710bc5de03d226b9635d; anonymid=igf39ots-maq778; depovince=GW; jebecookies=54d9c181-b1e4-425e-ab7e-16f3aee7c833|||||; _r01_=1; ick_login=fd425e42-d073-414a-b994-ad6f15c03688; _de=2774CCC1F9BBBAED8D1ADEFA232AC95D; p=cfd0b265f40c8a12526a51c80d4552655; ap=408842825; first_login_flag=1; ln_uact=13087550279; ln_hurl=http://hdn.xnimg.cn/photos/hdn321/20140514/1105/h_main_HPt7_e0b70000d28b195a.jpg; t=7c9f8752ec3879ab429214f6e23a3a445; societyguester=7c9f8752ec3879ab429214f6e23a3a445; id=408842825; xnsid=585f3ed3; JSESSIONID=abc-lFEP85beQ9HimONov; ver=7.0; loginfrom=null; jebe_key=88508a2b-7612-4f33-bc07-eaad55512a57%7Cbc7b7d83bfbd3fb8b6b66c3b7b24902d%7C1458806319555%7C1%7C1458806319489; wp_fold=0"}

# html = requests.get(url, cookies=cookie).content
# fo = open("/Users/mio/Desktop/r_blog.html", "wb")
# fo.write(html)


soup = BeautifulSoup(open("/Users/mio/Desktop/r_blog.html"), "html.parser")
# print soup
pre_and_next = soup.find_all(class_="blogDetail-pre")
next_blog_url = pre_and_next[0].findAll('a', href=True)[0]['href']

# //*[@id="blogDetail_sideLeft"]/div[2]
