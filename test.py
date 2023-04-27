import itchat, time
from itchat.content import *

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    #msg.user.send('%s: %s' % (msg.type, msg.text))
    print('%s: %s' % (msg.type, msg.text))

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    #return '@%s@%s' % (typeSymbol, msg.fileName)
    print('@%s@%s' % (typeSymbol, msg.fileName))

#@itchat.msg_register(FRIENDS)
#def add_friend(msg):
#    msg.user.verify()
#    msg.user.send('Nice to meet you!')

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING], isGroupChat=True)
def text_reply(msg):
    print("###msg:",msg)
    if msg.isAt:
        #msg.user.send(u'@%s\u2005I received: %s' % (
        #    msg.actualNickName, msg.text))
        print(u'@%s\u2005I received: %s' % (msg.actualNickName, msg.text))

itchat.auto_login(enableCmdQR=2)
itchat.run(True)
