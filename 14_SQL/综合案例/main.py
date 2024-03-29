"""
SQL 综合案例，读取文件，写入MySQL数据库中
"""

from file_define import CsvFileReader, JsonFileReader
from data_define import Record
from pymysql import Connection

csv_file_reader = CsvFileReader("2011年1月销售数据.txt")
json_file_reader = JsonFileReader("2011年2月销售数据JSON.txt")

jan_data: list[Record] = csv_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()
# 将两个月份的数据合并为一个 list 来存储
all_data: list[Record] = jan_data + feb_data

# 构建MySQL链接对象
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="bangbang",
    autocommit=True
)
# 获得游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("py_sql")
# cursor.execute("USE py_sql")
# 组织SQL语句
for record in all_data:
    sql = f"insert into orders values('{record.date}', '{record.order_id}', {record.money}, '{record.province}')"
    # print(sql)
# 执行SQL语句
    cursor.execute(sql)
# 关闭MySQL链接对象
conn.close()