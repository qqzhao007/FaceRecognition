import psycopg2
import bcrypt


def create_conn():
    """ 连接数据库 """
    database = 'xxxxx'  # 选择数据库名称
    user = 'xxxxx'  # 数据库用户名
    password = 'xxxxxxxxx'
    host = '192.168.xxx.xxx'  # 数据库ip
    port = 'xxxxx'  # 端口号
    conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)  # 连接数据库
    return conn
