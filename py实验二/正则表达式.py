
#匹配网址
import re
'''
str = ["http://www.interoem.com/messageinfo.asp?id=35",
       "http://3995503.com/class/class09/news_show.asp?id=14",
       "http://lib.wzmc.edu.cn/news/onews.asp?id=769",
       "http://www.zy-ls.com/alfx.asp?newsid=377&id=6",
       "http://www.fincm.com/newslist.asp?id=415"]

for i in str:
      per = re.findall(r'http://.*\..*?/',i)
      print(per)

#匹配正确的ip地址

（格式为：pattern=’正则表达式’
	example=input(‘请输入一个IP地址’)
	print(re.findall(pattern,example))
）
'''
'''
pattern=r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])'
example=input('请输入一个IP地址')
l=re.search(pattern,example)
print(l.group())

#
import re
f=open("test.txt",encoding='utf-8')
data = f.readlines()
f.close()

for line in data:
      result=re.search('(\d+).(\d+)',line)
      t1=result.group(1)
      t2=result.group(2)
      f1=open("test1.txt","a+",encoding='utf-8')
      f1.write(t1+t2+'\n')
f1.close()
'''
#匹配电子邮件的格式
import re
s2='abc_12@163.com'
pattern=r'(^[a-z]|[A-Z])(\w+)(@163.com)'
print(re.search(pattern,s2).group())











