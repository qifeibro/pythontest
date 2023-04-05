"""
面向对象，数据分析案例，主业务逻辑代码
实现步骤：
1. 设计一个类，可以完成数据的封装
2. 设计一个抽象类，定义文件读取的相关功能，并且使用子类实现具体功能
3. 读取文件，生产数据对象
4. 进行数据需求的逻辑计算(计算每一天的销售额)
5. 通过 PyEcharts 进行图形绘制
"""

from file_define import CsvFileReader, JsonFileReader
from data_define import Record
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

csv_file_reader = CsvFileReader("/workspaces/pythontest/13_面向对象/数据分析案例/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("13_面向对象/数据分析案例/2011年2月销售数据JSON.txt")

jan_data: list[Record] = csv_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()
# 将两个月份的数据合并为一个 list 来存储
all_data: list[Record] = jan_data + feb_data

# 开始进行数据计算
data_dict = {}
for record in all_data:
    # if record.date in data_dict.keys()
    # 显式地调用字典的 keys() 方法来获取一个包含所有键的列表，然后检查日期是否在该列表中。在功能上与下面的方式相同，但是它的执行效率可能会略低于下面的方式。
    if record.date in data_dict:    # 使用字典的默认行为来检查日期是否在字典中
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money

# 可视化图表开发
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))

bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("销售额", list(data_dict.values()), label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)

bar.render("每日销售额柱状图.html")