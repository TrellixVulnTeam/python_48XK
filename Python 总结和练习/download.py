# -*- coding: gbk -*-
from bs4 import BeautifulSoup
import urllib
import codecs
import re
def download(url,name):
    '''
        ���ݲ��ҵ����½�url�����½�ҳ������ݡ�nameΪ��ȡ����С˵������
    '''
    soup=BeautifulSoup(urllib.urlopen(url).read())#�����½ڵ�ҳ��
    cont=soup.find(id="contents").text#��ȡidΪcontents��ǩ�������
    title=soup.title.text#�������½���Ҳ����ҳ���title
    f=codecs.open('%s.txt'%name,'a','utf-8')#��С˵���������ļ����ƣ�����׷�ӵķ�ʽ��
    f.write('\r\n'+title+'\r\n')#��д���½�����
    f.write(cont)#��д���½�����
    f.close()#�ر��ļ�����ʵ���ļ���with����~
def search():
    name=raw_input('С˵����')#��ȡ����
    soup=BeautifulSoup(urllib.urlopen('http://so.23wx.com/cse/search?q=%s&click=1&s=15772447660171623812&nsid='%name).read())
    #������������ݣ��ϳ�����url������ȡ�������ݣ���beautifulsoup����heml
    N=soup.find('a', {'class': 'result-game-item-title-link'})#�����ض�����ҵ�С˵������
    print N['title'],N['href']
    return N

def getChapter(url):
    '''
        ����С˵���ӻ�ȡ�����½ڣ���Ϊ�½ڿ��ܴﵽ��ǧ~���Դ˴��õ�������
    '''
    b=urllib.urlopen(url).read()#��ȡҳ�������
    a=re.compile(r'<a href="(.*?)">(.*?)</a>')#html�����Ĺ��ߺ�����ںܶ�ı�ǩ���������ˣ����Բ��ò��Լ�д��������ȡÿ���½ڵ�url
    aa=a.findall(b)#��ҳ���������ҵ������½ڵ����ӣ���Ϊ���������·��������Ҫ�Լ��ϳɾ���·����
    for i in aa:
            if re.compile('^[0-9]*\.html').match(i[0]):
                yield url+i[0],i[1]#ÿ��ѭ���õ�һ���½����ƣ��˴��õ���������
N=search()
num=0
for url in getChapter(N['href']):
    num+=1
    try:                            #ͨ���쳣���������ֳ���������~
        download(url[0],N['title'])
        t='-'*(50-len(url[1]))
        print '%s%s������'%(url[1],t)
    except:
        print 'error'
'''
   �˴��������Һ�����д�����ģ����ڿ���ʵ�ڳ�ª����~ע�;��������������׵ĵط�@�Ҿ��У����������ʻ���ģ����Լ�ѧϰ��~
'''
    

