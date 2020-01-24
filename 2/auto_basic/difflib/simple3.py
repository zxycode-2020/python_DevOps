#coding:utf8
#!/usr/bin/python
import difflib
import sys

# 在控制台接受两个参数 ，文件名，和脚本在相对路径
try:
    textfile1=sys.argv[1]
    textfile2=sys.argv[2]
except Exception,e:
    print "Error:"+str(e)
    print "Usage: simple3.py filename1 filename2"
    sys.exit()

def readfile(filename):
    try:
        fileHandle = open (filename, 'rb' )  # 二进制读取文件
        text = fileHandle.read().splitlines()  # 按照行分割
        fileHandle.close() # 关闭文件对象
        return text # 返回文件内容
    except IOError as error:
       print('Read file Error:'+str(error)) # 异常处理
       sys.exit()

if __name__ == '__main__':
    # 异常判断 如果文件为空 则退出脚本
    if textfile1 == "" or textfile2=="":
        print "Usage: simple3.py filename1 filename2"
        sys.exit()

    # 读取文件
    text1_lines = readfile(textfile1)
    text2_lines = readfile(textfile2)

    d = difflib.HtmlDiff()
    html = d.make_file(text1_lines, text2_lines).replace('ISO-8859-1','utf-8')
    print html