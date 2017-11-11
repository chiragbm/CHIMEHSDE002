'''
@author: chiragm
'''
from urllib.request import urlopen

from bs4 import BeautifulSoup

output = open('quotes_file.txt','w', encoding = 'utf-8')
link = "https://www.goodreads.com/quotes/search?utf8=&q=marktwain&commit=Search"
response = urlopen(link)
content = response.read()
soup = BeautifulSoup(content, 'lxml')

[s.extract() for s in soup('script')]
[s.extract() for s in soup('style')]

count = 0
for ele in soup.findAll(attrs={'class' : 'quoteText'})[:10]:
    count+=1
    qt = str(ele.text.strip().split('\n')[0].encode('utf-8'))
    output.write('Quote%s : %s \n'%(str(count), qt))