from src.config.base_setting import API_BOOK_PATH, API_ISBN_PATH, PRE_PAGE
from src.libs import HTTP


class YuShuBook:
    # 获取配置
    isbn_url = API_ISBN_PATH
    keyword_url = API_BOOK_PATH
    pre_page = PRE_PAGE

    @classmethod
    def search_by_isbn(cls, isbn):
        # format 可以把参数替换占位符{}
        url = cls.isbn_url.format(isbn)
        print('isbn url:', url)
        result = HTTP.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        url = cls.keyword_url.format(keyword, cls.pre_page, cls.calculate_start(page))
        print('keyword url:', url)
        result = HTTP.get(url)
        return result

    @classmethod
    def calculate_start(cls, page):
        return page * cls.pre_page
