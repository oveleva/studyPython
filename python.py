# coding: utf-8
string = 'test Test'
# 首字母大写/不修改变量
print(string.title())
print(string)
# ~ Test Test
# ~ test Test
# 字母全大写/不修改变量
print(string.upper())
# ~ TEST TEST
# 字母全小写/不修改变量
print(string.lower())
# ~ test test
# 制表符
print('\t' + string)
# ~  test Test
# 换行
print('\n' + string)
# ~
# ~test Test
# 删除空白/不修改变量
test = ' 233 test '
print(test.rstrip())
print(test.lstrip())
print(test.strip())
# ~  233 test
# ~ 233 test
# ~ 233 test