def is_isbn_or_key(word):
    """
    判断查询对象的类型，是isbn或者key
    :param word: 查询字符
    :return: key ｜ isbn
    """

    #  类型是普通关键字和isbn
    query_type = 'key'
    # 13位，且都是数字
    if len(word) == 13 and word.isdigit():
        query_type = 'isbn'

    # 10位的isbn
    short_word = word.replace('-', '')
    # 越容易鉴别的条件，放在越前面。例如：长度判断
    # 越耗时的条件，放在后面。例如：数据库查询
    if len(short_word) == 10 and short_word.isdigit() and '-' in word:
        query_type = 'isbn'

    return query_type
