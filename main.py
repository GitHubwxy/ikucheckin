import requests, json, re, os

session = requests.session()
# 机场的地址
url = os.environ.get('URL')
# 配置用户名（一般是邮箱）

config = os.environ.get('CONFIG')
# server酱
SCKEY = os.environ.get('SCKEY')
# Telegram 机器人配置
TG_BOT_TOKEN = os.environ.get('TG_BOT_TOKEN')
TG_CHAT_ID = os.environ.get('TG_CHAT_ID')

login_url = '{}/auth/login'.format(url)
check_url = '{}/user/checkin'.format(url)

def send_telegram_message(message):
    """通过Telegram机器人发送消息"""
    if TG_BOT_TOKEN and TG_CHAT_ID:
        try:
            telegram_url = f"https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage"
            data = {
                "chat_id": TG_CHAT_ID,
                "text": message,
                "parse_mode": "HTML"
            }
            response = requests.post(telegram_url, data=data)
            if response.status_code == 200:
                print('Telegram推送成功')
            else:
                print(f'Telegram推送失败: {response.text}')
        except Exception as e:
            print(f'Telegram推送异常: {str(e)}')

def sign(order,user,pwd):
        global url,SEKEY
        header = {
        'origin': url,
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
        }
        data = {
        'email': user,
        'passwd': pwd
        }
        try:
                print(f'===账号{order}进行登录...===')
                print(f'账号：{user}')
                response = json.loads(session.post(url=login_url,headers=header,data=data).text)
                print(response['msg'])
                # 进行签到
                result = json.loads(session.post(url=check_url,headers=header).text)
                print(result['msg'])
                content = result['msg']
                # 进行推送
                if SCKEY != '':
                        push_url = 'https://sctapi.ftqq.com/{}.send?title=机场签到&desp={}'.format(SCKEY, content)
                        requests.post(url=push_url)
                        print('推送成功')
                # Telegram推送
                tg_message = f"✅ 机场签到结果\n\n账号：{user}\n结果：{content}"
                send_telegram_message(tg_message)
        except:
                content = '签到失败'
                print(content)
                if SCKEY != '':
                        push_url = 'https://sctapi.ftqq.com/{}.send?title=机场签到&desp={}'.format(SCKEY, content)
                        requests.post(url=push_url)
                        print('推送成功')
                # Telegram推送失败信息
                tg_message = f"❌ 机场签到失败\n\n账号：{user}"
                send_telegram_message(tg_message)
        print('===账号{order}签到结束===\n'.format(order=order))
if __name__ == '__main__':
        configs = config.splitlines()
        if len(configs) %2 != 0 or len(configs) == 0:
                print('配置文件格式错误')
                exit()
        user_quantity = len(configs)
        user_quantity = user_quantity // 2
        for i in range(user_quantity):
                user = configs[i*2]
                pwd = configs[i*2+1]
                sign(i,user,pwd)
        