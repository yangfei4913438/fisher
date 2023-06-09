"""
生产环境配置
注意：对外暴露的变量，需要全部大写。
"""
from urllib.parse import quote_plus

# 运行环境
ENV = 'production'

# 关闭调试
DEBUG = False

# 生产服务器信息
RUN_HOST = '127.0.0.1'
RUN_PORT = 8080

# 用于程序内部读取服务器信息
DOMAIN = f"http://{RUN_HOST}:{RUN_PORT}"

# 数据库链接信息
username = 'root'
password = quote_plus('Yf@111111')  # 处理密码中的特殊符号
host = '127.0.0.1'
port = '3306'
database = 'mysql'

# 连接数据库配置
SQLALCHEMY_DATABASE_URI = f"mysql://{username}:{password}@{host}:{port}/{database}"
# 编码格式
SQLALCHEMY_ENCODING = "utf8mb4"
# 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
SQLALCHEMY_TRACK_MODIFICATIONS = False
# 如果设置成 True，SQLAlchemy 将会记录所有 发到标准输出(stderr)的语句，这对调试很有帮助。
SQLALCHEMY_ECHO = False

# 當 flask 偵測到 template 有修改後，禁止自動更新。
TEMPLATED_AUTO_RELOAD = False
