import urllib.parse
import urllib.request
import urllib.error

url = "https://blog.csdn.net/qq_42539533/article/details/88902429"
wrong_url = "https://blog.csdn.net/qq_42539533/article/details/88902429123"
wrong_url2 = "http://www.doudan111.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"}

try:
    request = urllib.request.Request(url=wrong_url2, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    print(content)
except urllib.error.HTTPError as e:
    print("系统正在升级...")
except urllib.error.URLError as e:
    print("我都说了,系统正在升级")
