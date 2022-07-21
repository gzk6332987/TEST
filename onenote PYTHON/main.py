import pymysql

conn = pymysql.connect(host='localhost',port=3306,db='joker',user='root',password='root')

# 定义一个标志位，用于控制要执行那种操作
flag = 1

# 创建一个cursor（游标）对象，用于执行SQL语句
cursor = conn.cursor(pymysql.cursors.DictCursor)
'''
pymysql.cursors.DictCursor的作用：让查询结果以字典的形式展示
查询结果：{'id': 8, 'name': 'joker', 'age': 24}
'''
# 增
if flag == 0:
    # sql = 'insert into student(name,age) values("joker",24)'  # 直接将数据填充进去
    sql = 'insert into "tudent"(name,age) values(%s,%s)'       # 使用占位符占位，之后传参
    row = cursor.execute(sql,('joker',24))                   # 参数为一个（即新添加一行数据记录）时使用
    # cursor.executemany(sql,[('tom',38),('jack',26)])   # 参数为多个（即新添加多行数据记录）时使用
    print(row)
# 删
if flag == 1:
    sql = 'delete from student where name=%s'
    row = cursor.execute(sql,('joker',))
    print(row)
# 改
if flag == 2:
    # sql = 'update student set age=%s'
    sql = 'update student set age=%s where name=%s'
    row = cursor.execute(sql,(28,'tom'))
    print(row)
# 查
if flag == 3:
    sql = 'select * from student'
    cursor.execute(sql)
    print(cursor.fetchall())  # 查看全部
    # cursor.scroll(-3,'relative')
    '''
    scroll:用于控制查询开始的位置，类似于控制指针or索引
    relative：相对地址，absolute：绝对地址，2表示在各个地址上的偏移量
    '''
    cursor.scroll(2,'absolute')
    print(cursor.fetchmany(144))  # 查看指定个数,个数（参数）可无限大，取值只会取全部值为止
    print(cursor.fetchone())    # 查看一个


conn.commit()
cursor.close()
conn.close()


