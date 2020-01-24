# -*- coding:utf-8 -*-
import psutil
import winsound
import time

def getDisk():
    disk = psutil.disk_partitions()  # 获取硬盘信息
    print disk
    for i in disk:
        if i.opts != 'cdrom': # 除了光驱以外的设备
            print "磁盘：%s   分区格式:%s" % (i.device, i.fstype)
            disk_use = psutil.disk_usage(i.device)
            print "使用了：%sG,空闲：%sM,总共：%sM,使用率\033[1;31;m%s%%\033[0m," % (
            disk_use.used / 1024 / 1024 / 1024, disk_use.free / 1024 / 1024, disk_use.total / 1024 / 1024, disk_use.percent)


# getDisk()

def cpu():
    while True:
        time.sleep(1)
        cpu_liyonglv = psutil.cpu_percent() # 返回浮点型
        print "当前cpu利用率：\033[1;31;m %s%%\033[0m" % cpu_liyonglv
        if cpu_liyonglv > 20.0:  # 利用率大于15 则报警
            # print '利用率超标'
            baojing()


def baojing():
    winsound.PlaySound('1.wav', winsound.SND_ALIAS)
    print 'cpu 利用率过高，红色警报'


# cpu()

def getMem():
    memory = psutil.virtual_memory() # 获取内存对象
    print '使用了', memory.used / 1024 / 1024
    print '总共', memory.total / 1024 / 1024
    ab = float(memory.used) / float(memory.total) * 100
    print "利用率：%.2f%%" % ab
    #print psutil.swap_memory() #虚拟内存


def getNet():
    count = psutil.net_io_counters()
    print "发送字节数：\033[1;31;42m%s\033[0mbytes,接收字节数：\033[1;31;42m%s\033[0mbytes,发送包数：%s,接收包数%s" % (
    count.bytes_sent, count.bytes_recv, count.packets_sent, count.packets_recv)

    users = psutil.users()
    print "当前登录用户：", users[0].name
    # 时间
    curent_time = psutil.boot_time()

    curent_time_1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(curent_time))
    print curent_time_1


if __name__ == '__main__':
    #获取系统进程信息
    # pids = psutil.pids()
    # pro = psutil.Process(1088)
    # print pro.name()
    # print pro.exe()
    # print pro.cwd()
    # print pro.uids() # linux
    # print pro.gids() # linux
    # cpu()
    #getDisk()
    #getMem()
    getNet()
