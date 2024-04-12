# 连接momgdb数据库和mysql数据库
import pymongo

import pymysql
mongo = pymongo.MongoClient(host='localhost', port=27017)
db = mongo['test']
collection = db['test']
mysql = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='test')
# 创建游标
cursor = mysql.cursor()


for i in range(1,10):
    print(i)
    # mysql插入数据
    sql = "insert into test(i) values(%s)"
    cursor.execute(sql, (i))
    mysql.commit()
cursor.close()
mysql.close()
print('插入成功')


# cursor.close()
# mysql.close()

