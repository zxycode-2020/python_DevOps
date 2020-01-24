#coding:utf8
#!/usr/bin/python
import difflib

text1 = """text1:
This module provides classes and functions for comparing sequences.
including HTML and context and unified diffs.
difflib document v7.4
add string
"""

text1_lines = text1.splitlines() #按照行进行分割

text2 = """text2:
This module provides classes and functions for Comparing sequences.
including HTML and context and unified diffs.
difflib document v7.5"""

text2_lines = text2.splitlines() # 按照行进行分割
print text2_lines

d = difflib.Differ() # 比较对象  控制台对比方法
diff = d.compare(text1_lines, text2_lines)  # 调用compare  传入两个参数进行比较
print '\n'.join(list(diff))
