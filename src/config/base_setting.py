"""
基础配置
注意：对外暴露的变量，需要全部大写。
"""
from os import path

# 版本文件的路径(这里只是演示文件的获取，正常情况下，直接写版本号作为变量就行了)
RELEASE_PATH = path.join(path.dirname(path.dirname(path.dirname(__file__))), 'release_version')

# 教学数据源
API_BASE = 'http://t.talelin.com'
# 图书
API_BOOK_BASE = f'{API_BASE}/v2/book'
# 图书查询的url字符串模板
API_BOOK_PATH = API_BOOK_BASE + '/search?q={}&start={}&count={}'
# isbn查询的url字符串模板
API_ISBN_PATH = f'{API_BOOK_BASE}/isbn' + '/{}'

# 豆瓣api
API_DOUBAN = 'https://api.douban.com/v2/book'

# 请求配置
# 每页15条记录
PRE_PAGE = 15
