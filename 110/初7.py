import re
s1=input('請輸入一串句子:')
s2=input('請輸入想要找的字母:')
s1=s1.lower()
s2=s2.lower()
print(len(re.findall(s2,s1)))