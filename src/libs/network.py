"""
从鱼书的pai获取数据

请求库 requests, 智能处理url编码，智能处理返回数据，404不会抛出异常（现在都表示资源不存在）

静态方法，封装在类里面，会便于扩展。

"""
import requests


class HTTP:
    """
    封装网络请求核心类
    """
    
    # 静态方法装饰器
    # 还有一个 classmethod 装饰器，那个会在被修饰方法的第一个参数，多加一个cls参数，用于获取类里面的资源。
    @staticmethod
    def get(url, return_json=True):
        # 请求数据
        r = requests.get(url)

        # 先处理特殊情况
        # -- 不是200表示错误返回
        if r.status_code != 200:
            # 。。。一些上报、日志之类的处理逻辑
            pass
            # 返回空数据格式，具体根据用户传参决定
            return {} if return_json else ''

        # 如果知道服务器返回的是json, 可以直接调用json方法
        # 不是就直接返回text属性
        return r.json() if return_json else r.text
