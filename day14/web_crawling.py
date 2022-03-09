#pip install BeautifulSoup4
#pip install urlopen
import urllib.request

a = urllib.request.urlopen("https://www.naver.com/")
#print(a.read())
print(a.read().decode("utf-8"))