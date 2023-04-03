"""
书籍模型类
"""
from src import db


class Books(db.Model):
    __tablename__ = 'book'
    __table_args__ = {
        'comment': '书籍'
    }

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='书籍ID')
    title = db.Column(db.String(50), nullable=False, comment='标题')
    author = db.Column(db.String(30), default='未名', comment='作者')
    binding = db.Column(db.String(20), comment='装帧类型：精装或平装')
    publisher = db.Column(db.String(50), comment='出版社')
    price = db.Column(db.Integer, comment='书籍价格')
    pages = db.Column(db.Integer, comment='书籍页数')
    pubdate = db.Column(db.String(20), comment='出版日期')
    isbn = db.Column(db.String(15), nullable=False, unique=True, comment='书籍编号')
    summary = db.Column(db.Text, comment='书籍简介')
    image = db.Column(db.String(50), comment='书籍封面')

    # mvc 业务应该放在模型层中。
   