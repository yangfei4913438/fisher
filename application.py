from flask import Flask

from src import db, register_blueprint


def create_app(is_dev: bool = False):
    # 初始化flask
    app = Flask(__name__)

    # 加载基础配置（这里是模块的概念，不是路径哦，下同）
    app.config.from_object('src.config.base_setting')

    # 判断是否为开发环境
    if is_dev:
        # 加载开发环境配置
        app.config.from_object('src.config.local_setting')
    else:
        # 加载生产环境配置
        app.config.from_object('src.config.prod_setting')

    # 初始化蓝图注册
    register_blueprint(app)

    # 初始化数据库应用
    db.init_app(app)

    # with 就是替代 try ... finally 的一种写法，参考：https://www.runoob.com/python3/python-with.html
    # 当出现异常的时候，上下文管理器提供的方法会自动处理，异常后的资源释放。
    with app.app_context():
        # app.app_context() 就是获取到 app 的上下文对象。create_all 方法依赖app的上下文对象，所以要显示的处理。
        # 初始化数据库对象，没有会自动创建
        db.create_all()

    return app
