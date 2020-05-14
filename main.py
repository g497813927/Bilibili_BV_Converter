import requests
import sys

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'DNT': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4083.0 Safari/537.36 Edg/82.0.458.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'en-US,en;q=0.9'
}


# Function when it is short link
def get_url(link):
    response = requests.get(link, headers=headers)
    return response.url


try:
    sys.argv[1]
except IndexError:
    BV_Number = input('请输入BV号：')
    while True:
        if BV_Number.lower().find('bilibili.com') > 0 \
                or BV_Number.lower().find('b23.tv') > 0:
            if get_url(BV_Number).upper().find('BV') < len(get_url(BV_Number)) - 2:
                BV_Number = get_url(BV_Number)
                break
            else:
                print('输入错误！BV号应由BV开头！')
                BV_Number = input('请输入BV号：')
        else:
            if BV_Number.upper().find('BV') == 0:
                break
            else:
                print('输入错误！BV号应由BV开头！')
                BV_Number = input('请输入BV号：')
else:
    BV_Number = sys.argv[1]
    while True:
        if BV_Number.lower().find('bilibili.com') > 0 \
                or BV_Number.lower().find('b23.tv') > 0:

            if get_url(BV_Number).upper().find('BV') < len(get_url(BV_Number)) - 2:
                BV_Number = get_url(BV_Number)
                break
            else:
                print('输入错误！BV号应由BV开头！')
                BV_Number = input('请输入BV号：')
        else:
            if BV_Number.upper().find('BV') == 0:
                break
            else:
                print('输入错误！BV号应由BV开头！')
                BV_Number = input('请输入BV号：')

if BV_Number.find('?') != -1:
    BV_Number = BV_Number[BV_Number.find('BV'):BV_Number.find('?')]
else:
    BV_Number = BV_Number[BV_Number.find('BV'):]

url = 'https://api.bilibili.com/x/web-interface/archive/stat?bvid={}'

r = requests.get(url.format(BV_Number), headers=headers)
if r.status_code == 200:
    try:
        j = r.json()['data']
        AV_Number = j['aid']
    except Exception:
        print('查询出错了！\n可能的原因：\n\t该视频可能并不存在AV号')
else:
    print('查询出错了！\n可能的原因：\n\t1、你调用的次数太多暂时冻结了，要过一会儿才可以继续查询！\n\t2、你的网络可能出现了一些异常')
try:
    AV_Number
except Exception:
    print('抱歉，请重试！')
else:
    print('对应的AV号为：AV' + str(AV_Number))
