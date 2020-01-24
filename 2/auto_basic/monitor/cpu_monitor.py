#coding:utf8
import psutil
import time
import datetime
from monitor.sendmail import *

last_alert_stamp = time.time()
cpu_percent = [] #cpu利用率

# 获取cpu 利用率，并且加入列表
def get_cpu_percent():
    cpu_per = psutil.cpu_percent()
    cpu_percent.append(cpu_per) # 添加一个利用率
    if len(cpu_percent) > 12: #超出一定长度则删除
        cpu_percent.pop(0)  #删除列表中第一个元素

def cpu_alert():
    global last_alert_stamp
    res = sum(cpu_percent) #求总和
    avg = res / len(cpu_percent)
    now_stamp = time.time() # 获取现在系统时间戳
    if now_stamp > last_alert_stamp + 20:
        if avg >= 20:
            last_alert_stamp = now_stamp # 刷新上次报警时间
            if avg >= 90:
                # 刷新上次警报时间
                title =  '橙色警报'
                now = datetime.datetime.fromtimestamp(now_stamp).strftime('%Y-%m-%d %H:%M:%S')
                send_mail(mailto_list, title, now + title + '洗脚城炸了')
            elif avg >= 50:
                title = '红色警报'
                now = datetime.datetime.fromtimestamp(now_stamp).strftime('%Y-%m-%d %H:%M:%S')
                send_mail(mailto_list, title, now + title + '洗脚城炸了')

            elif avg >= 20:
                title = '白色警报'
                now = datetime.datetime.fromtimestamp(now_stamp).strftime('%Y-%m-%d %H:%M:%S')
                send_mail(mailto_list, title, now + title + '洗脚城炸了')

if __name__ == '__main__':
    while True:
        get_cpu_percent()
        time.sleep(2)
        cpu_alert()
