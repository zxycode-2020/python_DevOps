#coding: utf-8
'''
发送带图片的邮件
'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

HOST = "smtp.qq.com"
USER = '1752570559'
PWD = 'gzztgylcybavbfba'

SUBJECT = u"业务性能数据报表"
TO = [
    "1752570559@qq.com",
    '601222543@qq.com',
]

# TO =  '1752570559@qq.com'

FROM = "1752570559@qq.com"

# 添加图片函数
def addimg(src,imgid):
    fp = open(src, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', imgid)
    return msgImage

msg = MIMEMultipart('related')
msgtext = MIMEText("""
<table width="600" border="0" cellspacing="0" cellpadding="4">
      <tr bgcolor="#CECFAD" height="20" style="font-size:14px">
        <td colspan=2>*官网性能数据  <a href="monitor.domain.com">更多>></a></td>
      </tr>
      <tr bgcolor="#EFEBDE" height="100" style="font-size:13px">
        <td>
         <img src="cid:io"></td><td>
         <img src="cid:key_hit"></td>
      </tr>
      <tr bgcolor="#EFEBDE" height="100" style="font-size:13px">
         <td>
         <img src="cid:men"></td><td>
         <img src="cid:swap"></td>
      </tr>
    </table>""","html","utf-8")
msg.attach(msgtext) #把html文档加载到邮件对象中
msg.attach(addimg("img/bytes_io.png","io")) # 向邮件对象中添加一个图片
msg.attach(addimg("img/myisam_key_hit.png","key_hit")) # 向邮件对象中添加一个图片
msg.attach(addimg("img/os_mem.png","men")) # 向邮件对象中添加一个图片
msg.attach(addimg("img/os_swap.png","swap")) # 向邮件对象中添加一个图片

msg['Subject'] = SUBJECT # 邮件标题
msg['From']=FROM
msg['To']= ';'.join(TO)
try:
    server = smtplib.SMTP_SSL(HOST,465)
    server.connect(HOST)
    server.login(USER,PWD)
    # TO = ';'.join(TO)
    server.sendmail(FROM, TO, msg.as_string())
    server.quit()
    print "邮件发送成功！"
except Exception, e:
    print "失败："+str(e)
