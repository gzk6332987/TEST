import datetime


def application(pa, func, err):
    """
    处理status和head,并返回
    :return:
    """
    status = '200 OK'
    response_header = [('Content-Type', 'text/html')]
    func(status, response_header)
    x = str(pa) + '===This is a big world!Enjoy it.The time is %s' % str(datetime.datetime.now())

    # 返回
    return x.encode("utf-8")
