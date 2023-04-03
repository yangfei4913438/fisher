from application import create_app

# 保护内部代码，只能在入口文件执行。（如果文件在作为入口文件执行的时候，__name__ 的值就是 __main__）
# 生产部署的时候，使用其他方式启动服务，所以不需要这里的服务启动代码。
if __name__ == '__main__':
    app = create_app(True)

    # 获取配置文件中定义好的变量
    host = app.config.get('RUN_HOST')
    port = app.config.get('RUN_PORT')

    # 调试模式下，文件改动会自动重启
    # 默认情况下，开发服务器是单进程，多线程运行的。参数是 threaded=True，也可以关闭。
    # 开发服务器，也可以支持多进程，如 processes=5 开启5个进程，但是多进程和多线程不能同时开启。
    app.run(host=host, port=port, threaded=True)

else:
    # 生产环境下会被执行的代码
    app = create_app()
    pass
