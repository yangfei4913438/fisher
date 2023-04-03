"""
开发环境配置
注意：对外暴露的变量，需要全部大写。
"""

# 运行环境
ENV = 'development'

# 启用调试
DEBUG = True

# 开发服务器信息
RUN_HOST = '0.0.0.0'
RUN_PORT = 1000

# 数据库链接信息
username = 'yangfei'
password = 'Yf111111'
host = '127.0.0.1'
port = '3306'
database = 'fisher'
# 连接数据库配置（配置文件会被自动读取，不需要显示的引用）
SQLALCHEMY_DATABASE_URI = f"mysql://{username}:{password}@{host}:{port}/{database}"
# 编码格式
SQLALCHEMY_ENCODING = "utf8mb4"
# 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
SQLALCHEMY_TRACK_MODIFICATIONS = True
# 如果设置成 True，SQLAlchemy 将会记录所有 发到标准输出(stderr)的语句，这对调试很有帮助。
SQLALCHEMY_ECHO = True

# 當 flask 偵測到 template 有修改後，會自動去更新。
TEMPLATED_AUTO_RELOAD = True
