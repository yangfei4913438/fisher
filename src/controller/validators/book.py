from wtforms import Form, IntegerField, StringField
from wtforms.validators import DataRequired, Length, NumberRange


class SearchForm(Form):
    # 字符串验证，校验: 是否有值，长度
    q = StringField(validators=[DataRequired(), Length(min=1, max=30)])
    # 数字验证，校验：数字范围, 默认值就是，没有这个传入参数的时候，返回的值
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
