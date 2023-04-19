"""
SQL 综合案例，将MySQL的数据读取到文件中
"""

import json
from pymysql import Connection

# 构建MySQL链接对象
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="bangbang",
)
# 获得游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("py_sql")
# 执行SQL语句
cursor.execute("select * from orders")
# 获取查询结果
results: tuple = cursor.fetchall()

# 关闭MySQL链接对象
conn.close()

# 将查询结果写入文件
with open("orders.json", "w", encoding='utf-8') as f:
    for result in results:
        # 构建JSON字符串
        data = {
            "date": str(result[0]),
            "order_id": result[1],
            "money": result[2],
            "province": result[3]
        }
        json_str = json.dumps(data, ensure_ascii=False)
        # 写入文件
        f.write(json_str + "\n")