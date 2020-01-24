#coding: utf-8
'''
发送带附件的邮件
'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

HOST = "smtp.qq.com"
USER = '1752570559'
PWD = 'gzztgylcybavbfba'

SUBJECT = u"官网业务服务质量周报" # 邮件标题
TO = [
    '1752570559@qq.com',
    '601222543@qq.com',
] # 到哪里去
FROM = "1752570559@qq.com" # 从哪里来

# 添加图片函数
def addimg(src,imgid):
    fp = open(src, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', imgid)
    return msgImage

msg = MIMEMultipart('related')  # 生成多类型邮件对象
msgtext = MIMEText("<font color=red>官网业务周平均延时图表:<br><img src=\"cid:weekly\" border=\"1\"><br>详细内容见附件。</font>","html","utf-8")
msg.attach(msgtext) # 添加文本
msg.attach(addimg("img/weekly.png","weekly")) # 添加图片

# 添加excel附件 用二进制打开文件的时候，发送附件时候Content-Type 为 application/octet-stream（发送二进制文件类型）
attach1 = MIMEText(open("doc/week_report.xlsx", "rb").read(), "base64", "utf-8")
attach1["Content-Type"] = "application/octet-stream" # 文件类型 二进制类型
#设置附件名称
attach1["Content-Disposition"] = "attachment; filename=\"梦特卡罗(1周赌博收益).xlsx\"".decode("utf-8").encode("gbk")

attach2 = MIMEText(open("doc/week_report.xlsx", "rb").read(), "base64", "utf-8")
attach2["Content-Type"] = "application/octet-stream" # 文件类型
attach2["Content-Disposition"] = "attachment; filename=\"云顶山庄(骗人报表).xlsx\"".decode("utf-8").encode("gbk")

# 添加两个附件
msg.attach(attach1)
msg.attach(attach2)

msg['Subject'] = SUBJECT
msg['From']=FROM
msg['To'] = ';'.join(TO)
try:
    server = smtplib.SMTP_SSL(HOST,465)
    server.connect(HOST)
    server.login(USER,PWD)
    server.sendmail(FROM, TO, msg.as_string())
    server.quit()
    print "邮件发送成功！"
except Exception, e:
    print "失败："+str(e)
