import itchat, time
from itchat.content import *
import os

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    #msg.user.send('%s: %s' % (msg.type, msg.text))
    print('%s: %s' % (msg.type, msg.text))


'''
@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    #return '@%s@%s' % (typeSymbol, msg.fileName)
    print('@%s@%s' % (typeSymbol, msg.fileName))
'''

#@itchat.msg_register(FRIENDS)
#def add_friend(msg):
#    msg.user.verify()
#    msg.user.send('Nice to meet you!')

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING, PICTURE, RECORDING, ATTACHMENT, VIDEO], isGroupChat=True)
def text_reply(msg):
    group_nick_name = msg.User.NickName
    file_dir = "data/" + group_nick_name
    cmd = "mkdir -p " + file_dir + "/files"
    os.system(cmd)
    text = ""
    if msg.Type in [PICTURE, RECORDING, ATTACHMENT, VIDEO]:
        msg.download(msg.fileName)
        cmd = "mv " + msg.fileName + " " + file_dir + "/files"
        os.system(cmd)
        text = "@" + msg.type + "@" + msg.fileName
    else:
        text = msg.text
    import datetime 
    dt_object = datetime.datetime.fromtimestamp(msg.CreateTime)
    str_time = dt_object.strftime('%Y-%m-%d %H:%M:%S')
    text = text.replace("\n", "\$")
    text = str_time + "\t" + group_nick_name + "\t" + msg.ActualNickName + "\t" + text + "\t" + msg.Type
    text = text + "\t" + msg.Url
    print(msg)
    print(text)
    out_file = file_dir + "/log.txt" 
    f = open(out_file,"a")
    f.write(text+"\n")
    f.flush()
    f.close()

itchat.auto_login(enableCmdQR=2,hotReload=True)
itchat.run(True)



'''


    #print("###msg:",msg)
    print("type:", type(msg))
    #print("###msg.User:", type(msg.User), msg.User)
    print("group name:", msg.User.UserName)
    print("group name:", msg.User.NickName)
    print("FromUserName:", msg.FromUserName)
    print("ActualUserName:", msg.ActualUserName)
    print("ActualNickName:", msg.ActualNickName)
    print("Text:", msg.text)
    mlist = msg.User.MemberList
    #print("MemberList:", type(msg.User.MemberList), msg.User.MemberList)
    m0=msg.User.MemberList[0]
    print("MemberList[0]:", type(m0), m0)
    #for m in mlist:
    #    print(m.UserName, m.NickName)
'''
