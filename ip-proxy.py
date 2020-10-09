#coding:utf-8

from bs4 import BeautifulSoup
import requests
import xlwt
import time
import urllib
import socket
import threading

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
'''def getHTMLText(url,proxies):
    try:
        r = requests.get(url,proxies=proxies)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
    except:
        return 0
    else:
        return r.text
        '''
def get_ip_list(url):
    i=1
    for i in range(1,20):
        url_num = url + str(i)+'/'
        #print(url_num)
        web_data = requests.get(url_num,headers)
        print(url_num,web_data)
        soup = BeautifulSoup(web_data.text, 'lxml')
        ips = soup.find_all('tr')
        ip_list = []
        for i in range(1, len(ips)):
            ip_info = ips[i]
            tds = ip_info.find_all('td')
            ip_list.append(tds[0].text + ':' + tds[1].text)
            for ip in ip_list:
                with open('ip.txt', 'a') as f:
                    f.writelines(ip + '\r\n')
                    f.close()
        time.sleep(1)
    #test_proxies()

# 添加线程模式
def thread_test_proxy(proxy):
    url = "http://www.baidu.com/"
    header = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    }
    try:
        response = requests.get(
            url, headers=header, proxies={"http": proxy}, timeout=3)
        if response.status_code == 200:
            print("该代理IP可用：", proxy)
            exl_save(proxy)
        else:
            print("该代理IP不可用：", proxy)
    except Exception:
        print("该代理IP无效：", proxy)
        pass
# 验证已得到IP的可用性
def test_proxies(proxies):
    proxies = proxies
    print("test_proxies函数开始运行。。。\n", proxies)
    for proxy in proxies:
        test = threading.Thread(target=thread_test_proxy, args=(proxy,))
        test.start()


def test_proxies_slow():
    f = open('ip.txt','r')
    lines = f.readlines()
    # print(lines)
    ip_list = []
    for line in lines:
        tmp1 = line.strip('\r\n')
        ip_list.append(tmp1)
    print(ip_list)
    proxies = ip_list
    url = "http://www.baidu.com/"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        }
    normal_proxies = []
    count = 1
    for proxy in ip_list:
        print("第%s个。。" % count)
        count += 1
        try:
            response = requests.get(url, headers=header, proxies={"http": proxy}, timeout=1)
            #print(url)
            if response.status_code == 200:
                print("该代理IP可用：", proxy)
                normal_proxies.append(proxy)
            else:
                print("该代理IP不可用：", proxy)
        except OSError as err:
            print("该代理IP无效：", proxy)
            pass
    #print(normal_proxies)
    #exl_save(normal_proxies)
'''
proxy_ip = open('proxy_ip.txt', 'w')  # 新建一个储存有效IP的文档
lock = threading.Lock()  # 建立一个锁
def test(i):
    proxy_ip = open('proxy_ip.txt', 'w')  # 新建一个储存有效IP的文档
    lock = threading.Lock()  # 建立一个锁
    # 验证代理IP有效性的方法
    socket.setdefaulttimeout(3)  #设置全局超时时间
    url = "http://www.baidu.com"  #打算爬取的网址
    try:
        proxies="http:"+ ip_list[i]
        proxy_handler = urllib.request.ProxyHandler(proxies)
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders=[("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64)")]
        urllib.request.install_opener(opener)
        res = urllib.request.urlopen(url).read()
        lock.acquire()     #获得锁
        if '百度一下' in res:
            print(proxies,'is OK')
            proxy_ip.write('%s\n' %str(proxies))  #写入该代理IP
        lock.release()     #释放锁
    except Exception as e:
        lock.acquire()
        print(proxies,e)
        lock.release()
proxy_ip.close()
'''
#单线程验证
'''for i in range(len(proxys)):
    test(i)'''
#多线程验证

# 代理IP的信息存储
def write_proxy(proxy):
    print(proxy)
    for ip in proxy:
        with open("ip_proxy.txt", 'a+') as f:
            print("正在写入：", ip)
            f.write(ip + '\n')
    print("录入完成！！！")
def exl_save(normal_proxies):
    f = xlwt.Workbook()  # 创建工作簿bai
    sheet1=f.add_sheet(u'sheet1', cell_overwrite_ok=True)  # 创建sheet
    j = 0
    for i in normal_proxies:
        sheet1.write(0,i)  # 表格的第一行开始写du。第一列，第二列zhi。。。。

    # sheet1.write(0,0,start_date,set_style('Times New Roman',220,True))
    f.save('success-proxy.xls')  # 保存文件dao
    #save_ip(ip_list)
def save_ip(ip_list):
    for ip in ip_list:
        with open('ip.txt', 'a') as f:
            f.writelines(ip+'\r\n')
            f.close()
if __name__ == '__main__':
    url = 'https://www.kuaidaili.com/free/inha/'
    #ip_list = get_ip_list(url)
    f = open('ip.txt','r')
    lines = f.readlines()
    # print(lines)
    ip_list = []
    for line in lines:
        tmp1 = line.strip('\r\n')
        ip_list.append(tmp1)
    proxies= ip_list
    test_proxies(proxies)

    '''threads = []
    for i in range(len(ip_list)):
        thread = threading.Thread(target=test, args=[i])
        threads.append(thread)
        thread.start()
    # 阻塞主进程，等待所有子线程结束
    for thread in threads:
        thread.join()
    test(i)'''

    #print(ip_list)
