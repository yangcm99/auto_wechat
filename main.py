from wxauto import WeChat
import time
import yi_34b_chat
import utils

# 获取微信窗口对象
wx = WeChat()
# 输出 > 初始化成功，获取到已登录窗口
# 设置监听列表
listen_list = [
    '周子枫',
    '夏纤纤',
    '政治局'
]

# 循环添加监听对象
for i in listen_list:
    wx.AddListenChat(who=i, savepic=True)

# 持续监听消息，并且收到消息后回复“收到”
wait = 1  # 设置1秒查看一次是否有新消息
while True:
    msgs = wx.GetListenMessage()
    for chat in msgs:
        who = chat.who  # 获取聊天窗口名（人或群名）
        one_msgs = msgs.get(chat)  # 获取消息内容
        logger = utils.init_logger('log/chat_log_{}'.format(who))
        # 回复收到
        for msg in one_msgs:
            if msg.type == 'sys':
                logger.info(f'【系统消息】{msg.content}')
            elif msg.type == 'friend':
                sender = msg.sender  # 这里可以将msg.sender改为msg.sender_remark，获取备注名
                print(f'{sender.rjust(20)}：{msg.content}')
                logger.info(f'{sender.rjust(20)}：{msg.content}')
                if utils.is_path_string(msg.content):  # 判断是否非文本信息
                    res = yi_34b_chat.yi_34b_chat_main(content='你能识别除了文本以外的文件吗？',
                                                       role='user')
                    chat.SendMsg(res)
                else:
                    res = yi_34b_chat.yi_34b_chat_main(content=str(msg.content) + '。' + '你回复与我字数差不多的内容。',
                                                       role='user')
                    chat.SendMsg(res)

            elif msg.type == 'self':
                print(f'{msg.sender.ljust(20)}：{msg.content}')
                logger.info(f'{msg.sender.ljust(20)}：{msg.content}')
            elif msg.type == 'time':
                print(f'\n【时间消息】{msg.time}')
                logger.info(f'\n【时间消息】{msg.time}')
            elif msg.type == 'recall':
                print(f'【撤回消息】{msg.content}')
                logger.info(f'【撤回消息】{msg.content}')
    time.sleep(wait)
