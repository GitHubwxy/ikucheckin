# 通用机场签到😍<br/>
>只要机场网站''' Powered by SSPANEL ''',就可以进行签到。要确认是否是''' Powered by SSPANEL '''，在机场首页滑倒最底端就可以看到。例如：
![Y0}SY$J`8837H8T5GXM1DZY](https://user-images.githubusercontent.com/21276183/214764546-4f66333a-cb9b-420e-8260-697d26fb4547.png)
## 作用
>每天进行签到，获取额外的流量奖励

## 推送方式
  🚀🚀该脚本支持以下推送方式：
  - <a href = 'https://sct.ftqq.com/r/5126'>Server酱</a>：如果不需要推送，就将下面的SCKEY参数的值设置为<b>空</b>
  - Telegram机器人：如果需要使用Telegram推送，请配置TG_BOT_TOKEN和TG_CHAT_ID参数

# 部署过程
 
1. 右上角Fork此仓库
2. 然后到`Settings`→`Secrets and variables`→`Actions` 新建以下机密：

| 参数   | 是否必须  | 内容  | 
| ------------ | ------------ | ------------ |
| CONFIG| 是  | 账号密码  |
| SCKEY  | 否  | Sever酱秘钥  |
| TG_BOT_TOKEN  | 否  | Telegram机器人Token  |
| TG_CHAT_ID  | 否  | Telegram聊天ID  |
<br/>
<b>其中URL的值必须是机场网站的地址，例如：https://example.com</b>,尾部不要加''' / '''号 config写法：一行账号一行密码

3. 到`Actions`中创建一个workflow，运行一次，以后每天项目都会自动运行。<br/>
4. 最后，可以到Run sign查看签到情况，同时也会将签到详情推送到Sever酱和/或Telegram。

## Telegram机器人配置说明
1. 在Telegram中搜索 @BotFather 并开始对话
2. 发送 /newbot 命令，按照提示创建一个新的机器人
3. 创建成功后，BotFather 会发给你一个Token，这就是你需要的 TG_BOT_TOKEN
4. 搜索你刚创建的机器人，并开始对话
5. 搜索 @userinfobot 并开始对话，它会返回你的 Chat ID，这就是你需要的 TG_CHAT_ID
6. 在项目的 Secrets 中添加 TG_BOT_TOKEN 和 TG_CHAT_ID
