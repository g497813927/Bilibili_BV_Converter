import requests
import sys
import locale

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


chs = [
    '请输入BV号：',
    '输入错误！BV号应由\'BV\'开头！',
    '查询出错了！\n可能的原因：\n\t该视频不存在所指定的p！',
    '查询出错了！\n可能的原因：\n\t1、你调用的次数太多暂时冻结了，要过一会儿才可以继续查询！\n\t2、你的网络可能出现了一些异常\n\t3、不存在这一个视频',
    '抱歉，请重试！',
    '对应的CID号为：',
    '请输入你需要查询的对应视频的p数（仅限数字）\n（0代表视频第一p，1代表视频第二p，以此类推）\n',
    '输入错误！p数需为自然数！'
]

eng = [
    'Please input BV number:',
    'Input Error! BV number should start with \'BV\'!',
    'Query Error!\nPossible Reason:\n\tThis video might not have an AV number',
    'Query Error!\nPossible Reasons:\n\t1. You use this too much in short period, please query later!' +
    '\n\t2.You might encountered with some internet issues\n\t3.The video does not exist',
    'Sorry, please try again!',
    'The CID number for the video you input is: ',
    'Please input the part of the video you want to\n(Number only, 0 stands for the first part, ' +
    '1 stands for the second part, and so on.)\n',
    'Input error! The part number should be a whole number!'
]


# Function when it is short link
def get_url(link):
    response = requests.get(link, headers=headers)
    return response.url


language = locale.getdefaultlocale()[0]

try:
    temp = sys.argv[1]  # BV号是否在命令行中存在
    temp = sys.argv[2]  # 对应的p
except IndexError:
    if language == 'zh_CN':
        print('你当前的系统语言是简体中文，需要更改程序显示语言吗？')
        print('Your current language display is Chinese Simplified, do you want to switch language?')
        lang = chs
    else:
        print('你当前的系统语言不是简体中文，需要更改程序显示语言吗？')
        print('Your current language display is English, do you want to switch language?')
        lang = eng
    while True:
        switch_confirmation = input('(Y/N)')
        if switch_confirmation.lower() == 'y' or switch_confirmation.lower() == 'yes' \
                or switch_confirmation.lower() == 't' or switch_confirmation.lower() == 'true'\
                or switch_confirmation == '是' or switch_confirmation == '确定':
            switch = True
            break
        elif switch_confirmation.lower() == 'n' or switch_confirmation.lower() == 'no' \
                or switch_confirmation.lower() == 'f' or switch_confirmation.lower() == 'false'\
                or switch_confirmation == '否':
            switch = False
            break
        else:
            print('输入错误！')
            print('Unknown Selection, please try again!')
    if switch:
        while True:
            print('1. 简体中文\n2. English')
            language_selection = input('请选择语言(Select language):')
            if language_selection == '1' or language_selection.lower() == 'chs' or language_selection == '简体中文' \
                    or language_selection == '中文' or language_selection.lower() == 'cn' \
                    or language_selection.lower() == 'china' or language_selection.lower() == 'chinese':
                lang = chs
                break
            elif language_selection == '2' or language_selection.lower() == 'eng' \
                    or language_selection.lower() == 'english':
                lang = eng
                break
            else:
                print('输入错误，请重试\n(Unknown Selection, please try again)')
else:
    if language == 'zh_CN':
        lang = chs
    else:
        lang = eng
try:
    sys.argv[1]
except IndexError:
    BV_Number = input(lang[0])
    while True:
        if BV_Number.lower().find('bilibili.com') > 0 \
                or BV_Number.lower().find('b23.tv') > 0:
            if get_url(BV_Number).upper().find('BV') < len(get_url(BV_Number)) - 2:
                BV_Number = get_url(BV_Number)
                break
            else:
                print(lang[1])
                BV_Number = input(lang[0])
        else:
            if BV_Number.upper().find('BV') == 0:
                break
            else:
                print(lang[1])
                BV_Number = input(lang[0])
else:
    BV_Number = sys.argv[1]
    while True:
        if BV_Number.lower().find('bilibili.com') > 0 \
                or BV_Number.lower().find('b23.tv') > 0:

            if get_url(BV_Number).upper().find('BV') < len(get_url(BV_Number)) - 2:
                BV_Number = get_url(BV_Number)
                break
            else:
                print(lang[1])
                BV_Number = input(lang[0])
        else:
            if BV_Number.upper().find('BV') == 0:
                break
            else:
                print(lang[1])
                BV_Number = input(lang[0])

if BV_Number.find('?') != -1:
    BV_Number = "BV" + BV_Number[BV_Number.upper().find('BV')+2:BV_Number.find('?')]
else:
    BV_Number = "BV" + BV_Number[BV_Number.upper().find('BV')+2:]

try:
    sys.argv[2]
except IndexError:
    while True:
        try:
            p_number = int(input(lang[6]))
        except TypeError:
            print(lang[7])
        else:
            if p_number < 0:
                print(lang[7])
            else:
                break
else:
    try:
        p_number = int(sys.argv[2])
    except TypeError:
        print(lang[7])
        sys.exit(0)
    else:
        if p_number < 0:
            print(lang[7])
            sys.exit(0)

url = 'https://api.bilibili.com/x/player/pagelist?bvid={}&jsonp=jsonp'

r = requests.get(url.format(BV_Number), headers=headers)
if r.status_code == 200:
    try:
        j_cid = r.json()['data'][p_number]['cid']
        print(lang[5] + str(j_cid))
    except TypeError:
        print(lang[2])
    except IndexError:
        print(lang[2])
else:
    print(lang[3])
