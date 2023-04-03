"""
蓝图的主要目的是用来拆分不同模块。所以不要为了拆文件去建立一堆蓝图。
"""

from flask import Blueprint, Flask

# 定义蓝图实例，参数：蓝图名称，导入名称
web_server = Blueprint('web_server', __name__)


# 注册蓝图, app通过参数的方式传入
def register_blueprint(app: Flask):
    # 注册web
    app.register_blueprint(web_server, url_prefix='/')
