# coding=utf-8
# __author__ = 'Mio'
from pprint import pprint
import sys
import requests
from lxml import etree
import pyping

reload(sys)
sys.setdefaultencoding('utf-8')

cookie = {
    "Cookie": "__cfduid=daa430f3af762f3a4fddbb86fb2fe52791459232787; yundunReferer=http%3A//www.ss-link.com/; Hm_lvt_c010d8c64151fdb7de20b95b413127e3=1459232789; Hm_lpvt_c010d8c64151fdb7de20b95b413127e3=1459232868; webpy_session_id=b5307a794e13932b7927e183a4aed3f4e21075f4"}

url = "http://www.ss-link.com/my/hostings"

html = requests.get(url, cookies=cookie).content

selector = etree.HTML(html)
a = selector.xpath('//*[@id="main"]/script[6]/text()')[0]

# a = """
# jQuery( document ).ready(function() {
#         jQuery('#main').data('myarray', []);
#         jQuery('#main').data('n', []);
#             jQuery('#main').data('myarray').push("45.35.71.119");
#             n="美国洛杉矶PS线路, 节点45.35.71.119 , 当前负载423";
#             jQuery('#main').data('n').push(n);
#             jQuery('#main').data('myarray').push("45.35.75.57");
#             n="美国洛杉矶PS线路, 节点45.35.75.57 , 当前负载423";
#             jQuery('#main').data('n').push(n);
#             jQuery('#main').data('myarray').push("45.35.45.35");
#             n="美国达拉斯PD线路, 节点45.35.45.35 , 当前负载429";
#             jQuery('#main').data('n').push(n);
#             jQuery('#main').data('myarray').push("204.74.217.107");
#             n="美国硅谷T2线路, 节点204.74.217.107 , 当前负载454";
#             jQuery('#main').data('n').push(n);
#             jQuery('#main').data('myarray').push("204.74.212.195");
#             n="美国硅谷T2线路, 节点204.74.212.195 , 当前负载455";
#             jQuery('#main').data('n').push(n);
#             jQuery('#main').data('myarray').push("204.74.215.39");
#             n="美国硅谷T2线路, 节点204.74.215.39 , 当前负载455";
#             jQuery('#main').data('n').push(n);
#             jQuery('#main').data('myarray').push("204.74.216.105");
#             n="美国硅谷T2线路, 节点204.74.216.105 , 当前负载455";
#             jQuery('#main').data('n').push(n);
#             jQuery('#main').data('myarray').push("72.46.135.119");
#             n="美国拉斯维加斯VW线路, 节点72.46.135.119 , 当前负载473";
#             jQuery('#main').data('n').push(n);
#             jQuery('#main').data('myarray').push("173.252.220.201");
#             n="美国硅谷T2线路, 节点173.252.220.201 , 当前负载553";
#             jQuery('#main').data('n').push(n);
#             jQuery('#main').data('myarray').push("104.250.144.10");
#             n="美国洛杉矶GR线路, 节点104.250.144.10 , 当前负载553";
#             jQuery('#main').data('n').push(n);
#             jQuery('#main').data('myarray').push("76.164.224.102");
#             n="美国拉斯维加斯VW线路, 节点76.164.224.102 , 当前负载363";
#             jQuery('#main').data('n').push(n);
#             jQuery('#main').data('myarray').push("104.250.143.243");
#             n="美国洛杉矶GR线路, 节点104.250.143.243 , 当前负载365";
#             jQuery('#main').data('n').push(n);
#             jQuery('#main').data('myarray').push("104.250.146.212");
#             n="美国洛杉矶GR线路, 节点104.250.146.212 , 当前负载365";
#             jQuery('#main').data('n').push(n);
#             jQuery('#main').data('myarray').push("104.250.146.37");
#             n="美国洛杉矶GR线路, 节点104.250.146.37 , 当前负载366";
#             jQuery('#main').data('n').push(n);
#             jQuery('#main').data('myarray').push("104.250.147.22");
#             n="美国洛杉矶GR线路, 节点104.250.147.22 , 当前负载367";
#             jQuery('#main').data('n').push(n);
#             jQuery('#main').data('myarray').push("46.249.56.39");
#             n="欧洲荷兰线路, 节点46.249.56.39 , 当前负载397";
#             jQuery('#main').data('n').push(n);
# });
# """
b = a.split("push(")

host_dict = {}
for i in b:
    index_n = i.find('n="')
    index_end = i.find('";')
    if index_n > -1 and index_end > -1:
        host_info = i[index_n + 3:index_end]
        host_info_list = host_info.split(',')
        host_addr = host_info_list[1].split("节点")[1].strip()
        host_load = int(host_info_list[2].strip().split("当前负载")[1])
        host_name = host_info_list[0]
        host_dict[host_addr] = {"load": host_load, "name": host_name}

pprint(host_dict)
print "\n\n"
print ">>>>>>>>>> start ping <<<<<<<<<<<<<"
print "\n"

for ip in host_dict:
    print '---- ping {} ------'.format(ip)
    r = pyping.ping(ip)
    host_dict[ip]['avg_rtt'] = r.avg_rtt
    print '      {}'.format(r.avg_rtt)

sorted_host = sorted(host_dict.items(), key=lambda t: t[1]['avg_rtt'])
rst = {sorted_host[0][0]: sorted_host[0][1]}
print "\n\n\n"
print "========= fast ip ========="
print "ip: {}".format(sorted_host[0][0])
print "name: {}".format(sorted_host[0][1]['name'])
print "load: {}".format(sorted_host[0][1]['load'])
print "avg_rtt: {}".format(sorted_host[0][1]['avg_rtt'])
