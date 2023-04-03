"""
书籍相关的路由
request 只能用于http请求的处理，单独无法使用
"""
from flask import jsonify, request

# 导入蓝图web
from src.controller.blueprint import web_server
# 校验库
from src.controller.validators.book import SearchForm
# 帮助方法
from src.helper.search import is_isbn_or_key
# 网络请求方法
from src.requests.yu_shu_book import YuShuBook


@web_server.route('/book/search')
def book():
    """
    请求范例:
    http://127.0.0.1:1000/book/search?q=9787121215186&page=1
    """
    # 使用校验类
    form = SearchForm(request.args)
    # 执行校验
    if form.validate():
        # 取出校验后的值
        q = form.q.data.strip()  # 去掉前后空白
        page = form.page.data

        # 查询类型判断
        query_type = is_isbn_or_key(q)

        if query_type == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)

        return jsonify(result), 200
    else:
        # 出错的时候，这里会直接拿到错误信息
        return jsonify(form.errors), 400

# 路由注册，也可以使用app直接添加，上面的路由可以写成：
#   app.add_url_rule('/book/search', view_func=book)
