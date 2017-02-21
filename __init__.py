# encoding:utf-8
from bs4 import BeautifulSoup
from urllib import urlopen
import urllib2
import time
import sys 
import json
import smtplib
from email.mime.text import MIMEText 
from email.header import Header
import string
from time import sleep

def rm_all_pasce(text):
    return text.replace("\n", "").replace("\t", "").replace(' ', '').replace('\r', '').replace('<<收起', '')


def get_html(site):
    hdr = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    req = urllib2.Request(site, headers=hdr)
    try:
        data = urllib2.urlopen(req, timeout=4)
        page = data.read()
        return page
        print page
        print '===请求到了==='
    except:
        return '1错误'
    try:
#         page1 = page.decode('gbk')
        return BeautifulSoup(page);
    except:
        return BeautifulSoup(page);
    
    
    
def send_email(username='qingju.li@linjiahaoyi.com', password='Likaibo150', receiver= 'qingju.li@linjiahaoyi.com',text=''):
    subject = text #发送邮箱服务器
    smtpserver = 'smtp.exmail.qq.com' 
#中文需参数‘utf-8’,单字节字符不需要
    receiver =string.splitfields(receiver, ',')
    msg = MIMEText(u'数据导入出错了', 'text', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = '李庆举'
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(username, receiver, msg.as_string())
    smtp.quit()   


while True:
    try: 
        token_str =json.loads(get_html('https://www.wesai.com/index.php?r=user/getcuruser'))['data']['token'].encode('utf8')
        print token_str
        bs_txt_html =get_html('https://www.wesai.com/api/rest/'+token_str+'/Java/item/queryItem/%7B%22itemQuery%22:%7B%22allPlatform%22:false,%22cityId%22:%220%22,%22cityName%22:%22%E5%85%A8%E5%9B%BD%22,%22itemTypeId%22:null,%22itemTypePid%22:%228a8283eb55dfd9600156029f3ce00011%22,%22keyword%22:null,%22onlineId%22:null,%22showStartTime%22:null,%22showEndTime%22:null,%22venueId%22:%22%22,%22orderType%22:null,%22curpage%22:1,%22pagesize%22:8%7D%7D?v=1487678065856')
        print bs_txt_html
        bs_txt_html_str =bs_txt_html.encode('utf-8')
        bs_txt_html_str_json =json.loads(bs_txt_html_str)
        bs_txt_html_str_json_array =bs_txt_html_str_json['itemResult']['items']
        for one_bs_txt_html_str_json_array in bs_txt_html_str_json_array:
            one_bs_txt_html_str_json_array_one_str = one_bs_txt_html_str_json_array['itemTitleCN'].encode('utf8')
            if '杭州' in one_bs_txt_html_str_json_array_one_str:
                send_email(text ='开始卖票了');
                sleep(60*5)
        sleep(30)
    except:
        pass
# print bs_txt_html_str
# bs_txt_html_list =bs_txt_html.findAll('div', {'class':'ddleft'})
# for one_bs_txt_html_list in bs_txt_html_list:
#     print rm_all_pasce(one_bs_txt_html_list.get_text().encode('utf-8'))
# print(len(bs_txt_html_list))

