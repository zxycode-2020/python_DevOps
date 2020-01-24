#coding:utf8
#!/usr/bin/python
import difflib

text1 = u"""text1:
This module provides classes and functions for comparing sequences.
including HTML and context and unified diffs.
difflib document v7.4
add string
"""

text1_lines = text1.splitlines()

text2 = u"""text2:
I amd 58 洗澡城
This module provides classes and functions for Comparing sequences.
including HTML and context and unified diffs.
difflib document v7.5"""

text2_lines = text2.splitlines()

d = difflib.HtmlDiff()  # html 文档对比
print d.make_file(text1_lines, text2_lines)
