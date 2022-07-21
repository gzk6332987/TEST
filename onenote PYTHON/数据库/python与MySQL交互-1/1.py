import pymysql

def main():
    enter = input("输入你要查询的名称:")
    li = [enter]
    c = pymysql.connect(host='localhost',port=3306,database='jing_dong',user='root',password='123456',charset='utf8')
    cs1 = c.cursor()
    x = cs1.execute("select * from goods left join cate on cate.id=goods.cate_name left join brand on brand.id=goods.brand_name where goods.name=%s;", li)
    print('受影响的行数为:',x)
    for i in range(x):
        print(cs1.fetchone())

if __name__ == '__main__':
    main()